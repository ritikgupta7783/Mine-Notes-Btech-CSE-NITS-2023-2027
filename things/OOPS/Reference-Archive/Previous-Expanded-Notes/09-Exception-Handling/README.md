# Unit 09 — Exception Handling

**Goal:** Signal exceptional failure clearly, handle errors at a suitable level, and keep objects/resources valid while errors propagate.

## 1. try, throw and catch

- try marks a block whose execution may throw.
- throw signals a failure and starts searching for a matching handler.
- catch handles an exception compatible with the thrown type.

```cpp
#include <iostream>
#include <stdexcept>

double divide(double a, double b) {
    if (b == 0.0) throw std::invalid_argument("Divisor must not be zero");
    return a / b;
}

int main() {
    try {
        std::cout << divide(10, 2) << '\n';
        std::cout << divide(10, 0) << '\n';
    } catch (const std::invalid_argument& ex) {
        std::cout << "Error: " << ex.what() << '\n';
    }
}
```

**Output**
```text
5
Error: Divisor must not be zero
```

The second call throws, so execution jumps to the matching catch. The statement after that call in the try block would not execute.

## 2. Stack unwinding

When an exception leaves a scope, fully constructed automatic objects in the exited scopes are destroyed in reverse construction order. This is stack unwinding. It is why RAII is essential: a smart pointer, lock guard or file stream can clean up without a manually executed cleanup line.

An object whose constructor never completed does not have its ordinary destructor called as a whole, but fully constructed subobjects are destroyed.

## 3. Standard and custom exception types

The standard library provides types such as invalid_argument, out_of_range and runtime_error in <stdexcept>. Use a type that clearly expresses the failure. Catch polymorphic exception objects by const reference to avoid copying and slicing.

```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class InsufficientFunds : public std::runtime_error {
public:
    explicit InsufficientFunds(const std::string& message)
        : std::runtime_error(message) {}
};

int main() {
    try {
        throw InsufficientFunds("Wallet balance is too low");
    } catch (const InsufficientFunds& ex) {
        std::cout << ex.what() << '\n';
    } catch (const std::exception& ex) {
        std::cout << "General error: " << ex.what() << '\n';
    }
}
```

**Output**
```text
Wallet balance is too low
```

Catch the more specific type before a broader base exception type. Otherwise the broad handler may catch it first.

## 4. Rethrowing and catch-all

Inside a catch block, throw; rethrows the current exception preserving its original exception object. Writing throw ex; instead throws a new exception object and can slice if ex is a base reference. catch (...) catches any exception and is normally used only when a broad boundary must perform cleanup or logging before terminating/rethrowing; silently swallowing unknown failures is dangerous.

## 5. Exception-safety guarantees

- **No-throw guarantee:** no exception escapes the operation.
- **Strong guarantee:** if it fails, observable state remains unchanged (transaction-like behaviour).
- **Basic guarantee:** invariants remain valid and no resources leak, but state may have changed.
- **No guarantee:** state/resource validity may be compromised; avoid this for library code.

RAII and operations such as copy-and-swap help achieve stronger guarantees.

## 6. noexcept and destructors

noexcept communicates that a function will not propagate an exception. If one escapes a non-throwing function, C++ calls std::terminate. Mark a function noexcept only when its implementation and members support that promise. Destructors should not let exceptions escape, especially during stack unwinding, because a second exception can terminate the program.

## 7. Practical challenge — Inventory Checkout (intermediate)

### Problem statement
Build an InventoryItem with a stock count. Buying quantity must fail clearly when quantity is non-positive or greater than stock. Define a custom OutOfStock exception derived from runtime_error. Show one successful purchase and one failed purchase, catch the error and print the remaining stock.

### Worked solution
```cpp
#include <iostream>
#include <stdexcept>
#include <string>

class OutOfStock : public std::runtime_error {
public:
    explicit OutOfStock(const std::string& message)
        : std::runtime_error(message) {}
};

class InventoryItem {
private:
    std::string name;
    int stock;

public:
    InventoryItem(std::string itemName, int openingStock)
        : name(std::move(itemName)), stock(openingStock) {
        if (stock < 0) throw std::invalid_argument("Stock cannot be negative");
    }

    void buy(int quantity) {
        if (quantity <= 0) throw std::invalid_argument("Quantity must be positive");
        if (quantity > stock) throw OutOfStock("Not enough stock for " + name);
        stock -= quantity;
    }

    int getStock() const { return stock; }
};

int main() {
    InventoryItem item("Keyboard", 5);
    try {
        item.buy(3);
        std::cout << "Purchase successful\n";
        item.buy(4);
    } catch (const OutOfStock& ex) {
        std::cout << "Purchase failed: " << ex.what() << '\n';
    }
    std::cout << "Remaining: " << item.getStock() << '\n';
}
```

**Output**
```text
Purchase successful
Purchase failed: Not enough stock for Keyboard
Remaining: 2
```

### Why this is safe
The stock is only reduced after both validations pass. If the second purchase fails, stock remains 2. The caller chooses how to respond to the exception, while the class preserves its invariant.

**Stretch task:** make buying multiple items atomic: if any purchase fails, no item's stock should change. What data or transaction strategy would you need?

## 8. End-of-unit interview questions with answers

**Q1. What is exception handling?**  
A language mechanism to signal failures with throw and handle them at a suitable level using try/catch.

**Q2. What is stack unwinding?**  
Destruction of constructed automatic objects in exited scopes while an exception propagates.

**Q3. Why catch by const reference?**  
It avoids copying and preserves the dynamic exception type.

**Q4. Why catch derived exceptions before base exceptions?**  
A base-type handler can match a derived exception, preventing a later derived handler from receiving it.

**Q5. Does C++ have finally?**  
No language-level finally block. RAII normally provides reliable scope cleanup.

**Q6. What is the strong exception guarantee?**  
If an operation fails, it leaves the observable program state unchanged.

**Q7. What does noexcept mean?**  
The function promises no exception will escape. Violating the promise causes termination.

**Q8. Can a destructor throw?**  
A destructor technically can in limited circumstances, but it should not let exceptions escape. Throwing during unwinding may terminate the program.

**Q9. When should exceptions be used?**  
For failures that prevent an operation from fulfilling its contract, not as a replacement for every ordinary branch or expected result.

**Q10. How did InventoryItem preserve stock?**  
It validates quantity and available stock before mutating the stock field; the exception interrupts the failed operation before state changes.
