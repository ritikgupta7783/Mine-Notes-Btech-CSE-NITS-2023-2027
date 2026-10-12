# 08 — Memory and Object Lifetime

## Storage duration
- **Automatic:** common for local variables; lifetime ends when scope exits.
- **Dynamic:** acquired through allocation and managed according to ownership rules.
- **Static:** exists for the relevant program lifetime.
- **Thread:** lifetime associated with a thread.

Prefer automatic objects and resource managers over raw owning pointers.

## Shallow vs deep copy
Shallow copying a raw pointer duplicates the address, not the resource. Two objects can then attempt to free the same allocation. Deep copy duplicates the owned resource. Modern C++ often avoids custom resource-copy code by using std::string, std::vector and smart pointers.

## RAII
Resource Acquisition Is Initialization ties resource lifetime to an object's lifetime. A destructor releases it even during exception unwinding. Examples include containers, std::lock_guard and smart pointers.

## Smart pointers
- std::unique_ptr<T>: exclusive ownership; moveable, not copyable.
- std::shared_ptr<T>: shared ownership using reference counting.
- std::weak_ptr<T>: non-owning observation of a shared object; can break cycles.
- Raw pointers/references are commonly non-owning unless the contract says otherwise.
    #include <memory>
    struct Item { ~Item() = default; };
    int main() {
        auto item = std::make_unique<Item>();
        // destroyed automatically at scope exit
    }

## Copy construction vs assignment
T b = a initializes a new object; b = a assigns to an existing object. Move construction/assignment are analogous resource-transfer operations.

## Object slicing
    struct Base { virtual const char* name() const { return "Base"; } };
    struct Derived : Base { const char* name() const override { return "Derived"; } };
    Derived d;
    Base b = d;       // slices derived-specific state
    Base& ref = d;    // preserves polymorphism

## Interview questions
1. **Memory leak?** A resource is not released when no longer needed.
2. **Dangling pointer?** A pointer to an object whose lifetime ended or whose storage is invalid.
3. **Does std::move move?** It enables move-overload selection; the selected operation does the work.
4. **Why prefer unique_ptr by default?** It expresses exclusive ownership without shared-lifetime complexity.
5. **Rule of zero?** Let resource-managing members perform cleanup and use compiler-generated special members.
