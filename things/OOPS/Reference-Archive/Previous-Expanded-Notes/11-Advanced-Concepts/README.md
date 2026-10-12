# Unit 11 — Advanced OOP and Design Principles

**Goal:** Turn language knowledge into maintainable design: SOLID, dependency injection, composition, design patterns, casts and common traps.

## 1. SOLID, explained simply

SOLID is a set of design guidelines, not language rules.

- **S — Single Responsibility Principle:** a module should have one coherent reason to change. Separate invoice calculation from file export if the two change for different reasons.
- **O — Open/Closed Principle:** extend stable behaviour without constantly editing existing decision logic. A notification service that loops over a virtual Notification interface can accept a new notification type.
- **L — Liskov Substitution Principle:** a derived type must honour the promises callers expect from the base. It must not unexpectedly strengthen preconditions or break guarantees.
- **I — Interface Segregation Principle:** do not force a client to depend on operations it never uses. Several small interfaces can be clearer than one giant interface.
- **D — Dependency Inversion Principle:** high-level policy should depend on an abstraction rather than a low-level concrete implementation.

These principles require judgement. Turning every tiny class into several interfaces creates needless complexity.

## 2. Dependency injection

Dependency injection means a class receives the service it needs instead of constructing a concrete dependency inside itself. Constructor injection makes the dependency visible and easy to replace in a test.

```cpp
#include <iostream>
#include <string>

class Logger {
public:
    virtual void log(const std::string& message) const = 0;
    virtual ~Logger() = default;
};

class ConsoleLogger : public Logger {
public:
    void log(const std::string& message) const override {
        std::cout << "[log] " << message << '\n';
    }
};

class OrderService {
private:
    const Logger& logger;
public:
    explicit OrderService(const Logger& l) : logger(l) {}
    void placeOrder(int orderId) const {
        logger.log("placing order " + std::to_string(orderId));
    }
};

int main() {
    ConsoleLogger logger;
    OrderService service(logger);
    service.placeOrder(42);
}
```

**Output**
```text
[log] placing order 42
```

OrderService is not hard-coded to create a ConsoleLogger. A test logger can be supplied without changing OrderService. The reference does not own the logger, so the caller must keep the logger alive longer than the service.

## 3. Common design patterns

- **Factory:** centralizes object creation when the exact concrete type is selected by input/configuration.
- **Strategy:** wraps interchangeable algorithms behind a shared interface.
- **Observer:** notifies subscribers about subject changes.
- **Adapter:** wraps an incompatible interface behind the interface a client expects.
- **Decorator:** adds behaviour by wrapping an object that follows the same interface.
- **Singleton:** restricts instance creation to one shared object; global state can make testing and concurrency harder.

Patterns are vocabulary for recurring designs, not templates that should be added to every project.

## 4. C++ casts

- **static_cast:** performs conversions checked against compile-time language rules. A wrong downcast can be undefined behaviour.
- **dynamic_cast:** performs a checked cast in suitable polymorphic class hierarchies. A failed pointer cast returns nullptr; a failed reference cast throws std::bad_cast.
- **const_cast:** changes cv-qualification. Modifying an object originally defined as const through a cast is undefined behaviour.
- **reinterpret_cast:** low-level reinterpretation with strict limits; it is not a general safe conversion tool.

When possible, design code around stable interfaces instead of repeatedly asking which concrete type an object is.

## 5. Object slicing and construction-time virtual calls

Slicing occurs when a derived value is copied to a base object by value. Use references/pointers when runtime polymorphism is intended.

Virtual calls in a base constructor or destructor do not dispatch to derived overrides for parts that are not yet constructed or have already been destroyed. Avoid calling virtual extension points from constructors/destructors unless the behaviour is well understood.

## 6. Practical challenge — Discount Engine (intermediate/tough)

### Problem statement
Design a shopping cart that calculates line-item prices using interchangeable discount policies:
- NoDiscount returns the original price.
- PercentageDiscount applies an integer percentage from 0 to 100.
- Cart depends on a DiscountPolicy abstraction.
- Adding a new discount policy must not require rewriting Cart.
Use dependency injection and demonstrate the total for prices 1000 and 500 with a 10% discount. Use integer units to keep this example simple.

### Worked solution
```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <vector>

class DiscountPolicy {
public:
    virtual int apply(int price) const = 0;
    virtual ~DiscountPolicy() = default;
};

class NoDiscount : public DiscountPolicy {
public:
    int apply(int price) const override { return price; }
};

class PercentageDiscount : public DiscountPolicy {
private:
    int percent;
public:
    explicit PercentageDiscount(int p) : percent(p) {
        if (p < 0 || p > 100) throw std::invalid_argument("Percent must be 0..100");
    }
    int apply(int price) const override {
        if (price < 0) throw std::invalid_argument("Price cannot be negative");
        return price - (price * percent / 100);
    }
};

class Cart {
private:
    const DiscountPolicy& policy;
    std::vector<int> prices;
public:
    explicit Cart(const DiscountPolicy& p) : policy(p) {}
    void add(int price) {
        if (price < 0) throw std::invalid_argument("Price cannot be negative");
        prices.push_back(price);
    }
    int total() const {
        int result = 0;
        for (int price : prices) result += policy.apply(price);
        return result;
    }
};

int main() {
    PercentageDiscount tenPercent(10);
    Cart cart(tenPercent);
    cart.add(1000);
    cart.add(500);
    std::cout << "Discounted total: " << cart.total() << '\n';

    NoDiscount none;
    Cart fullPrice(none);
    fullPrice.add(1000);
    fullPrice.add(500);
    std::cout << "Regular total: " << fullPrice.total() << '\n';
}
```

**Output**
```text
Discounted total: 1350
Regular total: 1500
```

### Design explanation
Cart delegates pricing to an abstraction. The policy is injected through the constructor. A new policy (for example, BuyOneGetOneDiscount) can be implemented without adding another conditional inside Cart. In a real checkout, discounts must also define rounding, tax order, promotions eligibility and overflow behaviour.

**Stretch task:** add a capped discount that can reduce the total by at most 200 units. Explain whether the cap belongs to the strategy or the cart.

## 7. Design review checklist
1. Is the inheritance relationship genuinely is-a?
2. Does every public operation preserve invariants?
3. Is resource ownership clear and exception-safe?
4. Can dependencies be injected to make tests practical?
5. Is runtime polymorphism required, or would a template/free function be simpler?
6. Does the interface expose only what a caller needs?
7. Are failure paths, invalid input and object lifetime tested?

## 8. End-of-unit interview questions with answers

**Q1. What is SOLID?**  
Five commonly used OOP design guidelines intended to make code easier to extend and maintain: SRP, OCP, LSP, ISP and DIP.

**Q2. Explain Liskov Substitution Principle.**  
A derived object should work in contexts that expect the base object without breaking the base contract or surprising callers with stronger requirements.

**Q3. What is dependency injection?**  
Supplying a class's dependencies from outside, commonly through its constructor, rather than constructing a concrete dependency inside the class.

**Q4. What is a Strategy pattern?**  
Encapsulating interchangeable algorithms behind a common interface so the client can use different strategies without changing its core logic.

**Q5. Why prefer composition over inheritance?**  
Composition often leads to looser coupling and allows components to be changed independently. Inheritance remains useful for real subtype relationships.

**Q6. static_cast vs dynamic_cast?**  
static_cast applies compile-time conversion rules and does not generally verify a downcast's dynamic type. dynamic_cast checks suitable polymorphic casts at runtime.

**Q7. What is object slicing?**  
A derived object copied by value into a base object loses the derived part.

**Q8. Why not create a Singleton for every shared service?**  
Singletons introduce global state and can couple tests and components. Explicit dependencies often make lifecycle and testing clearer.

**Q9. What does Open/Closed mean?**  
A stable component should be designed so new behaviour can often be added through extension points rather than repeatedly editing its internal decision logic.

**Q10. Why is Cart easier to test with DiscountPolicy?**  
A test policy can return known values or simulate edge cases without needing a real pricing service; the contract is independent of the concrete implementation.
