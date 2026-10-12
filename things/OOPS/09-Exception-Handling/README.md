# 09 — Exception Handling

C++ uses try, throw and catch to signal and handle exceptional failures.
    #include <iostream>
    #include <stdexcept>
    double divide(double a, double b) {
        if (b == 0) throw std::invalid_argument("division by zero");
        return a / b;
    }
    int main() {
        try { std::cout << divide(10, 0); }
        catch (const std::invalid_argument& e) { std::cerr << e.what() << '\n'; }
    }

## Flow
1. The try block executes.
2. throw searches outward for a matching handler.
3. Stack unwinding destroys fully constructed automatic objects in exited scopes.
4. A matching catch handles the exception; otherwise it propagates.
5. If no handler exists, std::terminate is called.

## Good practices
Catch polymorphic exceptions by const reference; catch derived types before base types; use throw; to rethrow within a handler; prefer meaningful types from stdexcept; use RAII for cleanup; do not use exceptions for ordinary control flow; do not let destructors throw during unwinding.

## Exception-safety guarantees
- **No-throw:** no exception escapes.
- **Strong:** failure leaves observable state unchanged.
- **Basic:** invariants hold and resources are not leaked, though state may change.
- **No guarantee:** avoid where possible.

noexcept promises no exception escapes. If one does, the program terminates; mark functions noexcept only when that promise is true.

## Interview questions
1. Does C++ have finally? No language-level finally; RAII is the usual cleanup mechanism.
2. Stack unwinding? Destruction of automatic objects as an exception propagates.
3. Why catch by const reference? Avoids copies and preserves dynamic type.
4. Can a destructor throw? It should not let exceptions escape; that can terminate during unwinding.
5. Exception safety? Guarantees about state/resources when operations fail.
