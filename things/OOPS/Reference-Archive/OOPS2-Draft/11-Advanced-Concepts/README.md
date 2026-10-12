# 11 — Advanced OOP and Design

## SOLID principles
- **Single Responsibility:** one coherent reason to change.
- **Open/Closed:** enable extension without repeatedly modifying stable code.
- **Liskov Substitution:** derived types honour base behavioural contracts.
- **Interface Segregation:** clients should not depend on unused methods.
- **Dependency Inversion:** high-level policy depends on abstractions, not concrete low-level details.

These are design guidelines, not language rules; applying them mechanically can overcomplicate a project.

## Dependency injection
Supply dependencies from outside rather than constructing concrete dependencies internally. This makes dependencies explicit and can simplify testing.
```cpp
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
```

## Common design patterns
- **Factory:** centralizes object creation.
- **Strategy:** encapsulates interchangeable algorithms.
- **Observer:** notifies dependents when a subject changes.
- **Adapter:** converts one interface to another.
- **Decorator:** adds behaviour by wrapping an object.
- **Singleton:** one shared instance; beware global state and testing difficulty.

## Casts
- `static_cast`: compile-time conversion rules; an incorrect downcast can be unsafe.
- `dynamic_cast`: checked cast for suitable polymorphic class types; pointer form returns null on failure, reference form throws `std::bad_cast`.
- `const_cast`: changes cv-qualification; modifying an originally const object through a cast is undefined behaviour.
- `reinterpret_cast`: low-level reinterpretation with strict limits; not a general safe conversion.

## Interview traps
- A virtual call in a base constructor/destructor does not dispatch to the not-yet-constructed/already-destroyed derived portion.
- A virtual function cannot be static; constructors cannot be virtual.
- Polymorphic base classes normally need virtual destructors when base-pointer deletion is supported.
- Prefer `override` for intended overrides.
- Composition often models has-a relationships more cleanly than inheritance.
- Use references/pointers for polymorphism to avoid slicing.

## Design checklist
1. Is this really an is-a relationship?
2. Does every public operation preserve the invariant?
3. Is resource ownership clear and exception-safe?
4. Should a function be `const`, virtual, static or free?
5. Is runtime polymorphism actually needed?
6. Could composition or a template be simpler?
7. Do tests cover invalid input and object lifetime?
