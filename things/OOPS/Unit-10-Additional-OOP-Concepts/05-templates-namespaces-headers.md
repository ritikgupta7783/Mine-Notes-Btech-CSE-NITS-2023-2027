# Lesson 10.5 — Templates, Namespaces and Header/Source Files

## 1. Templates: reuse an algorithm across types

A template is a recipe the compiler uses to generate a function or class for a type. Templates are often described as compile-time polymorphism. They do not require inheritance.

```cpp
#include <iostream>
#include <string>

template <typename T>
T maximum(T first, T second) {
    return first < second ? second : first;
}

int main() {
    std::cout << maximum(4, 9) << '\n';
    std::cout << maximum(2.5, 1.7) << '\n';
    std::cout << maximum(std::string("Ada"), std::string("Mira")) << '\n';
}
```

**Output**
```text
9
2.5
Mira
```

template <typename T> introduces a type parameter named T. The function takes two T values and returns the greater one according to operator <. The type must support the operations that the function uses. Templates are powerful but should not be introduced before ordinary functions and types are understood.

## 2. Class template

```cpp
#include <iostream>
#include <string>
#include <utility>

template <typename T>
class Box {
    T value;
public:
    explicit Box(T v) : value(std::move(v)) {}
    const T& get() const { return value; }
};

int main() {
    Box<int> number(10);
    Box<std::string> word("OOP");
    std::cout << number.get() << '\n';
    std::cout << word.get() << '\n';
}
```

**Output**
```text
10
OOP
```

Box<int> and Box<std::string> are different concrete specializations. std::move is introduced here as a utility that can help transfer values; it is a cast that affects overload selection, not a magical instruction that moves every object. A beginner can first understand Box with a simple type and study move semantics separately.

## 3. Namespaces prevent name clashes

Suppose two libraries both define a function named print. Namespaces let them use the same name without colliding.

```cpp
#include <iostream>

namespace Geometry {
    int value() { return 10; }
}
namespace Finance {
    int value() { return 20; }
}

int main() {
    std::cout << Geometry::value() << '\n';
    std::cout << Finance::value() << '\n';
}
```

**Output**
```text
10
20
```

The :: operator is called the scope resolution operator. std::cout means cout in the std namespace; Geometry::value means value in Geometry. The operator connects a name to its scope.

## 4. Header files and source files

As projects grow, it is useful to place a class declaration in a header and its function definitions in a source file. A header commonly ends in .h or .hpp; an implementation file commonly ends in .cpp.

Example files:

Student.hpp
```cpp
#ifndef STUDENT_HPP
#define STUDENT_HPP
#include <string>

class Student {
    std::string name;
public:
    explicit Student(const std::string& n);
    void print() const;
};

#endif
```

Student.cpp
```cpp
#include "Student.hpp"
#include <iostream>

Student::Student(const std::string& n) : name(n) {}

void Student::print() const {
    std::cout << name << '\n';
}
```

main.cpp
```cpp
#include "Student.hpp"

int main() {
    Student s("Riya");
    s.print();
}
```

Compile both implementation files together: g++ -std=c++17 main.cpp Student.cpp -o app. The include guard prevents the same header declarations from being processed multiple times in one translation unit. This is a project organisation example; the earlier chapters used single-file programs to keep learning simple.

## 5. Practical challenge — Generic Box and Namespaced Helpers

### Problem statement
Create a template function maximum in a namespace called Helpers. Use it with integers and strings. Print the results. Explain why the namespace is useful and why the function template can be reused without writing separate int and string versions.

### Solution
```cpp
#include <iostream>
#include <string>

namespace Helpers {
    template <typename T>
    T maximum(T a, T b) {
        return a < b ? b : a;
    }
}

int main() {
    std::cout << Helpers::maximum(10, 7) << '\n';
    std::cout << Helpers::maximum(std::string("Asha"),
                                  std::string("Riya")) << '\n';
}
```

**Output**
```text
10
Riya
```

The namespace keeps the helper's name qualified. The template is instantiated for the argument type when needed. For strings, operator < compares according to the string comparison rules; it is not comparing how long the strings are.

## Common mistakes
- Expecting one function template to work with types that do not support its required operations.
- Confusing a template with inheritance-based runtime polymorphism.
- Omitting the header that declares a standard-library feature.
- Defining the same non-inline function in many source files via a header.
- Mixing source-file paths or forgetting to compile all implementation files.
- Putting everything into namespace std (do not do this; adding arbitrary declarations to std is not allowed).

## Interview questions
1. What is a template? A compile-time recipe for generating functions or classes for specified types.
2. Template vs virtual function? Templates usually instantiate at compile time; virtual calls select a method at runtime.
3. What is a namespace? A named scope that helps organize names and prevent collisions.
4. What does :: mean? It qualifies a name with its scope.
5. Why separate header and source files? To expose declarations while keeping implementation separate and easier to maintain.
6. What is an include guard? A preprocessor pattern preventing a header from being included repeatedly in one translation unit.
7. Why is std::vector preferable to manual dynamic arrays for most code? It manages storage and its lifetime and provides a reusable interface.

---
[← Previous lesson: Exception Handling](04-exceptions.md) · [Unit 10 overview](README.md) · [Next: Unit 11 — Practical Projects →](../Unit-11-Practical-Projects/README.md)
