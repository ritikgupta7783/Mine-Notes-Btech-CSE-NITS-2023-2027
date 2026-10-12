# Unit 7 — Abstraction: Hide Complexity Behind Simple Operations

**Prerequisite:** Units 2–6.
**Estimated time:** 60–90 minutes.

## 1. An everyday example

You use a television remote by pressing Power or Volume. You do not need to know the circuit details and radio protocol inside the remote. The remote provides a small set of meaningful operations and hides the implementation details.

In software, **abstraction** means showing the operations a caller needs while hiding details that the caller does not need to manage. Encapsulation helps control the internals; abstraction helps define a simple interface.

## 2. A simple public interface

```cpp
#include <iostream>

class CoffeeMachine {
private:
    bool hasWater = true;
    bool hasCoffee = true;

    void heatWater() const {
        std::cout << "Heating water...\n";
    }

public:
    void makeCoffee() const {
        if (!hasWater || !hasCoffee) {
            std::cout << "Cannot make coffee\n";
            return;
        }
        heatWater();
        std::cout << "Coffee is ready\n";
    }
};

int main() {
    CoffeeMachine machine;
    machine.makeCoffee();
}
```

**Output**
```text
Heating water...
Coffee is ready
```

The caller knows makeCoffee(). The private helper heatWater() is an implementation detail. The caller does not need to call internal steps in the right order.

## 3. What should an abstraction expose?

A good interface communicates operations and their results, not every low-level detail. It also needs clear guarantees. If makeCoffee() can fail, the interface should communicate failure through a result, an exception, or documented behaviour.

Abstraction does not mean “hide all code.” It means hide details that are not needed at the current boundary. Developers working inside CoffeeMachine still need to understand its implementation.

## 4. Encapsulation vs abstraction

| Encapsulation | Abstraction |
|---|---|
| Groups state and behaviour and controls access | Chooses the simple view the caller uses |
| Helps prevent invalid state | Helps reduce mental complexity |
| Often uses private data and public functions | Often uses meaningful operations and stable interfaces |
| Focuses on protecting an object | Focuses on what the user of the object needs |

Example: private balance is encapsulation; calling withdraw(amount) without knowing its internal validation steps is abstraction.

## 5. Abstract classes are a more advanced tool

So far, abstraction has used ordinary public functions. Later, we can define a common contract that several classes implement. In C++, a pure virtual function uses = 0. A class with an unimplemented pure virtual final overrider is abstract and cannot be instantiated directly. You do not need an abstract class to practise abstraction.

```cpp
#include <iostream>
#include <string>

class Printer {
public:
    virtual void print(const std::string& text) const = 0;
    virtual ~Printer() = default;
};

class ConsolePrinter : public Printer {
public:
    void print(const std::string& text) const override {
        std::cout << text << '\n';
    }
};

int main() {
    ConsolePrinter printer;
    printer.print("Hello through a simple interface");
}
```

**Output**
```text
Hello through a simple interface
```

This example previews later ideas (inheritance and virtual functions). If you have not studied them yet, focus on the contract: Printer promises that concrete printers provide print(text). The next two units explain inheritance and polymorphism in detail.

## 6. Common mistakes
- Assuming abstraction means deleting or hiding all implementation code.
- Exposing internal helper operations that callers do not need.
- Creating an abstract class when an ordinary method is enough.
- Hiding failure behaviour so callers cannot know whether an action worked.
- Confusing encapsulation (protect the state/operations) with abstraction (simplify the view of the system).

## 7. Practical challenge — Vending Machine (intermediate)

### Problem statement
Build a VendingMachine with private stock counts and a public vend(itemCode) operation. The caller may use code 1 for water and code 2 for juice. Show “dispensed” for available stock, “out of stock” for an empty item, and “unknown item” for other codes. The main function should not directly change stock.

### Worked solution
```cpp
#include <iostream>

class VendingMachine {
private:
    int waterStock = 1;
    int juiceStock = 0;

public:
    void vend(int itemCode) {
        if (itemCode == 1) {
            if (waterStock == 0) {
                std::cout << "Water: out of stock\n";
                return;
            }
            --waterStock;
            std::cout << "Water: dispensed\n";
            return;
        }

        if (itemCode == 2) {
            if (juiceStock == 0) {
                std::cout << "Juice: out of stock\n";
                return;
            }
            --juiceStock;
            std::cout << "Juice: dispensed\n";
            return;
        }

        std::cout << "Unknown item\n";
    }
};

int main() {
    VendingMachine machine;
    machine.vend(1);
    machine.vend(1);
    machine.vend(2);
    machine.vend(99);
}
```

**Output**
```text
Water: dispensed
Water: out of stock
Juice: out of stock
Unknown item
```

The caller supplies an item code and receives a result message. It does not manipulate the stock counters directly. The machine hides the sequence of checking stock, reducing stock and reporting the outcome.

**Stretch task:** return a bool from vend() so other code can react to success/failure without parsing a printed message. Explain why business logic and printing are often separated.

## Practice
1. Give an everyday example of abstraction.
2. Does abstraction require inheritance?
3. Predict what happens on the second call to vend(1).
4. Add code 3 for snacks with stock 2.
5. Explain why direct stock access would weaken the vending machine's interface.

**Hints and answers**
1. ATM users request withdrawal without managing bank database operations.
2. No. Ordinary public methods already create a useful abstraction.
3. It reports water out of stock because the first call reduced waterStock to zero.
4. Add a private snackStock value and a matching branch for item code 3.
5. Callers could reduce stock below zero or bypass checks, making valid behaviour harder to guarantee.

## Quick revision
- Abstraction hides unnecessary detail behind useful operations.
- The interface tells callers what the object can do.
- Encapsulation helps protect the object's internal rules.
- Abstract classes are one advanced form of abstraction, not the only form.
- Public interfaces should communicate failure behaviour.
- The next lessons build abstractions shared across related classes.

## Connection to Unit 8
We now understand classes with simple interfaces. The next question is how to express a genuine relationship between types—for example, Student and Person. Inheritance lets a derived type reuse and extend a base type, when the relationship is valid.

## Additional practice — output and debugging

1. **Easy:** Do callers of CoffeeMachine need to know how heatWater() works?
2. **Easy:** Does abstraction require an abstract base class?
3. **Beginner coding:** Add a public refillWater() operation to CoffeeMachine without exposing hasWater.
4. **Beginner coding:** Change vend() to return true when an item is dispensed and false otherwise.
5. **Output prediction:** If a vending machine starts with one water unit and vend(1) is called twice, what are the two messages?
6. **Debugging:** A caller changes the private juiceStock directly. Explain why the statement fails and how a public operation can replace it.

### Hints and answers
1. No. It only needs the makeCoffee() contract.
2. No; ordinary public methods can provide abstraction.
3. Add a public function that sets hasWater to true inside the class.
4. Return true after reducing stock and false in all rejection paths.
5. First “Water: dispensed”, then “Water: out of stock”.
6. Private members cannot be accessed directly from ordinary callers. Expose a refill operation that validates its input.

### Quick revision
- Abstraction gives callers a small useful interface.
- Internal helper functions can hide implementation steps.
- Encapsulation protects internals; abstraction simplifies the outside view.
- Abstract classes are a later tool, not a requirement for every abstraction.
- Good interfaces make failure behaviour clear.

### Connection to Unit 8
A public interface describes what one class can do. Inheritance lets us express how one type relates to another, and later polymorphism will let different derived types honour a shared interface in their own ways.

---
[← Previous: Unit 6](../Unit-06-Encapsulation/README.md) · [Course home](../README.md) · [Next: Unit 8 — Inheritance →](../Unit-08-Inheritance/README.md)
