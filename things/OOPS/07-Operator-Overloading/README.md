# Unit 07 — Operator Overloading

**Goal:** Give user-defined types natural syntax while keeping operator behaviour predictable.

## 1. What operator overloading means

C++ already defines operators such as +, ==, [] and << for built-in types. Operator overloading lets a class define an intuitive meaning for certain operators when operands are user-defined types. It does not let you create a new operator or change an operator's precedence, associativity or arity.

A good overload behaves like users would naturally expect. Addition of two Complex values should add their real and imaginary parts; using + to delete a file would be surprising and confusing.

## 2. Member function vs non-member function

A member operator uses the left operand as the object on which the member is called. A non-member operator can be useful when both operands should participate in conversions symmetrically. Stream output (std::cout << value) is usually implemented as a non-member because the left operand is an ostream, not your class.

## 3. Example: Complex number addition and output

```cpp
#include <iostream>

class Complex {
private:
    double real;
    double imag;

public:
    Complex(double r = 0, double i = 0) : real(r), imag(i) {}

    Complex operator+(const Complex& rhs) const {
        return Complex(real + rhs.real, imag + rhs.imag);
    }

    friend std::ostream& operator<<(std::ostream& os, const Complex& value) {
        os << value.real;
        if (value.imag >= 0) os << '+';
        os << value.imag << 'i';
        return os;
    }
};

int main() {
    const Complex a(2, 3);
    const Complex b(4, -1);
    std::cout << (a + b) << '\n';
}
```

**Output**
```text
6+2i
```

The + overload receives the right operand as rhs and returns a new result. The << overload returns the same stream by reference, so calls can be chained: std::cout << a << b.

## 4. Prefix and postfix increment

Prefix increment changes the object and generally returns a reference to it. Postfix increment returns the old value, so it needs a dummy int parameter to distinguish its signature.

```cpp
#include <iostream>

class Counter {
    int value;
public:
    explicit Counter(int v) : value(v) {}

    Counter& operator++() {        // prefix: ++x
        ++value;
        return *this;
    }

    Counter operator++(int) {      // postfix: x++
        Counter old(*this);
        ++value;
        return old;
    }

    int get() const { return value; }
};

int main() {
    Counter c(4);
    std::cout << (++c).get() << '\n';
    std::cout << (c++).get() << '\n';
    std::cout << c.get() << '\n';
}
```

**Output**
```text
5
5
6
```

## 5. Important restrictions

- At least one operand must be a user-defined or enumeration type.
- You cannot overload an operator for two built-in types such as int + int.
- You cannot invent a new operator token.
- You cannot change precedence, associativity or number of operands.
- Operators including ::, ., .*, ?: and sizeof cannot be overloaded.
- Some operators have special requirements; assignment, subscript, function-call and arrow operators need particular care.
- Prefer consistent semantics for ==, < and other comparisons.
- In C++20, defaulted comparison features exist; in C++17, implement the operations you need explicitly.

## 6. Practical challenge — Money type (intermediate)

### Problem statement
Implement a Money class that stores currency as integer cents, accepts a signed number of cents, supports addition and equality, and prints dollars with exactly two decimal places. For this exercise, allow negative values to represent a balance owed. The output operator must support chaining.

### Worked solution
```cpp
#include <iomanip>
#include <iostream>
#include <cstdlib>

class Money {
private:
    long long cents;
public:
    explicit Money(long long amountInCents) : cents(amountInCents) {}

    Money operator+(const Money& rhs) const {
        return Money(cents + rhs.cents);
    }

    bool operator==(const Money& rhs) const {
        return cents == rhs.cents;
    }

    friend std::ostream& operator<<(std::ostream& os, const Money& m) {
        const long long whole = m.cents / 100;
        const long long fraction = std::llabs(m.cents % 100);
        return os << (m.cents < 0 && whole == 0 ? "-$" : (m.cents < 0 ? "-$" : "$"))
                  << std::llabs(whole) << '.'
                  << std::setw(2) << std::setfill('0') << fraction
                  << std::setfill(' ');
    }
};

int main() {
    const Money lunch(1299);
    const Money coffee(325);
    const Money total = lunch + coffee;
    std::cout << "Lunch: " << lunch << "\n";
    std::cout << "Coffee: " << coffee << "\n";
    std::cout << "Total: " << total << "\n";
    std::cout << std::boolalpha << (total == Money(1624)) << '\n';
}
```

**Output**
```text
Lunch: $12.99
Coffee: $3.25
Total: $16.24
true
```

### Why this is better than storing floating-point money
Integer cents avoid binary floating-point representation surprises for the chosen precision. A production Money type would also need overflow policy, currency identity, rounding rules, and clearer formatting for negative amounts. The equality operator compares the underlying representation.

**Stretch task:** overload += and compare it with returning a new object from +. Which operations should modify the left operand, and which should create a new value?

## 7. End-of-unit interview questions with answers

**Q1. What is operator overloading?**  
Defining a suitable behaviour for an existing operator when used with a user-defined type.

**Q2. Can we overload + for two integers?**  
No. Both operands are built-in types, and the language does not permit that overload.

**Q3. Can operator precedence be changed?**  
No. Overloading changes the operation's meaning for user-defined operands, not the grammar or precedence.

**Q4. Why is operator<< often a non-member?**  
The left operand is an output stream, so a member of the custom class would have the wrong left-operand type. A friend non-member can access private state when needed.

**Q5. Why return ostream&?**  
To return the same stream and permit chaining.

**Q6. How do prefix and postfix increment differ?**  
Prefix has no dummy parameter and returns the updated value/reference. Postfix takes a dummy int and returns the previous value.

**Q7. Should every operator be overloaded?**  
No. Overload only when the meaning is intuitive and improves readability.

**Q8. What restrictions apply?**  
You cannot create operator tokens, change precedence/arity, or overload every operator. At least one operand must be user-defined or an enumeration.

**Q9. Member or non-member overload?**  
Use a member when the left operand is naturally the object. Non-members are useful for symmetric conversions and operators such as stream insertion.

**Q10. Why store Money in cents?**  
It represents the chosen fixed precision exactly for ordinary values, unlike binary floating point. Overflow and currency rules still need deliberate handling.
