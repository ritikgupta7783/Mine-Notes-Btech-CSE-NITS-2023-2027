# Unit 04 — Encapsulation, Abstraction and Object Relationships

**Goal:** Learn how classes protect rules, how interfaces hide complexity, and when to use composition instead of inheritance.

## 1. Encapsulation: protect a rule, not just a variable

Suppose a Wallet stores an integer balance. If balance is public, any code can write a negative number. If the balance is private and only deposit() and withdraw() can change it, the class can reject invalid operations.

Encapsulation combines related state and behaviour and controls access. Its real value is maintaining an **invariant**. A private field by itself is not enough: if the class exposes a public setter that accepts every value, the invariant is still unprotected.

```cpp
#include <iostream>

class Wallet {
private:
    int balance;

public:
    explicit Wallet(int openingBalance)
        : balance(openingBalance >= 0 ? openingBalance : 0) {}

    bool deposit(int amount) {
        if (amount <= 0) return false;
        balance += amount;
        return true;
    }

    bool spend(int amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        return true;
    }

    int getBalance() const { return balance; }
};

int main() {
    Wallet w(500);
    w.spend(120);
    std::cout << w.getBalance() << '\n';
    std::cout << w.spend(1000) << '\n';
}
```

**Output**
```text
380
0
```

The second spend is rejected, leaving the balance at 380. The methods expose valid actions instead of exposing the underlying variable.

## 2. Abstraction: simplify what the caller sees

Abstraction means presenting the necessary operations while hiding internal detail. A caller of a payment service might call processPayment(amount) without knowing the network protocol, retry logic or provider-specific API used internally.

An abstraction should not hide important guarantees. A useful interface documents valid input, effects and failure behaviour.

## 3. Encapsulation and abstraction compared

| Encapsulation | Abstraction |
|---|---|
| Groups data and methods and controls access | Presents the essential interface |
| Helps protect invariants | Reduces the amount of detail callers must understand |
| Often uses private/protected/public members | Often uses interfaces, functions and abstract classes |
| Asks: who can change this state? | Asks: what does the caller need to know? |

They support each other but are not identical.

## 4. Association, aggregation and composition

- **Association:** two objects know about or communicate with one another.
- **Aggregation:** a whole references parts that can independently exist; exact semantics depend on the model.
- **Composition:** a whole owns parts whose lifetime is tied to the whole in the design.

```cpp
#include <iostream>
#include <string>
#include <utility>

class Engine {
public:
    void start() const { std::cout << "Engine started\n"; }
};

class Car {
private:
    Engine engine;       // owned subobject: composition
    std::string model;
public:
    explicit Car(std::string m) : model(std::move(m)) {}
    void start() const {
        std::cout << model << ": ";
        engine.start();
    }
};

int main() {
    Car c("City");
    c.start();
}
```

**Output**
```text
City: Engine started
```

A Car has an Engine, so composition is more natural than deriving Car from Engine. For an aggregation example, a Department may refer to Teacher objects that can live independently. In C++, the relationship is implemented using values, references, pointers or smart pointers according to ownership.

## 5. Abstract classes and interface-style design

C++ has no separate interface keyword. A class with an unimplemented pure virtual function is abstract and cannot be instantiated directly. It can still have data members, constructors, regular functions and a virtual destructor.

```cpp
#include <iostream>
#include <memory>
#include <vector>

class Notifier {
public:
    virtual void send(const std::string& message) const = 0;
    virtual ~Notifier() = default;
};

class ConsoleNotifier : public Notifier {
public:
    void send(const std::string& message) const override {
        std::cout << "NOTICE: " << message << '\n';
    }
};

int main() {
    std::unique_ptr<Notifier> n = std::make_unique<ConsoleNotifier>();
    n->send("Build completed");
}
```

**Output**
```text
NOTICE: Build completed
```

The caller depends on Notifier, not on ConsoleNotifier's internals. This can make implementations replaceable and testing easier. The virtual destructor makes deletion through a base pointer safe.

## 6. Interface design checklist

- Keep public methods small and meaningful.
- Validate data at the boundary where it enters.
- Make ownership clear: who creates and who destroys the resource?
- Mark observer methods const.
- Avoid returning mutable references to private data unless that is an intentional part of the contract.
- Give operations clear failure semantics: return false, an error/result type, or throw a meaningful exception where appropriate.
- Do not add an interface for every class without a real need.

## 7. Practical challenge — Payment Checkout (intermediate/tough)

### Problem statement
Create an abstract PaymentMethod with a pay(amount) operation. Implement CardPayment and WalletPayment. Each payment method must reject non-positive amounts. WalletPayment must also reject amounts greater than its current balance and deduct a successful payment. A Checkout class should depend on the PaymentMethod abstraction so different payment types can be substituted without changing Checkout.

### Worked solution
```cpp
#include <iostream>
#include <string>

class PaymentMethod {
public:
    virtual bool pay(int amount) = 0;
    virtual ~PaymentMethod() = default;
};

class CardPayment : public PaymentMethod {
public:
    bool pay(int amount) override {
        if (amount <= 0) return false;
        std::cout << "Card charged: " << amount << '\n';
        return true;
    }
};

class WalletPayment : public PaymentMethod {
private:
    int balance;
public:
    explicit WalletPayment(int opening) : balance(opening >= 0 ? opening : 0) {}

    bool pay(int amount) override {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        std::cout << "Wallet paid: " << amount << '\n';
        return true;
    }

    int getBalance() const { return balance; }
};

class Checkout {
public:
    bool complete(PaymentMethod& method, int amount) {
        return method.pay(amount);
    }
};

int main() {
    Checkout checkout;
    WalletPayment wallet(500);
    CardPayment card;

    std::cout << checkout.complete(wallet, 120) << '\n';
    std::cout << checkout.complete(wallet, 600) << '\n';
    std::cout << checkout.complete(card, 250) << '\n';
    std::cout << "Wallet remaining: " << wallet.getBalance() << '\n';
}
```

**Output**
```text
Wallet paid: 120
1
0
Card charged: 250
1
Wallet remaining: 380
```

### Why the design matters
Checkout only knows the PaymentMethod contract. It does not inspect whether the payment is by card or wallet. The wallet preserves its balance invariant; the card example simulates a successful provider response rather than performing a real transaction. In a production system, payment failure, security, idempotency and provider responses need explicit modelling.

**Stretch task:** introduce a third payment method (UPI simulation) without modifying Checkout. What contract must the new class follow?

## 8. End-of-unit interview questions with answers

**Q1. Define encapsulation.**  
Grouping state and behaviour while controlling access. The goal is to provide safe operations that maintain the object's invariants.

**Q2. Define abstraction.**  
Exposing essential capabilities while hiding implementation details that callers do not need to understand.

**Q3. Are encapsulation and data hiding the same?**  
Data hiding is one technique used by encapsulation. Encapsulation is the broader design of grouping state/behaviour and protecting the contract.

**Q4. Can every private variable be exposed with a getter and still be well-designed?**  
Not necessarily. An interface should expose useful domain operations, not automatically mirror internal representation.

**Q5. What is composition over inheritance?**  
Prefer building a type from collaborators it owns or uses rather than deriving from a type merely to reuse code. Use inheritance where substitutability is real.

**Q6. What is an abstract class?**  
A class with at least one pure virtual final overrider that remains unimplemented. It cannot be instantiated directly.

**Q7. Can an abstract class have a constructor?**  
Yes. Its constructor initializes the base part of derived objects.

**Q8. Why make an abstract interface destructor virtual?**  
Derived objects can be destroyed correctly through a base pointer.

**Q9. Explain dependency inversion in simple language.**  
High-level logic should depend on a stable abstraction rather than being tightly coupled to one concrete implementation.

**Q10. Why does Checkout accept PaymentMethod&?**  
It uses an abstraction by reference, avoids copying a polymorphic object, and enables the correct virtual override to run.
