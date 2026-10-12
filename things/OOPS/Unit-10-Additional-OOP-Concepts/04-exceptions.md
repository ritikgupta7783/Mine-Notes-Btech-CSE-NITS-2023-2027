# Lesson 10.4 — Exception Handling

## 1. What problem do exceptions solve?

An operation may fail because the input is invalid, a file cannot be opened, or a required resource is unavailable. A function must communicate failure. One choice is a return code; another is to throw an exception for a failure that prevents the operation from fulfilling its contract.

C++ uses try, throw and catch. Learn the flow before memorising the keywords.

## 2. A small working example

```cpp
#include <iostream>
#include <stdexcept>

double divide(double a, double b) {
    if (b == 0.0) {
        throw std::invalid_argument("Divisor cannot be zero");
    }
    return a / b;
}

int main() {
    try {
        std::cout << divide(10, 2) << '\n';
        std::cout << divide(10, 0) << '\n';
    } catch (const std::invalid_argument& error) {
        std::cout << "Error: " << error.what() << '\n';
    }
}
```

**Output**
```text
5
Error: Divisor cannot be zero
```

The first division completes and prints 5. The second throws before returning a number, so execution moves to the matching catch. The statement after that call in the try block would not execute.

## 3. The three keywords
- try: marks code that may throw.
- throw: signals a failure and starts looking for a matching handler.
- catch: handles an exception of a compatible type.

The standard header stdexcept provides types such as invalid_argument, out_of_range and runtime_error. Catch polymorphic exceptions by const reference to avoid unnecessary copying and object slicing.

## 4. Stack unwinding and RAII

When an exception leaves a scope, fully constructed automatic objects in the exited scopes are destroyed in reverse construction order. This is called stack unwinding. A vector, string or smart pointer still cleans up automatically when an exception is thrown; that is why RAII makes exception-safe code simpler.

Do not depend on a destructor running for an object whose constructor never completed. Its already-constructed members/base subobjects are cleaned up, but the incomplete object as a whole never finished construction.

## 5. Custom exceptions

A custom exception can give the caller more information about the problem:
```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class OutOfStock : public std::runtime_error {
public:
    explicit OutOfStock(const std::string& message)
        : std::runtime_error(message) {}
};

int main() {
    try {
        throw OutOfStock("Keyboard not available");
    } catch (const OutOfStock& error) {
        std::cout << error.what() << '\n';
    } catch (const std::exception& error) {
        std::cout << "Other error: " << error.what() << '\n';
    }
}
```

**Output**
```text
Keyboard not available
```

Catch more specific exceptions before general base types, otherwise the general handler may catch them first.

## 6. Exception-safety guarantees

- **No-throw guarantee:** an exception will not escape the operation.
- **Strong guarantee:** if the operation fails, externally visible state remains unchanged.
- **Basic guarantee:** invariants remain valid and resources are not leaked, but state may change.
- **No guarantee:** state/resource validity may be lost; avoid this for normal library interfaces.

noexcept promises that no exception escapes a function; if one does, the program terminates. Destructors should not let exceptions escape, especially during stack unwinding.

## 7. Practical challenge — Validated Ticket Purchase

### Problem statement
A TicketOffice sells a limited number of tickets. buy(count) must reject a non-positive count and reject counts larger than the remaining stock. Use invalid_argument for non-positive counts and out_of_range or a custom exception for insufficient stock. Show one successful purchase and one failed attempt while keeping the remaining stock valid.

### Solution
```cpp
#include <iostream>
#include <stdexcept>

class TicketOffice {
    int remaining;
public:
    explicit TicketOffice(int count) : remaining(count) {
        if (count < 0) throw std::invalid_argument("Initial stock cannot be negative");
    }

    void buy(int count) {
        if (count <= 0) throw std::invalid_argument("Quantity must be positive");
        if (count > remaining) throw std::out_of_range("Not enough tickets");
        remaining -= count;
    }

    int stock() const { return remaining; }
};

int main() {
    TicketOffice office(5);
    try {
        office.buy(3);
        std::cout << "Purchase successful\n";
        office.buy(4);
    } catch (const std::out_of_range& error) {
        std::cout << "Purchase failed: " << error.what() << '\n';
    }
    std::cout << "Remaining: " << office.stock() << '\n';
}
```

**Output**
```text
Purchase successful
Purchase failed: Not enough tickets
Remaining: 2
```

The failed purchase does not subtract anything because the available-stock check happens before mutation. The catch handles the failure at the caller level.

## Common mistakes
- Catching every exception and ignoring it.
- Catching derived exceptions after a general std::exception handler.
- Catching by value when dynamic type matters.
- Throwing exceptions for ordinary, expected branches that can be handled with a return value.
- Letting exceptions escape destructors.
- Forgetting that an exception interrupts the remaining statements in the current try block.

## Interview questions
1. What do try, throw and catch do?
2. What is stack unwinding?
3. Why catch a polymorphic exception by const reference?
4. What is the strong exception guarantee?
5. Does C++ have a finally block? No language-level finally; RAII is typically used for cleanup.
6. What does noexcept mean? No exception may escape; violation terminates.
7. Can a constructor throw? Yes; the object is not fully constructed, and constructed subobjects are cleaned up.
8. How did TicketOffice preserve stock? It validated all failure conditions before changing remaining.

---
[← Previous lesson: Copying, Memory and RAII](03-copy-memory-raii.md) · [Unit 10 overview](README.md) · [Next lesson: Templates and Project Files →](05-templates-namespaces-headers.md)
