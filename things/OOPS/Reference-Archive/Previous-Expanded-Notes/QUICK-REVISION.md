# C++ OOP — Quick Revision Sheet

Use this after finishing the detailed units. It is a recall checklist, not a replacement for the worked examples.

## Four pillars
- **Encapsulation:** group state and behaviour and control access.
- **Abstraction:** expose essential interface and hide implementation details.
- **Inheritance:** derive types; public inheritance should preserve substitutability.
- **Polymorphism:** one interface, multiple behaviours.

## Class rules
- class defaults to private member access and private inheritance.
- struct defaults to public member access and public inheritance.
- private base members are not directly accessible in derived code.
- this is available in non-static member functions, not static ones.
- const member functions are observers unless they modify mutable state.

## Constructors and lifetime
- Constructor initializes a new object; destructor releases owned resources.
- Members initialize in declaration order and destroy in reverse order.
- Copy constructor creates an object; copy assignment changes an existing object.
- std::move enables move overload selection; it does not itself move resources.
- Prefer Rule of Zero; use the Rule of Three/Five when explicitly managing resources.
- RAII connects resource cleanup to object lifetime.

## Inheritance and polymorphism
- Single, multilevel, multiple, hierarchical, hybrid describe hierarchy shapes.
- Virtual inheritance shares a common virtual base subobject in diamond structures.
- Virtual functions enable dynamic dispatch; override checks the programmer's intent.
- Abstract classes cannot be instantiated when a pure virtual final overrider remains unimplemented.
- Polymorphic base classes generally need virtual destructors when deletion through base pointers is supported.
- Object slicing occurs when a derived value is copied into a base object by value.
- Overloading uses parameter lists; return type alone cannot differentiate overloads.

## Operators
- At least one operand must be user-defined or an enumeration.
- Precedence, associativity and arity cannot be changed.
- ::, ., .*, ?: and sizeof cannot be overloaded.
- Prefix increment typically returns a reference to the updated value; postfix takes a dummy int and returns the previous value.

## Memory and exceptions
- unique_ptr: exclusive owner; shared_ptr: shared ownership; weak_ptr: non-owning observer.
- try/throw/catch implement exception handling.
- Catch polymorphic exceptions by const reference.
- RAII cleans resources during stack unwinding.
- Avoid exceptions escaping destructors.

## Templates and STL
- Function/class templates enable generic compile-time code.
- STL includes containers, iterators, algorithms and callable objects.
- vector is suited to contiguous sequence storage; map keeps keys ordered; unordered_map uses hashing.
- Use the C++ standard matching your code, such as g++ -std=c++17.

## Design principles
- Composition usually models has-a; public inheritance models a valid is-a.
- SOLID stands for Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation and Dependency Inversion.
- Dependency injection passes dependencies in rather than constructing concrete ones internally.
- Common patterns: Factory, Strategy, Observer, Adapter and Decorator.

## Ten high-yield interview traps
1. Constructors cannot be virtual.
2. Static member functions cannot be virtual.
3. Function templates themselves cannot be virtual.
4. Return type alone cannot overload functions.
5. Virtual calls in base construction/destruction don't dispatch into not-yet-constructed/already-destroyed derived portions.
6. private inheritance is the default for class; public for struct.
7. A default constructor may be implicitly deleted or not generated.
8. std::move is a cast, not a resource transfer by itself.
9. A derived type must honour the base contract to be a sound public subtype.
10. A vtable is a common implementation technique, not a layout mandated by the C++ standard.

## Recommended revision cycle
1. Explain each pillar from memory.
2. Trace one virtual and one non-virtual call.
3. Sketch construction/destruction order.
4. Explain Rule of Zero and RAII.
5. Solve one practical exercise from Units 1–12 without looking at the solution.
6. Answer interview questions using definition → rationale → example → caveat.
