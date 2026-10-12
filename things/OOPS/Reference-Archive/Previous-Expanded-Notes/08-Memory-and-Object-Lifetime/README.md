# Unit 08 — Memory, Copying and Object Lifetime

**Goal:** Understand ownership and lifetime; learn why raw owning pointers are risky and how RAII and smart pointers help.

## 1. Storage duration and lifetime

- **Automatic storage duration:** common for local variables; the object is destroyed when its scope exits.
- **Dynamic storage duration:** acquired through allocation and released by an owner or resource manager.
- **Static storage duration:** exists for the relevant program lifetime.
- **Thread storage duration:** lifetime associated with a thread.

Do not confuse a pointer's lifetime with the pointed-to object's lifetime. A pointer can remain in scope after its target has been destroyed, making it dangling.

## 2. Shallow copy and deep copy

A shallow copy of an object containing an owning raw pointer copies the address. Then two objects may attempt to delete the same resource. A deep copy duplicates the owned resource so each object has independent ownership.

The best modern solution is usually not to implement deep copying manually. Use std::vector, std::string, std::unique_ptr or another type that represents ownership correctly.

## 3. RAII — Resource Acquisition Is Initialization

RAII binds a resource's ownership to an object's lifetime. Acquire the resource while constructing the owner and release it in the destructor. If the scope exits normally or by exception, C++ destroys fully constructed automatic objects and the resource manager performs cleanup.

Examples:
- std::vector owns dynamic storage.
- std::unique_ptr owns a dynamically allocated object.
- std::lock_guard owns a mutex lock for a scope.
- std::ifstream owns an open file resource.

## 4. Smart pointers

| Type | Ownership model | Typical use |
|---|---|---|
| unique_ptr<T> | One exclusive owner | Default for dynamic ownership |
| shared_ptr<T> | Shared owners via reference count | Truly shared lifetime |
| weak_ptr<T> | Non-owning observation of shared ownership | Break cycles or check if shared object still exists |
| raw pointer/reference | Usually non-owning | Observe/pass an object when ownership stays elsewhere |

```cpp
#include <iostream>
#include <memory>

struct Report {
    ~Report() { std::cout << "Report cleaned up\n"; }
    void print() const { std::cout << "Generating report\n"; }
};

int main() {
    {
        auto report = std::make_unique<Report>();
        report->print();
    } // unique_ptr destroys Report here
    std::cout << "Scope ended\n";
}
```

**Output**
```text
Generating report
Report cleaned up
Scope ended
```

Avoid using new/delete directly in ordinary application code when a standard container or smart pointer can express ownership.

## 5. Copy constructor vs copy assignment

```cpp
class Item {
public:
    Item() = default;
    Item(const Item&) { /* initialize new object from existing */ }
    Item& operator=(const Item&) { /* update existing object */ return *this; }
};

int main() {
    Item a;
    Item b = a; // copy constructor: b does not exist yet
    Item c;
    c = a;       // copy assignment: c already exists
}
```

Move construction and move assignment are similar operations designed to transfer resources when doing so is appropriate.

## 6. Object slicing

If a Derived object is copied into a Base object by value, the new object only has the Base part. Derived-specific state and virtual identity are sliced off. Use a Base reference or pointer when polymorphism is intended.

```cpp
#include <iostream>
struct Base {
    virtual const char* name() const { return "Base"; }
    virtual ~Base() = default;
};
struct Derived : Base {
    const char* name() const override { return "Derived"; }
};

int main() {
    Derived d;
    Base sliced = d;
    Base& reference = d;
    std::cout << sliced.name() << '\n';
    std::cout << reference.name() << '\n';
}
```

**Output**
```text
Base
Derived
```

## 7. Rule of zero / three / five

Rule of three: a class manually managing a resource may need destructor, copy constructor and copy assignment. Rule of five adds move constructor and move assignment. Rule of zero advises using resource-owning members that already handle these operations correctly.

Rule of zero is usually the safest and shortest approach.

## 8. Practical challenge — Safe Task Queue (intermediate/tough)

### Problem statement
Implement a TaskQueue that stores string tasks using a standard container, lets callers add a task, take the next task, and report whether tasks remain. Empty task names must be rejected. Taking from an empty queue must report an error. Demonstrate that the queue cleans itself up without manual new/delete.

### Worked solution
```cpp
#include <iostream>
#include <queue>
#include <stdexcept>
#include <string>
#include <utility>

class TaskQueue {
private:
    std::queue<std::string> tasks;

public:
    void add(std::string task) {
        if (task.empty()) throw std::invalid_argument("Task cannot be empty");
        tasks.push(std::move(task));
    }

    bool empty() const { return tasks.empty(); }

    std::string takeNext() {
        if (tasks.empty()) throw std::out_of_range("No tasks remain");
        std::string next = tasks.front();
        tasks.pop();
        return next;
    }
};

int main() {
    TaskQueue q;
    q.add("Compile");
    q.add("Run tests");

    while (!q.empty()) {
        std::cout << q.takeNext() << '\n';
    }

    try {
        q.takeNext();
    } catch (const std::out_of_range& e) {
        std::cout << "Handled: " << e.what() << '\n';
    }
}
```

**Output**
```text
Compile
Run tests
Handled: No tasks remain
```

### Why this teaches memory safety
The queue owns strings, and the standard library manages their memory. No custom destructor, copy constructor or move constructor is needed. The class focuses on the queue invariant and error behaviour instead of manual allocation.

**Stretch task:** make TaskQueue movable but non-copyable. When would exclusive ownership of a queue be useful?

## 9. End-of-unit interview questions with answers

**Q1. What is RAII?**  
Resource ownership follows object lifetime. The destructor releases the resource, including when exceptions cause stack unwinding.

**Q2. What is a memory leak?**  
A resource remains allocated or unreleased after the program has lost a reliable way to release it.

**Q3. What is a dangling pointer?**  
A pointer that refers to an object whose lifetime has ended or whose storage is no longer valid.

**Q4. unique_ptr vs shared_ptr?**  
unique_ptr models one exclusive owner. shared_ptr models shared ownership with reference counting and should be used only when lifetime truly needs to be shared.

**Q5. What is weak_ptr for?**  
It observes an object managed by shared_ptr without increasing the strong reference count; it can help break ownership cycles.

**Q6. What does std::move do?**  
It casts an expression to an xvalue so move overloads may be selected; it does not itself move resources.

**Q7. Explain object slicing.**  
Copying a derived object into a base object by value removes derived-specific state. References/pointers preserve dynamic identity.

**Q8. Why prefer standard containers to raw arrays?**  
They manage storage, size and cleanup and can provide safer copying/moving with less custom code.

**Q9. What are the Rule of Three and Rule of Five?**  
Guidelines for resource-managing classes that need custom destruction/copy or move operations. Prefer the Rule of Zero whenever possible.

**Q10. When should you use shared_ptr?**  
When multiple owners genuinely share responsibility for the object's lifetime—not merely because multiple parts of a program need to access the object.
