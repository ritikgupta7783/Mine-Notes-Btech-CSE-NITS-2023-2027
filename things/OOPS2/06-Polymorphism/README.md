# 06 — Polymorphism

Polymorphism means one interface can represent multiple types/behaviours.

## Compile-time polymorphism
- **Function overloading:** same name, different parameter lists; return type alone cannot distinguish overloads.
- **Operator overloading:** define intuitive operations for user-defined types.
- **Templates:** generic code instantiated for compatible types.

## Runtime polymorphism
A virtual function can be overridden. Calls through a base pointer/reference dispatch to the final overrider of the dynamic object type.
```cpp
#include <iostream>
struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};
struct Circle : Shape {
    double r;
    explicit Circle(double x): r(x) {}
    double area() const override { return 3.141592653589793 * r * r; }
};
int main() {
    Circle c(2);
    Shape& s = c;
    std::cout << s.area() << '\\n'; // approximately 12.5664
}
```

## Overloading vs overriding vs hiding
| Term | Meaning |
|---|---|
| Overloading | Same function name, different parameter list |
| Overriding | Derived class provides a matching implementation of inherited virtual function |
| Hiding | A derived declaration hides base names/overloads during name lookup |

Use `override` to catch signature mismatches. A pure virtual function (`virtual void draw() = 0;`) makes its class abstract.

## Virtual dispatch implementation
Compilers commonly use a vtable and a vptr, but these are implementation techniques, not a memory layout mandated by the C++ standard. The standard specifies behaviour, not a specific vtable representation.

## Common pitfalls
- Non-virtual calls do not dynamically dispatch.
- Constructors cannot be virtual; static functions cannot be virtual.
- Function templates themselves cannot be virtual.
- Object slicing happens when a derived object is copied into a base object by value.
- A polymorphic base usually needs a virtual destructor if deletion through a base pointer is supported.
- Default arguments are selected from the static type even for virtual functions.

## Interview Q&A
1. **What is dynamic binding?** Selecting a virtual function implementation according to the dynamic type at runtime.
2. **Why use `override`?** It makes the compiler check that the function really overrides a base virtual.
3. **Can a pure virtual function have a definition?** Yes, though the class remains abstract; a pure virtual destructor needs a definition when destruction requires it.
4. **Is virtual dispatch always slow?** It may add indirection, but performance depends on context; measure before optimizing.
