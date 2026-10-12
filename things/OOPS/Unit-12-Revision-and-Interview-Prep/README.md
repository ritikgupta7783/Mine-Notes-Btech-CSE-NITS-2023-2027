# Unit 12 — Revision, Debugging and Interview Preparation

**Prerequisite:** Complete Units 0–11 or read this as a checklist while revising.
**Goal:** Explain concepts simply, predict outputs, diagnose mistakes, and solve small OOP design problems.

> The questions here are representative C++ interview/OA practice. They are not claimed to be exact questions from a specific company unless a date and reliable source are recorded.

## 1. A good interview answer pattern

Use four steps:
1. **Definition:** say what the concept means in one sentence.
2. **Reason:** explain why it exists or what problem it solves.
3. **Example:** use a small code or real-life situation.
4. **Caveat:** mention one common trap or limitation.

For example, for encapsulation: “Encapsulation keeps data and the operations that work on it together and controls access. It helps preserve rules such as a non-negative account balance. A BankAccount can keep balance private and expose deposit and withdraw. A blind setter would weaken the rule.”

## 2. Core questions with answers

### Foundations and classes
**Q1. What are the four pillars of OOP?**  
Encapsulation, abstraction, inheritance and polymorphism. These are design ideas; not every program needs all four equally.

**Q2. Is C++ purely object-oriented?**  
No. C++ is multi-paradigm: it also supports procedural and generic programming, among other styles.

**Q3. Class vs object?**  
A class defines a type and its members; an object is an instance with a lifetime and its own non-static state.

**Q4. What is a member function?**  
A function declared as part of a class. It can normally access the object's eligible private/protected members.

**Q5. class vs struct?**  
Same basic capabilities; class defaults to private member/base access while struct defaults to public.

### Access, constructors and lifetime
**Q6. public vs private vs protected?**  
Public is accessible to ordinary callers, private is accessible directly to the class/friends, and protected is mainly for the class and eligible derived contexts.

**Q7. What is a constructor?**  
A special member function that initializes a newly created object. It has the class name and no return type.

**Q8. Copy constructor vs copy assignment?**  
The copy constructor creates a new object from another; copy assignment updates an already-existing object.

**Q9. Why use a member initializer list?**  
It initializes bases/members directly and is required for references, const members and members without suitable default constructors.

**Q10. What does this mean?**  
In a non-static member function, this refers to the object associated with the current call.

**Q11. What is a destructor?**  
A special member function called as an object's lifetime ends; it usually releases resources that object owns.

**Q12. Rule of three/five/zero?**  
Three concerns destructor, copy constructor and copy assignment; five adds move constructor and move assignment. Rule of zero prefers member types that manage resources so the class needs no custom operations.

### Encapsulation and abstraction
**Q13. What is an invariant?**  
A rule that must remain true for every valid object, such as wallet balance ≥ 0.

**Q14. Encapsulation vs abstraction?**  
Encapsulation groups and controls state/behaviour. Abstraction gives callers the essential operations and hides irrelevant detail.

**Q15. Is private data encrypted?**  
No. It is compile-time access control, not a security or encryption mechanism.

### Inheritance and polymorphism
**Q16. What is inheritance?**  
A way to derive a class from one or more base classes. It is most suitable when the derived type can honour the base contract.

**Q17. Overloading vs overriding?**  
Overloading uses the same function name with distinguishable parameter lists. Overriding provides a matching implementation of an inherited virtual function.

**Q18. Why use override?**  
It tells the compiler to verify that a derived function actually overrides a base virtual function.

**Q19. What is a pure virtual function?**  
A virtual function declared with = 0. A class remains abstract while a pure virtual final overrider is not implemented.

**Q20. Why a virtual destructor?**  
If a derived object can be deleted through a base pointer, virtual destruction ensures the derived-to-base destructor chain is invoked.

**Q21. What is object slicing?**  
Copying a derived object into a base object by value discards the derived-specific portion.

**Q22. Virtual inheritance vs virtual function?**  
Virtual inheritance shares a common base subobject in a diamond hierarchy; virtual functions enable runtime method dispatch.

### Memory and other concepts
**Q23. What is RAII?**  
Tie resource ownership to object lifetime so destruction performs cleanup automatically.

**Q24. unique_ptr vs shared_ptr?**  
unique_ptr expresses exclusive ownership. shared_ptr expresses shared lifetime and has reference-counting overhead/complexity.

**Q25. What does std::move do?**  
It casts an expression to an xvalue so move overloads may be selected. It does not itself move the resource.

**Q26. What is stack unwinding?**  
The destruction of fully constructed automatic objects as an exception leaves scopes.

**Q27. Why catch by const reference?**  
It avoids an unnecessary copy and preserves the dynamic exception type.

**Q28. What is a template?**  
A compile-time recipe for generating generic functions or classes for types that support the required operations.

**Q29. What is a namespace?**  
A named scope that organizes identifiers and helps prevent name conflicts.

**Q30. What is dependency injection?**  
Giving an object the dependency it needs from outside, rather than making it construct a particular implementation itself.

## 3. Output-prediction practice

### Question A
```cpp
#include <iostream>
class Counter {
public:
    int value = 0;
    void inc() { ++value; }
};
int main() {
    Counter a, b;
    a.inc();
    a.inc();
    b.inc();
    std::cout << a.value << ' ' << b.value << '\n';
}
```
**Answer:** `2 1`. The non-static value member belongs to each object separately.

### Question B
```cpp
#include <iostream>
struct Base {
    virtual void show() const { std::cout << "Base"; }
    virtual ~Base() = default;
};
struct Derived : Base {
    void show() const override { std::cout << "Derived"; }
};
int main() {
    Derived d;
    Base& b = d;
    b.show();
}
```
**Answer:** `Derived`. The call is virtual and the dynamic object is Derived.

### Question C
```cpp
#include <iostream>
struct Base { void show() const { std::cout << "Base"; } };
struct Derived : Base { void show() const { std::cout << "Derived"; } };
int main() {
    Derived d;
    Base* p = &d;
    p->show();
}
```
**Answer:** `Base`. show() is not virtual, so the call is resolved using the static type Base.

### Question D
```cpp
#include <iostream>
struct A { A(){std::cout<<"A+";} ~A(){std::cout<<"A-";} };
struct B { B(){std::cout<<"B+";} ~B(){std::cout<<"B-";} };
struct C { A first; B second; C(){std::cout<<"C+";} ~C(){std::cout<<"C-";} };
int main(){ C c; }
```
**Answer:** `A+B+C+C-B-A-`. Members are constructed in declaration order and destroyed in reverse order.

## 4. Debugging drills

Try to fix each before reading the explanation.

### Drill 1 — inaccessible member
```cpp
class Account {
private:
    int balance = 100;
};
int main() {
    Account a;
    // std::cout << a.balance;
}
```
**Issue:** uncommenting the print produces a compile-time access error. **Fix:** add a public getter such as int getBalance() const { return balance; }.

### Drill 2 — wrong override signature
```cpp
struct Base {
    virtual void run() const {}
};
struct Child : Base {
    // void run() override {} // does not override because const differs
};
```
**Fix:** write void run() const override {}. The const qualifier is part of the member-function signature relevant to overriding.

### Drill 3 — virtual deletion
```cpp
struct Base { ~Base() = default; };
struct Child : Base { ~Child() = default; };
// Deleting a Child through Base* is not supported safely with a non-virtual destructor.
```
**Fix:** use virtual ~Base() = default; when the interface supports deleting derived objects through Base pointers. Prefer a smart pointer with an appropriate base destructor in real code.

## 5. OA-style MCQs

**1. Which provides runtime dispatch through a base pointer?**  
A. static function  B. virtual function  C. friend function  D. constructor  
**Answer: B.**

**2. Which can distinguish an overload?**  
A. Return type alone  B. Parameter list  C. Comment  D. Variable name in main  
**Answer: B.**

**3. Which smart pointer represents exclusive ownership?**  
A. shared_ptr  B. weak_ptr  C. unique_ptr  D. raw pointer  
**Answer: C.**

**4. What does a pure virtual function normally make its class?**  
A. Abstract  B. Static  C. Namespace  D. Template  
**Answer: A.**

**5. What does std::move guarantee by itself?**  
A. Delete object  B. Deep copy  C. An xvalue cast  D. Allocate memory  
**Answer: C.**

**6. What helps prevent leaks during exceptions?**  
A. RAII  B. Ignoring errors  C. Global pointer  D. Raw new everywhere  
**Answer: A.**

**7. In class D : Base, what is the default inheritance mode?**  
A. public  B. protected  C. private  D. virtual  
**Answer: C.**

**8. What does override do?**  
A. Makes method static  B. Compiler checks intended override  C. Hides all base methods  D. Deletes the base  
**Answer: B.**

## 6. Coding challenges by level

**Beginner**
1. Write a Student class with private name and roll number.
2. Write a Rectangle class with area() and perimeter().
3. Add validation to a BankAccount withdraw() method.

**Intermediate**
4. Implement a Library containing Book values and borrow/return operations.
5. Create an abstract Shape and implement Circle and Rectangle.
6. Explain and fix object slicing.

**Challenging**
7. Design a PaymentMethod interface with Card and Wallet implementations.
8. Implement a resource-owning class, explain its copy/move policy, and then redesign it using vector or unique_ptr.
9. Create a generic Registry template using map.
10. Extend the payroll project without making one large class responsible for everything.

Hints: start by listing state and invariants. Then choose class responsibilities, public methods, ownership, and failure behaviour before writing code.

## 7. Final interview checklist
Before calling yourself interview-ready, verify that you can:
- define all four pillars and give a practical example for each;
- explain class vs object and public/private/protected;
- describe constructor, destructor, copy and move;
- compare overloading, overriding and hiding;
- explain virtual destructor, abstract class and object slicing;
- compare composition with inheritance;
- explain RAII and smart pointers;
- trace constructor/destructor order;
- spot compile-time access and override errors;
- solve one project using the topic without copying its code.

## Note on company-specific questions
Add company questions only with evidence, date and interview round. Candidate-reported experiences may be useful but are anecdotal. Do not claim a practice question was asked by a company without a source.

---
[← Previous: Unit 11 — Projects](../Unit-11-Practical-Projects/README.md) · [Course home](../README.md) · [Progress checklist](../PROGRESS-CHECKLIST.md)
