# C++ OOP — Quick Revision Sheet

Use this after studying the numbered beginner course. Return to the unit links whenever a term feels unclear.

## Learning path at a glance
0. Basic C++: programs, variables, conditions, loops, functions, arrays and structs.
1. Why OOP: organize programs around meaningful objects.
2. Classes/objects: type definition vs instance.
3. Member functions: methods attached to a class; scope resolution with ::.
4. Access specifiers: public, private, protected.
5. Constructors: initialize objects; member initializer lists run before the constructor body.
6. Encapsulation: protect rules and object invariants.
7. Abstraction: show useful operations and hide irrelevant detail.
8. Inheritance: model valid is-a relationships.
9. Polymorphism: a common interface supports different behaviour.
10. Additional concepts: static, const, friend, relationships, RAII, exceptions, templates, namespaces and headers.
11. Practical projects.
12. Interview and OA practice.

## Four pillars
- **Encapsulation:** group state and operations; control access to protect object rules.
- **Abstraction:** expose the useful interface, hide implementation detail.
- **Inheritance:** derive a type that can honour the base class contract.
- **Polymorphism:** one interface/operation can represent multiple behaviours.

## Class and object rules
- A class defines a type; an object is an instance with lifetime/state.
- Data members store per-object state unless declared static.
- Member functions define operations.
- Dot syntax object.member is for objects; arrow pointer->member is for pointers.
- class defaults to private member access; struct defaults to public.
- const member functions should not modify ordinary non-mutable state.
- this refers to the current object in a non-static member function.

## Constructors, copying and destruction
- Constructor initializes; it has the class name and no return type.
- No-argument/default and parameterized constructors are common forms.
- Member initializer list starts with a colon and initializes members directly.
- Members initialize in declaration order, not initializer-list text order.
- Copy constructor creates a new object; copy assignment changes an existing object.
- Destructor runs as the lifetime ends.
- Prefer Rule of Zero; resource-owning members should manage cleanup.
- std::move is a cast that can select move operations; it does not itself transfer resources.

## Inheritance and polymorphism
- Single, multilevel, multiple, hierarchical and hybrid describe hierarchy shapes.
- Private base members are not directly accessible in derived code.
- Public inheritance models a genuine is-a relationship; composition usually models has-a.
- Virtual inheritance shares a common base subobject in a diamond.
- Overloading uses different parameter lists; overriding provides a derived implementation for a virtual function.
- override lets the compiler check intended overriding.
- A pure virtual function (= 0) can make a class abstract.
- A polymorphic base normally needs a virtual destructor if deletion through its pointer is supported.
- Object slicing occurs when derived data is lost in a base object copied by value.
- A vtable is a common implementation technique, not a required standard memory layout.

## Memory, exceptions and generic code
- RAII ties resource cleanup to object lifetime.
- unique_ptr: exclusive owner; shared_ptr: shared lifetime; weak_ptr: non-owning observer of shared ownership.
- try, throw and catch handle exceptional failure; catch polymorphic exceptions by const reference.
- Stack unwinding destroys constructed automatic objects while an exception propagates.
- Templates enable reusable code at compile time.
- STL includes containers, iterators, algorithms and callables.
- Namespaces qualify names; headers expose declarations and source files contain definitions.

## Ten interview traps
1. Constructors cannot be virtual.
2. Static member functions cannot be virtual.
3. Function templates themselves cannot be virtual.
4. Return type alone cannot distinguish an overload.
5. class inheritance defaults to private; struct inheritance defaults to public.
6. A default constructor may not exist when other constructors are declared.
7. std::move is a cast, not the move operation itself.
8. The virtual keyword on a base function enables runtime dispatch; without it a base-pointer call is not dynamically dispatched.
9. A derived object copied by value to a base object is sliced.
10. Public inheritance should preserve the base class's behavioural contract.

## Interview answer pattern
Use: **definition → why it matters → example → limitation/trap**. Show understanding by explaining what the code guarantees, who owns resources, how invalid input is handled and what changes at runtime.

## Links
- [Course home](README.md)
- [Glossary](GLOSSARY.md)
- [Troubleshooting](TROUBLESHOOTING.md)
- [Progress checklist](PROGRESS-CHECKLIST.md)
- [Setup and running examples](SETUP-AND-RUN.md)
