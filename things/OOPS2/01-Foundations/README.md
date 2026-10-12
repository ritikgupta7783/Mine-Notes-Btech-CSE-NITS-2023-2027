# 01 — OOP Foundations

## What is OOP?
Object-oriented programming organizes a program around objects: entities that combine **state** (data) and **behaviour** (operations). In C++, a class defines a user-defined type and an object is an instance of that type. Example: a bank account has a balance and operations such as deposit and withdraw.

OOP is an organizational approach, not a guarantee of good design. C++ is multi-paradigm and also supports procedural, generic and functional styles.

## The four pillars
- **Encapsulation:** group related data and operations, controlling access so an object can preserve its invariants.
- **Abstraction:** expose a useful interface while hiding implementation details irrelevant to the caller.
- **Inheritance:** derive a type from another type; public inheritance is appropriate when derived objects can honour the base type's contract.
- **Polymorphism:** use one interface with different behaviours. Templates/overloads are common compile-time mechanisms; virtual functions enable runtime dispatch.

## Procedural vs object-oriented programming
| Procedural | OOP |
|---|---|
| Organizes logic around functions | Organizes related state and behaviour around types/objects |
| Data often passes among functions | State can be protected behind operations |
| Reuse through functions/modules | Reuse through composition, templates, and sometimes inheritance |
| Good for simple transformations too | Useful for domain entities with state and behaviour |

Neither paradigm is universally best.

## Example
```cpp
#include <iostream>
#include <string>
#include <utility>
class BankAccount {
    std::string owner;
    int balance; // integer minor units in a real currency design
public:
    BankAccount(std::string name, int opening)
        : owner(std::move(name)), balance(opening >= 0 ? opening : 0) {}
    void deposit(int amount) { if (amount > 0) balance += amount; }
    bool withdraw(int amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        return true;
    }
    int getBalance() const { return balance; }
};
int main() {
    BankAccount a("Asha", 1000);
    a.deposit(250);
    a.withdraw(100);
    std::cout << a.getBalance() << '\\n'; // 1150
}
```
Balance is not publicly writable; callers use operations that validate requests.

## Advantages and limitations
**Advantages:** localizes state and behaviour, supports clear interfaces, makes invariants easier to preserve, and can improve extensibility.
**Limitations:** excessive classes add indirection; deep inheritance is fragile; dynamic dispatch can add complexity; procedural/data-oriented designs can be simpler for some tasks.

## Interview/viva
1. **Is C++ a pure OOP language?** No; it is multi-paradigm.
2. **Class vs object?** A class defines a type; an object is an instance.
3. **Encapsulation vs abstraction?** Encapsulation controls access and groups state/behaviour; abstraction presents essential operations and hides implementation details.
4. **Must every class use inheritance?** No. Prefer composition unless an is-a relationship is genuine.
5. **What is an invariant?** A condition that must remain true for a valid object.
