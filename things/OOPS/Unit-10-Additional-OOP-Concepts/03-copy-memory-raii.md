# Lesson 10.3 — Copying, Destructors, Dynamic Memory and RAII

## 1. Every object has a lifetime

An object begins its lifetime when it has been properly created/initialized, and its lifetime ends when destruction rules say it ends. A local variable commonly lives until the block exits. A dynamically allocated object may outlive the function that created it, so someone must own it and ensure it is released.

## 2. Destructor and cleanup

A destructor is named ~Type and runs when the object's lifetime ends. Its job commonly includes releasing resources owned by the object. Classes such as std::string and std::vector already manage their own storage, so ordinary classes often need no custom destructor.

```cpp
#include <iostream>
#include <string>

class Note {
    std::string text;
public:
    explicit Note(std::string t) : text(t) {
        std::cout << "Created: " << text << '\n';
    }
    ~Note() {
        std::cout << "Destroyed: " << text << '\n';
    }
};

int main() {
    Note n("OOP");
    std::cout << "Inside main\n";
}
```

**Output**
```text
Created: OOP
Inside main
Destroyed: OOP
```

The Note variable is local to main, so it is destroyed when main's block exits. The string member owns its text storage and is destroyed automatically after the destructor body completes.

## 3. Copying values: shallow vs deep copy

For ordinary value members, copying each member may be correct. But copying a raw owning pointer copies the address, not the resource. Two objects can then believe they own the same allocation and may attempt to delete it twice.

- **Shallow copy:** copies the pointer/address, not the pointed-to resource.
- **Deep copy:** duplicates the resource so each object has independent ownership.

The easier modern approach is often to use a standard resource-owning type such as std::vector or std::string, which already implements copying/moving correctly.

## 4. Dynamic allocation and the danger of raw new/delete

The new expression requests dynamic storage and constructs an object. delete destroys the object and releases storage. Every owning new needs a correctly matched cleanup path; arrays use new[] and delete[] as a pair.

```cpp
#include <iostream>
int main() {
    int* number = new int(42);
    std::cout << *number << '\n';
    delete number;
    number = nullptr;
}
```

**Output**
```text
42
```

The asterisk in *number accesses the integer through the pointer. After delete, the pointer no longer points to a live allocated integer. Setting it to nullptr prevents this local variable from retaining the old address, but it does not fix other copied pointers. Prefer smart pointers/containers in normal code.

## 5. RAII

RAII means **Resource Acquisition Is Initialization**. In simple terms, put ownership of a resource inside an object whose destructor releases it. C++ destroys fully constructed local objects on normal scope exit and during exception unwinding, so the cleanup is reliable.

Examples of RAII types: std::string, std::vector, std::ifstream, std::lock_guard and smart pointers.

## 6. Smart pointers

- std::unique_ptr represents one exclusive owner. It can move to a different owner but cannot be copied.
- std::shared_ptr represents shared ownership; the object is destroyed when the last shared owner is released.
- std::weak_ptr observes an object managed by shared_ptr without keeping it alive. It can help break shared_ptr cycles.
- A raw pointer/reference is commonly used as a non-owning view. The lifetime contract must be clear.

```cpp
#include <iostream>
#include <memory>

struct FileLikeResource {
    FileLikeResource() { std::cout << "Acquire\n"; }
    ~FileLikeResource() { std::cout << "Release\n"; }
};

int main() {
    {
        auto resource = std::make_unique<FileLikeResource>();
        std::cout << "Work\n";
    }
    std::cout << "Finished\n";
}
```

**Output**
```text
Acquire
Work
Release
Finished
```

std::make_unique creates an object managed by unique_ptr. When resource leaves the inner scope, its destructor releases the FileLikeResource automatically. No explicit delete appears.

## 7. Practical challenge — Resource Owner

### Problem statement
Write a small class that owns a dynamically allocated integer safely using unique_ptr. It should initialize the value in the constructor, update it through a public method and print it through a const method. Demonstrate that the object cleans up automatically at scope exit. This challenge practices ownership; do not write a custom copy constructor.

### Solution
```cpp
#include <iostream>
#include <memory>

class Score {
    std::unique_ptr<int> value;
public:
    explicit Score(int initial)
        : value(std::make_unique<int>(initial)) {}

    void set(int next) { *value = next; }
    int get() const { return *value; }
};

int main() {
    {
        Score score(60);
        std::cout << score.get() << '\n';
        score.set(95);
        std::cout << score.get() << '\n';
    }
    std::cout << "Score object left scope\n";
}
```

**Output**
```text
60
95
Score object left scope
```

The unique_ptr member owns the integer. When Score is destroyed, its member's destructor releases the integer. Score is automatically non-copyable because unique_ptr is non-copyable; if copying is required, design what copy should mean rather than copying an address accidentally.

## 8. Common mistakes
- Losing the only pointer to an allocation before deleting it (memory leak).
- Using a pointer after its target's lifetime ends (dangling pointer).
- Deleting the same resource twice.
- Using delete for memory allocated with new[] instead of delete[].
- Copying an owning raw pointer without deciding whether the copy should share or duplicate ownership.
- Using shared_ptr when unique ownership is enough.
- Believing std::move itself performs a transfer.

## Interview questions
1. **What is a memory leak?** A resource remains allocated/unreleased after the program has lost a reliable way to release it.
2. **What is a dangling pointer?** A pointer referring to an object whose lifetime has ended or to invalid storage.
3. **What is RAII?** Tying resource ownership and cleanup to an object's lifetime.
4. **unique_ptr vs shared_ptr?** Exclusive ownership vs shared lifetime.
5. **Why prefer Rule of Zero?** Resource-owning members perform cleanup/copying, so custom special-member code is often unnecessary.
6. **What is object slicing?** A derived object copied into a base object by value loses the derived part.
7. **Does std::move move?** It casts to an xvalue to enable move overload selection; the selected operation performs the transfer.
8. **When is shared_ptr appropriate?** When there truly are multiple owners of the object's lifetime.

---
[← Previous lesson: Object Relationships](02-object-relationships.md) · [Unit 10 overview](README.md) · [Next lesson: Exception Handling →](04-exceptions.md)
