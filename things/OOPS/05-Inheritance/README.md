# 05 — Inheritance

## Meaning
Inheritance derives a class from one or more base classes. Public inheritance expresses substitutability: derived objects should honour the base contract.
    #include <iostream>
    struct Animal {
        virtual void speak() const { std::cout << "sound\n"; }
        virtual ~Animal() = default;
    };
    struct Dog : Animal {
        void speak() const override { std::cout << "bark\n"; }
    };

## Types
- **Single:** one direct base.
- **Multilevel:** a derived class becomes a base for another.
- **Multiple:** more than one direct base.
- **Hierarchical:** multiple derived classes share a base.
- **Hybrid:** combination of patterns.

## Inheritance access modes
| Base member | Public inheritance | Protected inheritance | Private inheritance |
|---|---|---|---|
| public | public | protected | private |
| protected | protected | protected | private |
| private | not directly accessible | not directly accessible | not directly accessible |

Default base access: class D : Base is private inheritance; struct D : Base is public inheritance.

## Multiple inheritance and ambiguity
    struct Printer { void run() {} };
    struct Scanner { void run() {} };
    struct Device : Printer, Scanner {};
    // Device d; d.run(); // ambiguous
    // d.Printer::run(); // qualification resolves lookup

## Diamond problem and virtual inheritance
Two intermediate classes may inherit the same base and a final class may inherit both, creating duplicate base subobjects. Virtual inheritance shares one virtual base subobject:
    struct Person { int id = 0; };
    struct Student : virtual Person {};
    struct Employee : virtual Person {};
    struct Assistant : Student, Employee {};

Virtual inheritance differs from virtual functions. The most-derived class initializes virtual bases.

## Rules and traps
Derived classes cannot directly access private base members. Constructors are not virtual; destructors can be virtual. A derived declaration can hide base overloads; using Base::f may reintroduce them. final prevents further derivation/overriding as applicable. Virtual calls during base construction/destruction do not act as if derived portions were fully alive. Prefer composition if inheritance is only code reuse.

## Interview questions
1. What is the diamond problem? Duplicate common-base subobjects and ambiguity through multiple paths.
2. Virtual inheritance vs virtual function? Shared base-subobject arrangement vs runtime dispatch.
3. Does a derived object contain private base state? The base subobject exists, but derived code cannot directly access those private members.
4. When is public inheritance appropriate? When derived objects can honour the base contract.
