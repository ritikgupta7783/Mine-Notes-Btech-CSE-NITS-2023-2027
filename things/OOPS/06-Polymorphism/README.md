# 06 — Polymorphism

Polymorphism means one interface can represent multiple types or behaviours.

## Compile-time polymorphism
- **Function overloading:** same name, different parameter lists; return type alone cannot distinguish overloads.
- **Operator overloading:** define intuitive operations for user-defined types.
- **Templates:** generic code instantiated for compatible types.

## Runtime polymorphism
A virtual function can be overridden. Calls through a base pointer/reference dispatch to the final overrider for the dynamic object's type.
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
        std::cout << s.area() << '\n'; // about 12.5664
    }

## Overloading vs overriding vs hiding
| Term | Meaning |
|---|---|
| Overloading | Same name, different parameter list |
| Overriding | Derived class provides matching implementation of inherited virtual function |
| Hiding | A derived declaration hides base names/overloads during name lookup |

Use override so the compiler catches signature mistakes. A pure virtual function (virtual void draw() = 0) makes its class abstract.

## What happens under the hood?
Compilers commonly implement virtual dispatch with a vtable and vptr, but these are implementation techniques, not a required object layout. C++ specifies behaviour rather than a particular vtable representation.

## Common pitfalls
- Non-virtual calls do not dynamically dispatch.
- Constructors cannot be virtual; static functions cannot be virtual.
- Function templates themselves cannot be virtual.
- Object slicing occurs when a derived object is copied into a base object by value.
- A polymorphic base generally needs a virtual destructor when deletion through a base pointer is supported.
- Default arguments are selected from the static type even for virtual functions.

## Interview Q&A
1. Dynamic binding? Selecting a virtual implementation using dynamic type at runtime.
2. Why override? It makes the compiler verify that the function overrides a base virtual.
3. Can a pure virtual function have a definition? Yes, but the class remains abstract; a pure virtual destructor needs a definition if destruction requires it.
4. Is virtual dispatch always slower? It may add indirection; measure in context.
