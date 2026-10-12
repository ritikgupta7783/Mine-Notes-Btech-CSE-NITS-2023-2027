# 11 — Advanced OOP and Design

## SOLID principles
- **Single Responsibility:** one coherent reason to change.
- **Open/Closed:** enable extension without repeatedly modifying stable code.
- **Liskov Substitution:** derived types honour base behavioural contracts.
- **Interface Segregation:** clients should not depend on unused methods.
- **Dependency Inversion:** high-level policy depends on abstractions rather than concrete low-level details.

These are design guidelines, not language rules; applying them mechanically can overcomplicate a project.

## Dependency injection
Supply dependencies from outside instead of constructing concrete dependencies internally. This makes dependencies explicit and can simplify testing.
    #include <string>
    struct Logger {
        virtual void log(const std::string&) = 0;
        virtual ~Logger() = default;
    };
    class Service {
        Logger& logger;
    public:
        explicit Service(Logger& l): logger(l) {}
        void run() { logger.log("service started"); }
    };

## Common design patterns
- **Factory:** centralizes object creation.
- **Strategy:** encapsulates interchangeable algorithms.
- **Observer:** notifies dependents when a subject changes.
- **Adapter:** converts one interface to another.
- **Decorator:** adds behaviour by wrapping an object.
- **Singleton:** one shared instance; beware global state and testing difficulty.

## Casts
- static_cast: conversion according to compile-time rules; an incorrect downcast can be unsafe.
- dynamic_cast: checked cast for suitable polymorphic types; pointer form returns null on failure, reference form throws std::bad_cast.
- const_cast: changes cv-qualification; modifying an originally const object through it is undefined behaviour.
- reinterpret_cast: low-level reinterpretation with strict limits.

## Interview traps
A virtual call in a base constructor/destructor does not dispatch to the not-yet-constructed/already-destroyed derived portion. Virtual functions cannot be static; constructors cannot be virtual. Polymorphic bases normally need virtual destructors when base-pointer deletion is supported. Prefer override; use references/pointers for polymorphism to avoid slicing; composition often models has-a better than inheritance.

## Design checklist
1. Is this really an is-a relationship?
2. Do public operations preserve invariants?
3. Is resource ownership clear and exception-safe?
4. Should a function be const, virtual, static or free?
5. Is runtime polymorphism needed?
6. Could composition or a template be simpler?
7. Do tests cover invalid input and object lifetime?
