# C++ OOP — Quick Revision

## Four pillars
- Encapsulation: group state/behaviour and control access.
- Abstraction: expose essential interface, hide irrelevant implementation.
- Inheritance: derive types; public inheritance should preserve substitutability.
- Polymorphism: one interface, multiple behaviours.

## Defaults and special members
- `class`: private members/base inheritance by default.
- `struct`: public members/base inheritance by default.
- Copy constructor: `T(const T&)`.
- Move constructor: `T(T&&)`.
- Copy/move assignment modify an existing object.
- Destructor: `~T()`.
- Prefer Rule of Zero with standard resource-managing members.

## Polymorphism
- Overloading: same name, different parameter list.
- Overriding: matching derived implementation of virtual function.
- `override`: compiler verifies intent.
- `= 0`: pure virtual; abstract class cannot be instantiated.
- Polymorphic base generally needs virtual destructor if deletion through base pointer is supported.
- Object slicing happens when copying derived object into base object by value.

## Inheritance
Single, multilevel, multiple, hierarchical, hybrid.
Virtual inheritance shares a common virtual base subobject in a diamond; it is not the same as virtual functions.

## Memory and exceptions
- Prefer RAII, containers and smart pointers.
- `unique_ptr`: exclusive; `shared_ptr`: shared; `weak_ptr`: non-owning observer.
- `std::move` enables move overload selection; it does not itself move.
- `try` / `throw` / `catch`; catch polymorphic exceptions by `const&`.
- RAII cleans up during stack unwinding.

## Common traps
1. Return type alone cannot overload a function.
2. Constructors cannot be virtual.
3. Static member functions cannot be virtual.
4. Operator precedence cannot be changed.
5. `::`, `.`, `.*`, `?:`, `sizeof` cannot be overloaded.
6. Private base members are not directly accessible to derived code.
7. Virtual calls during base construction/destruction do not dispatch to derived parts not yet constructed/already destroyed.
8. C++ is multi-paradigm, not pure OOP.
