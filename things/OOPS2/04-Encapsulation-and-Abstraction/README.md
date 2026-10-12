# 04 — Encapsulation, Abstraction and Relationships

## Encapsulation
Encapsulation groups related state and operations and controls how callers access them. It helps preserve invariants, validate input and localize changes. Private fields alone do not guarantee a good abstraction if the public interface still exposes every implementation detail.

## Abstraction
Abstraction presents essential operations and hides details irrelevant to the caller. An interface describes what an operation promises; implementation describes how it fulfils that promise.

| Encapsulation | Abstraction |
|---|---|
| Controls access and groups state/behaviour | Presents essential operations |
| Helps preserve invariants | Reduces conceptual complexity |
| Often uses classes/access specifiers | Often uses public interfaces and abstract base classes |

## Association, aggregation and composition
- **Association:** objects communicate or refer to one another.
- **Aggregation:** a whole refers to parts that can live independently.
- **Composition:** a whole owns parts whose lifetime is tied to the whole in the design.
```cpp
class Engine { public: void start() {} };
class Car {
    Engine engine; // composition: subobject owned by Car
public:
    void start() { engine.start(); }
};
```
Prefer composition for a has-a relationship. Use public inheritance for a genuine is-a relationship.

## Abstract interface
C++ has no separate `interface` keyword. An abstract class can provide an interface:
```cpp
struct Shape {
    virtual double area() const = 0;
    virtual ~Shape() = default;
};
```
A class with a pure virtual function is abstract and cannot be instantiated directly, but it may have constructors, data members and implemented functions.

## Good interface checklist
- Keep public APIs purposeful.
- Validate inputs at boundaries.
- Make ownership and failure behaviour clear.
- Use `const` for observers.
- Avoid exposing mutable internals unintentionally.
- Document preconditions, postconditions and invariants.

## Interview questions
1. **Why not make every field public?** It can allow invalid state and couples callers to representation.
2. **Is a getter always good encapsulation?** No; the interface should model useful operations, not mechanically mirror every field.
3. **What is composition over inheritance?** Assemble behaviour from collaborating objects instead of relying on a hierarchy when no true is-a relation exists.
4. **Can an abstract class have a constructor?** Yes; it initializes the base subobject of derived objects.
