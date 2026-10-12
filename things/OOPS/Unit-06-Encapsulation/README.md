# Unit 6 — Encapsulation: Protect an Object's Rules

**Prerequisite:** Units 2–5: classes, functions, access control and constructors.
**Estimated time:** 75–100 minutes.

## 1. The problem: public data can become invalid

Imagine a bank account whose balance is public. A caller could assign -1000 or withdraw more than the account has. We want every valid account to keep a rule: the balance must not become negative.

**Encapsulation** means keeping related data and the operations that use it together, while controlling how that data can be changed. The rule an object must always preserve is called an **invariant**.

## 2. Before and after

A public-data design lets outside code change balance without permission or checks:

```cpp
struct Account {
    int balance;
};
// Any code could write: account.balance = -500;
```

A more careful design makes balance private and offers operations that check the request. The class is responsible for protecting its own rule.

## 3. Build the bank account step by step

```cpp
#include <iostream>
#include <string>

class BankAccount {
private:
    std::string owner;
    int balance;

public:
    BankAccount(std::string name, int openingBalance)
        : owner(name), balance(openingBalance >= 0 ? openingBalance : 0) {}

    bool deposit(int amount) {
        if (amount <= 0) return false;
        balance += amount;
        return true;
    }

    bool withdraw(int amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        return true;
    }

    int getBalance() const {
        return balance;
    }

    const std::string& getOwner() const {
        return owner;
    }
};

int main() {
    BankAccount account("Asha", 1000);
    account.deposit(250);
    const bool success = account.withdraw(400);
    const bool rejected = account.withdraw(2000);

    std::cout << "Owner: " << account.getOwner() << '\n';
    std::cout << "Withdrawal succeeded: " << std::boolalpha << success << '\n';
    std::cout << "Oversized withdrawal accepted: " << rejected << '\n';
    std::cout << "Balance: " << account.getBalance() << '\n';
}
```

**Output**
```text
Owner: Asha
Withdrawal succeeded: true
Oversized withdrawal accepted: false
Balance: 850
```

## 4. Understand the important lines

- private is the access label for owner and balance. Code in main cannot write account.balance.
- public lists the operations that callers can use.
- The constructor initializes owner and balance when the object is created.
- The condition openingBalance >= 0 ? openingBalance : 0 is a conditional expression: use openingBalance if it is non-negative, otherwise use zero. In a strict banking API, throwing an error or returning a validation result might be preferable; this example chooses a simple fallback.
- deposit() rejects zero and negative amounts. If it accepts the amount, it updates balance and returns true.
- withdraw() rejects non-positive amounts and amounts greater than balance. The state is changed only after both checks pass.
- getBalance() returns a copy of the integer balance and is const because it does not change the account.
- std::boolalpha asks the output stream to print true/false rather than 1/0.

## 5. Getters and setters: use them with a purpose

A **getter** reads information; a **setter** requests a change. A getter does not automatically make a design good, and a setter that accepts every value can defeat encapsulation.

For example, setBalance(int value) that blindly assigns balance=value would allow a negative balance. A method named deposit(amount) communicates a business action and validates its own input.

Returning const std::string& from getOwner() avoids copying the owner name. This syntax is more advanced than the initial lessons; you may instead return std::string by value while learning. The reference is safe here because owner remains a member of the live account object.

## 6. Encapsulation vs simply putting fields in a class

Putting fields and functions inside a class is only the starting point. Encapsulation means deciding which operations are allowed, checking invalid input, hiding implementation details, and keeping the object valid after every public operation.

Access control is not encryption. It protects the program through compiler rules and design contracts; it is not a security boundary against arbitrary memory access.

## 7. Practical challenge — Digital Wallet (intermediate)

### Problem statement
Build a Wallet with a private balance:
- Constructor receives an opening balance; negative opening balance is rejected by using zero.
- addMoney(amount) only accepts positive amounts.
- pay(amount) rejects non-positive payments and payments larger than the balance.
- getBalance() reads the current balance.
- Demonstrate one successful payment and two rejected operations.
- The balance must never become negative.

### Worked solution
```cpp
#include <iostream>

class Wallet {
private:
    int balance;

public:
    explicit Wallet(int opening) : balance(opening >= 0 ? opening : 0) {}

    bool addMoney(int amount) {
        if (amount <= 0) return false;
        balance += amount;
        return true;
    }

    bool pay(int amount) {
        if (amount <= 0 || amount > balance) return false;
        balance -= amount;
        return true;
    }

    int getBalance() const { return balance; }
};

int main() {
    Wallet wallet(500);
    std::cout << wallet.pay(120) << '\n';
    std::cout << wallet.pay(1000) << '\n';
    std::cout << wallet.addMoney(-10) << '\n';
    std::cout << "Balance: " << wallet.getBalance() << '\n';
}
```

**Output**
```text
1
0
0
Balance: 380
```

Dry run: 500 - 120 becomes 380. The next payment is rejected, so balance remains 380. The negative deposit is also rejected. The booleans print as 1 and 0 because boolalpha was not enabled.

**Stretch task:** add a transaction history that records every successful change but does not record rejected requests.

## 8. Common mistakes
- Making sensitive state public “for convenience.”
- Adding a setter that bypasses validation.
- Modifying state before checking all failure conditions.
- Confusing private with encryption.
- Returning a reference to a temporary/local object.
- Assuming a const getter should change the object.

## 9. End-of-unit interview questions with answers

**Q1. What is encapsulation?**  
Keeping related data and operations together and controlling access so the object can protect its rules.

**Q2. What is an invariant?**  
A condition that must remain true for every valid object, such as a wallet balance being non-negative.

**Q3. Why are private members useful?**  
They prevent arbitrary callers from changing internal state and force updates through the class's chosen operations.

**Q4. Are getters and setters required for every field?**  
No. Provide methods that make sense for the domain. A public field may be appropriate for a simple data record, while a field enforcing rules should be carefully controlled.

**Q5. Encapsulation vs data hiding?**  
Data hiding is one technique used by encapsulation. Encapsulation is the broader organization of state/behaviour and protection of the object's contract.

**Q6. How does BankAccount protect its balance?**  
It keeps balance private and verifies the amount before changing the value.

**Q7. Is private the same as secure?**  
No. It is compile-time access control; security also depends on application design, memory safety, authentication and other concerns.

**Q8. Why return bool from deposit()?**  
So the caller can learn whether the requested action succeeded.

**Q9. Why validate before modifying state?**  
If validation fails, the object remains unchanged. This helps preserve invariants.

**Q10. Why is getBalance() const?**  
Because reading the balance should not modify the account.

## Practice before moving on

Try these without looking at the answers first.

1. **Easy:** Why should a wallet's balance normally be private?
2. **Easy:** What should happen to the balance when pay(0) is called?
3. **Beginner coding:** Add a method canAfford(amount) that reports whether a positive amount is no greater than the balance; it must not change the balance.
4. **Beginner coding:** Add a method that can spend all remaining money, but rejects negative/zero amounts.
5. **Output prediction:**

```cpp
Wallet w(100);
w.pay(30);
w.pay(100);
std::cout << w.getBalance() << '\\n';
```

6. **Debugging:** A setter does balance = amount without checking amount. Explain one invalid state it can create and fix the setter.

**Hints:** Validate before changing state. An operation that only answers a question should be const and should not mutate the object.

### Answers
1. So all changes must pass through operations that preserve the balance rule.
2. The call should fail and leave the balance unchanged.
3. Return amount > 0 && amount <= balance.
4. Check amount > 0 and amount <= balance, then subtract it.
5. Output is 70. The second payment is rejected because only 70 remains.
6. Negative amounts can make balance negative. Reject non-positive input or invalid values before assignment.

### Quick revision
- Encapsulation protects the object contract.
- Private data plus validating methods can maintain invariants.
- Validate before mutation; failure should leave state unchanged.
- Getters are observers, not permission to expose every internal detail.
- A public setter that bypasses rules weakens encapsulation.

### Connection to Unit 7
The Wallet lets callers pay without knowing the internal checks. That simple interface is an example of abstraction. Next we learn to design such interfaces deliberately.

---
[← Previous: Unit 5](../Unit-05-Constructors-and-Object-Initialization/README.md) · [Course home](../README.md) · [Next: Unit 7 — Abstraction →](../Unit-07-Abstraction/README.md)
