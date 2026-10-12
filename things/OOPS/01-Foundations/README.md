# Unit 01 — Foundations of Object-Oriented Programming

**Goal:** Understand what OOP solves, learn its vocabulary, and identify the four pillars in real code.

## 1. Start with the problem

Imagine a college application storing the names, roll numbers, CGPAs and attendance of hundreds of students. With only unrelated variables, the code soon becomes difficult to maintain. A procedure-based program may organize data in structs and use functions to process it. OOP offers another way: create a Student type that groups the student's state and the operations that make sense for that student.

OOP is not simply “put every line inside a class.” It is a way to choose sensible boundaries for a program. A simple calculation may be clearer as a free function; a bank account that must never have a negative balance is a good candidate for a class that protects its state.

## 2. Essential vocabulary

- **Class:** a user-defined type that describes data, operations and access rules.
- **Object:** an instance of a class, with a lifetime and its own state.
- **State:** current values, such as the balance of one account.
- **Behaviour:** operations an object offers, such as deposit or withdraw.
- **Interface:** what code outside the class is allowed to use.
- **Implementation:** the internal details that make the interface work.
- **Invariant:** a rule that must remain true for every valid object, such as balance ≥ 0.
- **Abstraction boundary:** the line between what callers need to know and what can remain private.

An object is not identical to its class. One Student class can have thousands of Student objects, each with different values.

## 3. The four pillars, in plain language

### Encapsulation — protect the object's rules
Keep closely related state and operations together. Restrict uncontrolled writes to important data and provide operations that validate changes. A private field is not secure encryption; it is a language-level access rule that helps prevent accidental misuse.

### Abstraction — give callers a simpler model
A caller asks an object to perform an operation without knowing every internal step. For example, a caller uses a vector's push_back operation without managing vector memory directly.

### Inheritance — model a valid “is-a” relation
A derived type can reuse and extend a base type. Public inheritance is suitable only if derived objects can safely stand in for base objects. “Car uses an Engine” is a has-a relationship and usually calls for composition, not inheritance.

### Polymorphism — one interface, multiple behaviours
Different concrete objects can answer the same virtual-function call differently. A Circle and Rectangle can both provide area(), but calculate it with different formulas. Templates and overloads also provide compile-time forms of polymorphism.

## 4. Procedural programming and OOP

| Procedural style | OOP style |
|---|---|
| Primary unit is often a function | Primary unit is often a type/object |
| State may be passed among procedures | State can be protected behind operations |
| Reuse with functions/modules | Reuse with composition, templates and sometimes inheritance |
| Natural for many data transformations | Natural when entities have state, rules and behaviour |

C++ supports both. Neither style is always faster or better. Choose the least complicated design that communicates the problem clearly.

## 5. A first complete example

We want deposits and withdrawals to be valid: a deposit must be positive, and a withdrawal cannot exceed the available balance.

```cpp
#include <iostream>
#include <string>
#include <utility>

class BankAccount {
private:
    std::string owner;
    int balance; // Use integer minor units in a real money system.

public:
    BankAccount(std::string name, int openingBalance)
        : owner(std::move(name)),
          balance(openingBalance >= 0 ? openingBalance : 0) {}

    void deposit(int amount) {
        if (amount > 0) {
            balance += amount;
        }
    }

    bool withdraw(int amount) {
        if (amount <= 0 || amount > balance) {
            return false;
        }
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
    const bool paid = account.withdraw(100);

    std::cout << account.getOwner() << "\n";
    std::cout << "Withdrawal successful: " << paid << "\n";
    std::cout << "Balance: " << account.getBalance() << "\n";
}
```

**Output**
```text
Asha
Withdrawal successful: 1
Balance: 1150
```

### Trace the example
1. The constructor creates an account with balance 1000.
2. deposit(250) changes the balance to 1250.
3. withdraw(100) passes both validations and changes it to 1150.
4. A direct statement such as account.balance = -900 would fail to compile because balance is private.
5. The public operations provide controlled ways to work with the data.

In a larger financial program, monetary values need a deliberate precision and overflow policy; this example focuses on OOP, not production banking.

## 6. Advantages and limitations

**Advantages:** related data and operations live together; invariants are easier to protect; interfaces can reduce coupling; composition and polymorphism can make extensions manageable.

**Limitations:** unnecessary classes make simple code verbose; deep hierarchies can be hard to reason about; too many layers hide control flow; virtual dispatch and dynamic allocation introduce trade-offs. OOP does not automatically make software reusable or secure.

## 7. Practical challenge — College Result Manager (intermediate)

### Problem statement
Build a small Result Manager for one student. It must:
- store a student's name and marks in three subjects;
- reject marks outside 0–100;
- calculate total, percentage and a letter grade;
- keep marks private;
- print a result card through a public method.

For this exercise, percentage is the average of the three subjects. Grade rules: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F. Invalid data must not be accepted.

### Worked solution
```cpp
#include <array>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class StudentResult {
private:
    std::string name;
    std::array<int, 3> marks;

public:
    StudentResult(std::string studentName, std::array<int, 3> subjectMarks)
        : name(std::move(studentName)), marks(subjectMarks) {
        for (int mark : marks) {
            if (mark < 0 || mark > 100) {
                throw std::invalid_argument("Marks must be between 0 and 100.");
            }
        }
    }

    int total() const {
        return marks[0] + marks[1] + marks[2];
    }

    double percentage() const {
        return total() / 3.0;
    }

    char grade() const {
        const double p = percentage();
        if (p >= 90) return 'A';
        if (p >= 80) return 'B';
        if (p >= 70) return 'C';
        if (p >= 60) return 'D';
        return 'F';
    }

    void printCard() const {
        std::cout << "Result: " << name << "\n"
                  << "Total: " << total() << "/300\n"
                  << std::fixed << std::setprecision(2)
                  << "Percentage: " << percentage() << "%\n"
                  << "Grade: " << grade() << "\n";
    }
};

int main() {
    try {
        StudentResult result("Riya", {91, 84, 95});
        result.printCard();
    } catch (const std::invalid_argument& ex) {
        std::cerr << ex.what() << "\n";
    }
}
```

**Output**
```text
Result: Riya
Total: 270/300
Percentage: 90.00%
Grade: A
```

### What this teaches
- The class groups related data and calculations.
- The marks array is private; callers cannot bypass validation.
- The constructor establishes the invariant once when the object is created.
- const member functions promise not to modify the result object.
- The exception makes invalid construction explicit to the caller.

**Try next:** add a fourth subject, display individual marks, and test the boundary values 0, 60, 89 and 100.

## 8. End-of-unit interview and revision questions

**Q1. What is OOP?**  
A programming approach that models a system using objects combining state and behaviour. The design benefit comes from clear boundaries and contracts, not merely using classes.

**Q2. Is C++ a pure object-oriented language?**  
No. C++ supports procedural programming, generic programming, object-oriented techniques and other styles.

**Q3. What is the difference between a class and an object?**  
A class defines a type; an object is an instance with a lifetime and state.

**Q4. Explain the four pillars with one-line examples.**  
Encapsulation protects an account balance; abstraction exposes deposit(); inheritance models a valid derived type such as Dog from Animal; polymorphism lets different Shape objects implement area() differently.

**Q5. Encapsulation vs abstraction?**  
Encapsulation groups state/operations and controls access. Abstraction presents the essential interface while hiding implementation details. They work together but are not synonyms.

**Q6. What is an invariant? Why does it matter?**  
A property that must always hold for a valid object. A non-negative bank balance is an example. Constructors and public operations should preserve the invariant.

**Q7. Does OOP always make a program better?**  
No. For short transformations or data-oriented tasks, free functions and simple structures may be clearer. Design for the actual problem.

**Q8. What is composition, and how is it different from inheritance?**  
Composition expresses has-a/uses-a by storing or collaborating with another object. Inheritance expresses a type relationship and can expose a substitutable base interface.

**Q9. Why is the Result Manager a class?**  
Its data and calculations belong together, and the class must validate marks so callers cannot construct an invalid result.

**Q10. What should be said when asked to explain an OOP project?**  
Explain the problem, the classes and responsibilities, the invariant each class protects, how objects collaborate, and the alternatives considered. Avoid listing buzzwords without showing how the design uses them.
