# 03 — Constructors and Destructors

## Constructors
A constructor initializes a new object and helps establish its invariants. It has the class name and no return type. Common forms:
- default constructor;
- parameterized constructor;
- copy constructor (`T(const T&)`);
- move constructor (`T(T&&)`);
- converting constructor, often marked `explicit`.

A default constructor is not always generated or available; declaring other constructors can affect implicit generation.

## Initializer lists
```cpp
class Student {
    const int roll;
    std::string name;
public:
    Student(int r, std::string n) : roll(r), name(std::move(n)) {}
};
```
Members initialize in **declaration order**, not the order written in the initializer list. Initializer lists are required for references, const members and members without a suitable default constructor.

## Copy and move
A copy constructor initializes a new object from another. A move constructor can transfer resources from an expiring object. `std::move(x)` is a cast enabling move overload selection; it does not itself transfer resources.
```cpp
#include <iostream>
#include <string>
#include <utility>
struct Label {
    std::string text;
    explicit Label(std::string s): text(std::move(s)) {}
    Label(const Label& x): text(x.text) { std::cout << "copy\\n"; }
    Label(Label&& x) noexcept: text(std::move(x.text)) { std::cout << "move\\n"; }
};
```

## Destructor and order
A destructor (`~Type`) releases resources when object lifetime ends. Construction order: virtual bases, direct bases, members in declaration order, constructor body. Destruction reverses this sequence. If construction throws, already-constructed subobjects are destroyed.

For polymorphic base classes that permit deletion through a base pointer, provide a virtual destructor:
```cpp
struct Base { virtual ~Base() = default; };
struct Derived : Base { ~Derived() override = default; };
```

## Rule of three/five/zero
- **Three:** destructor, copy constructor, copy assignment.
- **Five:** also move constructor and move assignment.
- **Zero:** prefer resource-owning standard types (`std::string`, `std::vector`, smart pointers) so custom resource-management functions are unnecessary.

## Interview questions
1. **Can constructors be virtual?** No; the most-derived object is not fully constructed yet.
2. **Can a destructor be overloaded?** No.
3. **Copy construction vs assignment?** The former creates a new object; the latter changes an existing one.
4. **Why initializer lists?** Direct initialization and support for const/reference/no-default-constructor members.
5. **What is a delegating constructor?** One constructor invokes another constructor of the same class in its initializer list.
6. **Why should destructors not throw?** An exception escaping during stack unwinding can cause termination.
