# 09 — Exception Handling

C++ uses `try`, `throw` and `catch` to signal and handle exceptional failures.
```cpp
#include <iostream>
#include <stdexcept>
double divide(double a, double b) {
    if (b == 0) throw std::invalid_argument("division by zero");
    return a / b;
}
int main() {
    try { std::cout << divide(10, 0); }
    catch (const std::invalid_argument& e) { std::cerr << e.what() << '\\n'; }
}
```

## Flow
1. The `try` block executes.
2. `throw` searches outward for a matching handler.
3. Stack unwinding destroys fully constructed automatic objects in exited scopes.
4. A matching `catch` handles the exception; otherwise it propagates.
5. If no handler exists, `std::terminate` is called.

## Good practices
- Catch polymorphic exceptions by `const&`.
- Catch derived exception types before base types.
- Use `throw;` to rethrow the current exception from a handler.
- Prefer meaningful standard exception types from `<stdexcept>`.
- Use RAII so resources are released during unwinding.
- Avoid routine control flow via exceptions.
- Do not let destructors throw during stack unwinding.

## Exception safety guarantees
- **No-throw:** no exception escapes.
- **Strong:** failure leaves observable state unchanged.
- **Basic:** invariants hold and resources are not leaked, but state may change.
- **No guarantee:** avoid where possible.

`noexcept` promises that exceptions will not escape; if one does, the program terminates. Only use it when the promise is true.

## Interview questions
1. **Does C++ have `finally`?** No language-level `finally`; RAII is the usual cleanup mechanism.
2. **What is stack unwinding?** Destruction of constructed automatic objects as an exception propagates.
3. **Why catch by reference?** Avoids copies and preserves dynamic exception type.
4. **Can a destructor throw?** It should not let exceptions escape; doing so during unwinding can terminate.
5. **What is exception safety?** Guarantees about state and resources when operations fail.
