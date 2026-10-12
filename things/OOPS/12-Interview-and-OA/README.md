# Unit 12 — OOP Interview, Viva and OA Practice

This chapter is a revision bank for campus placements and technical screening. Questions are representative practice, **not verified company-specific past questions** unless a source and date are recorded. Interview content varies by job role and year.

## 1. High-frequency questions and concise answers

### Fundamentals
**1. What are the four pillars of OOP?**  
Encapsulation, abstraction, inheritance and polymorphism.

**2. Is C++ a pure OOP language?**  
No. C++ is multi-paradigm and supports procedural and generic programming too.

**3. Class vs object?**  
A class defines a type; an object is an instance with its own lifetime/state.

**4. Encapsulation vs abstraction?**  
Encapsulation groups state and operations and controls access. Abstraction presents the useful interface and hides details.

### Classes and object lifetime
**5. What is this?**  
A pointer available in non-static member functions referring to the object associated with that call.

**6. class vs struct?**  
Same capabilities; class defaults to private access/inheritance and struct defaults to public.

**7. Copy constructor vs copy assignment?**  
Copy construction creates a new object from another; copy assignment updates an existing object.

**8. What is a move constructor?**  
A constructor that may transfer resources from an expiring object. std::move enables overload selection; it does not perform the move itself.

**9. Rule of zero?**  
Prefer resource-managing members so the class does not need custom destructor/copy/move operations.

### Inheritance and polymorphism
**10. Overloading vs overriding?**  
Overloading uses a common name with distinguishable parameter lists. Overriding supplies a matching implementation of inherited virtual behaviour.

**11. What is a pure virtual function?**  
A virtual function declared with = 0. If the final overrider remains pure, the class is abstract.

**12. Why virtual destructor?**  
It enables correct destruction when a derived object is deleted through a base pointer.

**13. Diamond problem?**  
A common base is inherited along multiple paths. Virtual inheritance can make the shared base a single virtual base subobject.

**14. Virtual inheritance vs virtual function?**  
Virtual inheritance concerns base-subobject sharing; virtual functions concern runtime dispatch.

**15. What is slicing?**  
Copying a derived object into a base object by value removes the derived portion.

### Memory and errors
**16. What is RAII?**  
Tie resource ownership to object lifetime; cleanup happens automatically when the owner is destroyed.

**17. unique_ptr vs shared_ptr?**  
Exclusive ownership vs shared lifetime through reference counting.

**18. What is stack unwinding?**  
Destruction of fully constructed automatic objects as an exception propagates out of scopes.

**19. Why catch exceptions by const reference?**  
Avoid copying and preserve dynamic exception type.

**20. Can return type alone overload a function?**  
No; overload resolution uses the parameter list and other language rules, not the return type alone.

## 2. Output-tracing practice

### Question A — runtime dispatch
```cpp
#include <iostream>
struct Base {
    virtual void show() const { std::cout << "Base"; }
    virtual ~Base() = default;
};
struct Derived : Base {
    void show() const override { std::cout << "Derived"; }
};
int main() { Derived d; Base& ref = d; ref.show(); }
```
**Answer:** `Derived`. The call is virtual, and the dynamic object is Derived.

### Question B — non-virtual method
```cpp
#include <iostream>
struct Base { void show() const { std::cout << "Base"; } };
struct Derived : Base { void show() const { std::cout << "Derived"; } };
int main() { Derived d; Base* p = &d; p->show(); }
```
**Answer:** `Base`. The function is not virtual, so the call resolves using the static type Base.

### Question C — member construction and destruction
```cpp
#include <iostream>
struct A { A(){std::cout<<"A+";} ~A(){std::cout<<"A-";} };
struct B { B(){std::cout<<"B+";} ~B(){std::cout<<"B-";} };
struct C { A a; B b; C(){std::cout<<"C+";} ~C(){std::cout<<"C-";} };
int main(){ C c; }
```
**Answer:** `A+B+C+C-B-A-`. Members construct in declaration order and are destroyed in reverse order around the class destructor body.

### Question D — virtual destructor
```cpp
#include <iostream>
struct Base { virtual ~Base(){std::cout<<"B";} };
struct Derived : Base { ~Derived() override {std::cout<<"D";} };
int main(){ Base* p = new Derived; delete p; }
```
**Answer:** `DB`. The base destructor is virtual, so deleting through the pointer runs the derived destructor first. Production code should normally use a smart pointer instead of manual new/delete.

## 3. OA-style MCQs

**1. Which enables runtime dispatch through a base pointer?**  
A. Friend function  B. Virtual function  C. Static function  D. Constructor  
**Answer: B.** The virtual call selects the final overrider for the dynamic object type.

**2. Which is the default inheritance mode for class D : Base?**  
A. Public  B. Protected  C. Private  D. Virtual  
**Answer: C.** struct uses public inheritance by default.

**3. Which operator cannot be overloaded?**  
A. +  B. []  C. ::  D. <<  
**Answer: C.** The scope-resolution operator cannot be overloaded.

**4. Which smart pointer represents exclusive ownership?**  
A. shared_ptr  B. weak_ptr  C. unique_ptr  D. Raw pointer  
**Answer: C.**

**5. Can functions overload on return type alone?**  
A. Yes  B. No  C. Only virtual functions  D. Only templates  
**Answer: B.**

**6. What does std::move do by itself?**  
A. Deletes object  B. Deep-copies object  C. Casts to an xvalue  D. Allocates memory  
**Answer: C.** A selected move operation performs the transfer.

**7. What usually makes a class abstract?**  
A. Static data  B. Unimplemented pure virtual final overrider  C. Private constructor only  D. Friend function  
**Answer: B.**

**8. What does a virtual destructor primarily protect?**  
A. Overload resolution  B. Deletion through base pointer  C. Constructor chaining  D. Template deduction  
**Answer: B.**

**9. What is the best ordinary way to avoid resource leaks on exceptions?**  
A. Manual cleanup after every line  B. RAII  C. Global pointer  D. catch(...) that ignores errors  
**Answer: B.**

**10. What is the main benefit of override?**  
A. Makes method static  B. Changes visibility  C. Compiler checks that an override exists  D. Disables virtual dispatch  
**Answer: C.**

## 4. Practical interview challenge — Parking Lot Fee Calculator (intermediate/tough)

### Problem statement
Design a parking fee system with a polymorphic PricingPolicy. HourlyPricing charges a fixed amount per started hour. MemberPricing applies a percentage discount. ParkingTicket stores the vehicle plate and duration in minutes, rejects negative duration, and asks an injected policy to compute a fee. Demonstrate both pricing strategies without modifying ParkingTicket.

### Worked solution
```cpp
#include <iostream>
#include <memory>
#include <stdexcept>
#include <string>
#include <utility>

class PricingPolicy {
public:
    virtual int calculate(int minutes) const = 0;
    virtual ~PricingPolicy() = default;
};

class HourlyPricing : public PricingPolicy {
    int rate;
public:
    explicit HourlyPricing(int hourlyRate) : rate(hourlyRate) {
        if (rate < 0) throw std::invalid_argument("Rate cannot be negative");
    }
    int calculate(int minutes) const override {
        if (minutes < 0) throw std::invalid_argument("Duration cannot be negative");
        const int hours = (minutes + 59) / 60; // each started hour is charged
        return hours * rate;
    }
};

class MemberPricing : public PricingPolicy {
    int rate;
    int discountPercent;
public:
    MemberPricing(int hourlyRate, int discount)
        : rate(hourlyRate), discountPercent(discount) {
        if (rate < 0 || discount < 0 || discount > 100)
            throw std::invalid_argument("Invalid pricing configuration");
    }
    int calculate(int minutes) const override {
        if (minutes < 0) throw std::invalid_argument("Duration cannot be negative");
        const int hours = (minutes + 59) / 60;
        const int base = hours * rate;
        return base - (base * discountPercent / 100);
    }
};

class ParkingTicket {
    std::string plate;
    int minutes;
    const PricingPolicy& policy;
public:
    ParkingTicket(std::string p, int m, const PricingPolicy& pricing)
        : plate(std::move(p)), minutes(m), policy(pricing) {
        if (m < 0) throw std::invalid_argument("Duration cannot be negative");
    }
    void print() const {
        std::cout << plate << " fee: " << policy.calculate(minutes) << '\n';
    }
};

int main() {
    HourlyPricing regular(100);
    MemberPricing member(100, 20);
    ParkingTicket a("AS01AB1234", 70, regular);
    ParkingTicket b("AS01CD5678", 70, member);
    a.print();
    b.print();
}
```

**Output**
```text
AS01AB1234 fee: 200
AS01CD5678 fee: 160
```

### What makes this a good interview problem?
It combines encapsulation, constructor validation, abstraction, runtime polymorphism and dependency injection. The pricing policy is borrowed by reference, so it must outlive the ticket. A real application would also define integer overflow handling, maximum stay, timezone/time-recording concerns, and whether the free/partial hour rules are legally and commercially correct.

**Stretch task:** add WeekendPricing and prove that ParkingTicket needs no modification.

## 5. Questions to ask yourself during revision
- Can I describe each class's responsibility in one sentence?
- Which data invariant does it preserve?
- What happens for invalid input?
- Who owns each object/resource and how long does it live?
- Is inheritance truly substitutable or should I use composition?
- Can I predict the output before compiling?

## 6. Company-specific question evidence template
| Company/role | Date | Round | Question | Public source or personal notes |
|---|---|---|---|---|
| To be researched | — | OA/technical | — | Add a reliable source URL |

Do not claim a question was asked by a named company merely because it is common practice.
