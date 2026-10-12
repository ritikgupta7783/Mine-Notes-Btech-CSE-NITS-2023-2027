# 08 — Memory and Object Lifetime

## Storage duration
- **Automatic:** common for local variables; lifetime ends when scope exits.
- **Dynamic:** acquired through allocation and must be managed according to ownership rules.
- **Static:** exists for the relevant program lifetime.
- **Thread:** lifetime associated with a thread.

Prefer automatic objects and standard resource managers over raw owning pointers.

## Shallow vs deep copy
Shallow copying a raw pointer duplicates the address, not the resource. Two objects can then attempt to free the same allocation. Deep copying duplicates the owned resource. Modern C++ often avoids custom resource-copy code with `std::string`, `std::vector` and smart pointers.

## RAII
Resource Acquisition Is Initialization ties a resource's lifetime to an object's lifetime. A destructor releases it even during exception unwinding. Examples include containers, `std::lock_guard` and smart pointers.

## Smart pointers
- `std::unique_ptr<T>`: exclusive ownership; moveable, not copyable.
- `std::shared_ptr<T>`: shared ownership using reference counting.
- `std::weak_ptr<T>`: non-owning observation of a shared object; can break cycles.
- Raw pointers/references are commonly non-owning unless the contract says otherwise.
```cpp
#include <memory>
struct Item { ~Item() = default; };
int main() {
    auto item = std::make_unique<Item>();
    // automatically destroyed at scope exit
}
```

## Copy construction vs assignment
`T b = a;` initializes a new object (copy construction). `b = a;` assigns to an existing object (copy assignment). Move construction/assignment are analogous resource-transfer operations.

## Object slicing
```cpp
struct Base { virtual const char* name() const { return "Base"; } };
struct Derived : Base { const char* name() const override { return "Derived"; } };
Derived d;
Base b = d; // slices derived-specific state
Base& ref = d; // preserves polymorphic identity
```

## Interview questions
1. **Memory leak?** A resource is not released when no longer needed.
2. **Dangling pointer?** A pointer to an object whose lifetime has ended or whose storage is invalid.
3. **Does `std::move` move?** It enables move overload selection; the operation selected does the work.
4. **Why prefer `unique_ptr` by default?** It expresses simple exclusive ownership without shared-lifetime complexity.
5. **What is the Rule of Zero?** Let resource-managing members handle cleanup and use compiler-generated special members.
