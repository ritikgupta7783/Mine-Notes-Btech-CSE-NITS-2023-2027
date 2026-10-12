# 05 — Inheritance

## Meaning
Inheritance derives a class from one or more base classes. Public inheritance expresses substitutability: derived objects should honour the base contract.
```cpp
struct Animal {
    virtual void speak() const { std::cout << "sound\\n"; }
    virtual ~Animal() = default;
};
struct Dog : Animal {
    void speak() const override { std::cout << "bark\\n"; }
};
```

## Types
- **Single:** one direct base.
- **Multilevel:** a derived class becomes a base for another.
- **Multiple:** more than one direct base.
- **Hierarchical:** multiple derived classes share a base.
- **Hybrid:** combination of patterns.

## Access modes
| Base member | Public inheritance | Protected inheritance | Private inheritance |
|---|---|---|---|
| public | public | protected | private |
| protected | protected | protected | private |
| private | not directly accessible | not directly accessible | not directly accessible |

Default base access: `class D : Base` is private inheritance; `struct D : Base` is public inheritance.

## Multiple inheritance and ambiguity
```cpp
struct Printer { void run() {} };
struct Scanner { void run() {} };
struct Device : Printer, Scanner {};
// Device d; d.run(); // ambiguous
// d.Printer::run(); // qualify to resolve
```

## Diamond problem and virtual inheritance
When two intermediate classes inherit the same base and a final class inherits both, duplicate base subobjects may result. Virtual inheritance shares one virtual base subobject:
```cpp
struct Person { int id = 0; };
struct Student : virtual Person {};
struct Employee : virtual Person {};
struct Assistant : Student, Employee {};
```
Virtual inheritance is different from virtual functions. The most-derived class initializes virtual bases.

## Rules and traps
- Derived classes cannot directly access private base members.
- Constructors are not virtual; destructors can be virtual.
- A derived declaration may hide base overloads; `using Base::f;` can reintroduce them.
- `final` prevents further derivation or overriding as applicable.
- Virtual calls during base construction/destruction do not behave as though the most-derived portion were fully alive.
- Prefer composition if inheritance is only for code reuse.

## Interview questions
1. **What is the diamond problem?** Duplicate common-base subobjects and potential ambiguity through multiple paths.
2. **Virtual inheritance vs virtual function?** Shared base-subobject layout versus runtime dispatch.
3. **Does a derived object contain private base state?** The base subobject exists, but its private members are not directly accessible by derived code.
4. **When is public inheritance appropriate?** When every derived instance can honour the base type's contract.
