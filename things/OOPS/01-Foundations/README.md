# 01 — OOP Foundations

## What is object-oriented programming?
Object-oriented programming organizes a program around objects that combine state (data) and behaviour (operations). In C++, a class defines a user-defined type and an object is an instance of it. A bank account, for example, has a balance and operations such as deposit and withdraw.

OOP is an organizational approach, not a guarantee of good design. C++ is multi-paradigm and also supports procedural, generic and functional styles.

## The four pillars
- **Encapsulation:** group related state and operations, controlling access so an object can preserve its invariants.
- **Abstraction:** expose a useful interface while hiding implementation details callers do not need.
- **Inheritance:** derive a type from another; public inheritance is appropriate when the derived type honours the base contract.
- **Polymorphism:** one interface can represent multiple behaviours. Templates and overloads are common compile-time mechanisms; virtual functions enable runtime dispatch.

## Procedural vs OOP
| Procedural | OOP |
|---|---|
| Organizes logic around functions | Organizes related state and behaviour around types and objects |
| Data often passes among functions | State can be protected behind operations |
| Reuse through functions and modules | Reuse through composition, templates and sometimes inheritance |
| Excellent for straightforward transformations | Useful for domain entities with state and behaviour |

Neither paradigm is universally best.

## Example: encapsulated bank account
    #include <iostream>
    #include <string>
    #include <utility>
    class BankAccount {
        std::string owner;
        int balance;
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
        std::cout << a.getBalance() << '\n'; // 1150
    }

The balance is not publicly writable; operations validate requests and preserve the account invariant. Integer minor units are often preferable to floating point for currency.

## Advantages and limitations
**Advantages:** localizes state and behaviour, supports clear interfaces, helps preserve invariants and can improve extensibility.
**Limitations:** excessive classes add indirection; deep inheritance can be fragile; runtime dispatch can add complexity; procedural or data-oriented designs may be simpler for some tasks.

## Viva and interview questions
1. **Is C++ pure OOP?** No, it is multi-paradigm.
2. **Class vs object?** Type definition vs instance.
3. **Encapsulation vs abstraction?** Encapsulation controls access and groups state/behaviour; abstraction presents essential operations and hides irrelevant details.
4. **Must every class use inheritance?** No; prefer composition unless an is-a relationship is genuine.
5. **What is an invariant?** A condition that must remain true for a valid object.
