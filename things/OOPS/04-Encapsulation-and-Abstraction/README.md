# 04 — Encapsulation, Abstraction and Relationships

## Encapsulation
Encapsulation groups related state and operations and controls how callers access them. It helps preserve invariants, validate input and localize changes. Private fields alone do not guarantee a good abstraction if the public interface exposes every implementation detail.

## Abstraction
Abstraction presents essential operations and hides details irrelevant to the caller. An interface states what an operation promises; implementation determines how it fulfils the promise.

| Encapsulation | Abstraction |
|---|---|
| Controls access and groups state/behaviour | Presents essential operations |
| Helps preserve invariants | Reduces conceptual complexity |
| Often uses classes/access specifiers | Often uses public interfaces and abstract base classes |

## Association, aggregation and composition
- **Association:** objects communicate or refer to one another.
- **Aggregation:** a whole refers to parts that can live independently.
- **Composition:** a whole owns parts whose lifetime is tied to it in the design.
    class Engine { public: void start() {} };
    class Car {
        Engine engine; // composition: subobject owned by Car
    public:
        void start() { engine.start(); }
    };

Prefer composition for a has-a relationship. Use public inheritance for a genuine is-a relationship.

## Abstract interface
C++ has no separate interface keyword. An abstract class can provide an interface:
    struct Shape {
        virtual double area() const = 0;
        virtual ~Shape() = default;
    };

A class with a pure virtual function is abstract and cannot be instantiated directly, but may have constructors, data members and implemented functions.

## Interface checklist
Keep APIs purposeful, validate at boundaries, make ownership and failure behaviour clear, use const for observers, avoid exposing mutable internals accidentally, and document invariants plus preconditions/postconditions.

## Interview questions
1. Why not make every field public? That can allow invalid state and couple callers to representation.
2. Is a getter always good encapsulation? No; an API should expose useful operations rather than mirror every field mechanically.
3. What is composition over inheritance? Assemble behaviour from collaborators rather than forcing a hierarchy where there is no true is-a relationship.
4. Can an abstract class have a constructor? Yes; it initializes the base subobject of derived objects.
