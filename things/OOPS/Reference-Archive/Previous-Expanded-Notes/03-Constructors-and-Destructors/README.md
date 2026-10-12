# Unit 03 — Constructors, Destructors and Object Lifetime

**Goal:** Understand when objects are initialized and destroyed, and how modern C++ manages copying, moving and resources safely.

## 1. Constructor: establish a valid starting state

A constructor runs when an object is created. It initializes its base classes and data members, then executes its body. A constructor has the class name and no return type. It can be overloaded so the same type can be initialized in multiple valid ways.

Common forms:
- **Default constructor:** can be called with no arguments.
- **Parameterized constructor:** receives values to initialize state.
- **Copy constructor:** creates an object from another object of the same type, usually T(const T&).
- **Move constructor:** can acquire resources from an rvalue, usually T(T&&).
- **Converting constructor:** accepts another type; explicit prevents unintended implicit conversion.

A default constructor is not always implicitly generated or available. If member/base types cannot be default-constructed, a defaulted constructor can become deleted.

## 2. Why member initializer lists matter

Members are initialized before the constructor body. Writing an assignment in the body does not replace initialization; it assigns after initialization has already happened.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Student {
private:
    const int roll;
    std::string name;
public:
    Student(int r, std::string n)
        : roll(r), name(std::move(n)) {}

    void print() const {
        std::cout << roll << " " << name << '\n';
    }
};

int main() {
    Student s(42, "Mira");
    s.print();
}
```

**Output**
```text
42 Mira
```

The roll member is const, so it must be initialized, not assigned later. References also need initialization. Member initialization order follows the order of declaration in the class, regardless of the order written in the initializer list.

## 3. Default, parameterized and delegating constructors

```cpp
#include <iostream>

class Point {
    int x, y;
public:
    Point() : Point(0, 0) {}       // delegates
    Point(int xValue, int yValue) : x(xValue), y(yValue) {}

    void print() const {
        std::cout << '(' << x << ", " << y << ")\n";
    }
};

int main() {
    Point origin;
    Point p(3, 5);
    origin.print();
    p.print();
}
```

**Output**
```text
(0, 0)
(3, 5)
```

Delegating constructors avoid duplicating initialization logic. Only one constructor in the chain performs the final member initialization.

## 4. Copy construction and copy assignment

These look similar but serve different moments:

```cpp
Widget first;        // construct a new object
Widget second = first; // copy construction
Widget third;
third = first;       // copy assignment into an existing object
```

For a class with ordinary value members, compiler-generated copy operations typically copy each member. For a class that manually owns a resource through a raw pointer, memberwise copying can create two owners of the same resource. That can cause double deletion and undefined behaviour.

## 5. Move constructor and std::move

A move constructor is allowed to transfer an object's resources rather than duplicate them. std::move does not itself move; it converts an expression into an rvalue/xvalue form so the appropriate overload can be chosen. The moved-from object still needs to be safely destructible and assignable, although its value may be unspecified for many library types.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Label {
    std::string text;
public:
    explicit Label(std::string s) : text(std::move(s)) {}
    Label(const Label& other) : text(other.text) {
        std::cout << "copy\n";
    }
    Label(Label&& other) noexcept : text(std::move(other.text)) {
        std::cout << "move\n";
    }
    const std::string& get() const { return text; }
};

int main() {
    Label a("OOP");
    Label b = a;
    Label c = std::move(a);
    std::cout << b.get() << " " << c.get() << '\n';
}
```

**Output**
```text
copy
move
OOP OOP
```

The string is copied into b and moved from a into c. We do not depend on the exact remaining value of a after the move.

## 6. Destructors and destruction order

A destructor is named ~Type and has no return type or parameters. It runs when an object's lifetime ends and should release resources the object owns. In well-designed modern C++, member types such as std::string and std::vector usually clean themselves up.

For a derived object, construction occurs from base to derived: virtual bases, direct bases, data members in declaration order, then constructor body. Destruction is reversed: derived destructor body, members in reverse declaration order, then bases.

A polymorphic base type intended to be deleted through a base pointer should have a virtual destructor.

```cpp
#include <iostream>
struct Base {
    Base() { std::cout << "Base+\n"; }
    virtual ~Base() { std::cout << "Base-\n"; }
};
struct Member {
    Member() { std::cout << "Member+\n"; }
    ~Member() { std::cout << "Member-\n"; }
};
struct Derived : Base {
    Member m;
    Derived() { std::cout << "Derived+\n"; }
    ~Derived() override { std::cout << "Derived-\n"; }
};
int main() {
    Derived d;
}
```

**Output**
```text
Base+
Member+
Derived+
Derived-
Member-
Base-
```

## 7. Rule of three, five and zero

- **Rule of three:** if a class needs a custom destructor, copy constructor or copy assignment for resource management, it probably needs all three.
- **Rule of five:** C++11 adds move constructor and move assignment to the resource-management set.
- **Rule of zero:** design a class from resource-managing members and avoid writing any of those five manually.

Rule of zero is usually preferable. Use vector instead of manually managing an array, string instead of a char buffer, and unique_ptr when unique dynamic ownership is truly required.

## 8. Exception safety during construction

If a constructor throws, the object's destructor is not called for the object as a whole because it never finished construction. However, already-constructed base subobjects and members are destroyed automatically. This is another reason to store resources in RAII members rather than raw resources that need manual cleanup.

## 9. Practical challenge — Resource-Safe Buffer (intermediate/tough)

### Problem
Design a Buffer class that owns a dynamic array of integers:
- construct with a size and initialize all elements to zero;
- support deep copy construction and copy assignment;
- support move construction;
- provide bounds-checked set/get;
- print the contents;
- demonstrate that changing the copy does not change the original.

This exercise intentionally uses raw new[]/delete[] to teach ownership mechanics. For production code, prefer std::vector<int> and the Rule of Zero.

### Worked solution
```cpp
#include <cstddef>
#include <iostream>
#include <stdexcept>
#include <utility>

class Buffer {
private:
    std::size_t size = 0;
    int* data = nullptr;

public:
    explicit Buffer(std::size_t n)
        : size(n), data(n ? new int[n]{} : nullptr) {}

    ~Buffer() {
        delete[] data;
    }

    Buffer(const Buffer& other)
        : size(other.size),
          data(other.size ? new int[other.size] : nullptr) {
        for (std::size_t i = 0; i < size; ++i) data[i] = other.data[i];
    }

    Buffer& operator=(const Buffer& other) {
        if (this == &other) return *this;
        Buffer temp(other); // deep copy; if allocation fails, *this is unchanged
        swap(temp);
        return *this;
    }

    Buffer(Buffer&& other) noexcept
        : size(std::exchange(other.size, 0)),
          data(std::exchange(other.data, nullptr)) {}

    Buffer& operator=(Buffer&& other) noexcept {
        if (this == &other) return *this;
        delete[] data;
        size = std::exchange(other.size, 0);
        data = std::exchange(other.data, nullptr);
        return *this;
    }

    void swap(Buffer& other) noexcept {
        std::swap(size, other.size);
        std::swap(data, other.data);
    }

    void set(std::size_t index, int value) {
        if (index >= size) throw std::out_of_range("Buffer index");
        data[index] = value;
    }

    int get(std::size_t index) const {
        if (index >= size) throw std::out_of_range("Buffer index");
        return data[index];
    }

    void print() const {
        for (std::size_t i = 0; i < size; ++i) {
            if (i) std::cout << ' ';
            std::cout << data[i];
        }
        std::cout << '\n';
    }
};

int main() {
    Buffer original(3);
    original.set(0, 10);
    original.set(1, 20);

    Buffer copied = original; // deep copy
    copied.set(0, 99);

    original.print();
    copied.print();

    Buffer moved = std::move(copied);
    moved.print();
    try {
        std::cout << copied.get(0) << '\n';
    } catch (const std::out_of_range& ex) {
        std::cout << "Moved-from buffer: " << ex.what() << '\n';
    }
}
```

**Output**
```text
10 20 0
99 20 0
99 20 0
Moved-from buffer: Buffer index
```

The move transfers the array to moved and leaves copied with size zero and a null pointer. The bounds-checked access is caught and reported. The copy assignment uses copy-and-swap for a strong guarantee if allocation fails. The copy assignment uses copy-and-swap for a strong guarantee if allocation fails.

### Design review
This class illustrates the Rule of Five, but it is more code than needed for everyday C++. The equivalent production direction is a wrapper containing std::vector<int>, which usually needs no custom destructor/copy/move operations.

## 10. End-of-unit interview questions with answers

**Q1. Constructor vs destructor?**  
A constructor initializes a new object; a destructor releases owned resources as the lifetime ends.

**Q2. Can a constructor be virtual?**  
No. Virtual dispatch requires an object whose dynamic type has already been established; constructors build that object step by step.

**Q3. Can the destructor be overloaded?**  
No. A class has one destructor, although its destructor may be virtual.

**Q4. Copy constructor vs copy assignment?**  
A copy constructor initializes a new object from another. Copy assignment updates an already-existing object.

**Q5. Why are members initialized in declaration order?**  
C++ specifies this order to make object initialization consistent. If the initializer list visually suggests a different order, the declaration order still wins.

**Q6. What is std::move?**  
A cast that produces an xvalue expression and can select move overloads. The selected constructor or assignment performs the actual transfer.

**Q7. Explain the Rule of Five.**  
Resource-owning classes may need a destructor, copy constructor, copy assignment, move constructor and move assignment to manage ownership safely. The Rule of Zero is preferred when possible.

**Q8. What is the risk of a shallow copy of an owning pointer?**  
Two objects may believe they own the same resource and both delete it, causing double deletion/undefined behaviour.

**Q9. Why is a virtual destructor important in a base class?**  
When deletion through a base pointer is supported, it ensures the derived destructor chain is invoked correctly.

**Q10. What is RAII?**  
Resource Acquisition Is Initialization: tie a resource to an object's lifetime so cleanup occurs automatically, including during exceptions.

**Q11. What happens if a constructor throws?**  
The incomplete object's destructor is not called, but fully constructed base and member subobjects are cleaned up automatically.

**Q12. Why does the Buffer example use copy-and-swap?**  
It builds a complete copy first, then swaps ownership. If copying allocation fails, the target object remains unchanged.
