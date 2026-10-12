# Lesson 10.1 — this, static, const and friend

## this: which object is being used?

If you call first.setValue(10), the function needs to know which object's value should change. In a non-static member function, this points to the object used for the call.

```cpp
#include <iostream>

class Counter {
    int value;
public:
    explicit Counter(int start) : value(start) {}

    void setValue(int value) {
        this->value = value;
    }

    int getValue() const { return value; }
};

int main() {
    Counter first(1);
    Counter second(2);
    first.setValue(10);
    std::cout << first.getValue() << '\n';
    std::cout << second.getValue() << '\n';
}
```

**Output**
```text
10
2
```

Inside setValue, the parameter is named value too. this->value explicitly means the member belonging to the current object; plain value means the parameter. The arrow operator accesses a member through a pointer. this is not available in a static member function.

## static data members: one shared value

Ordinary data members belong to individual objects. A static data member belongs to the class and has one shared value for the class, not a separate copy in each object.

```cpp
#include <iostream>

class Ticket {
    inline static int nextId = 1; // C++17
    int id;
public:
    Ticket() : id(nextId++) {}
    int getId() const { return id; }
    static int nextTicketId() { return nextId; }
};

int main() {
    Ticket a;
    Ticket b;
    std::cout << a.getId() << ' ' << b.getId() << '\n';
    std::cout << Ticket::nextTicketId() << '\n';
}
```

**Output**
```text
1 2
3
```

inline static lets the member be defined inside the class in C++17. The static function can be called with the class name because it doesn't need a particular object. Older C++ standards have a different out-of-class definition requirement; this course targets C++17.

## const member functions: promise not to change state

A function that only reads an object should usually be const. The compiler can then prevent ordinary modifications to non-mutable data members through that function.

```cpp
class Temperature {
    double celsius;
public:
    explicit Temperature(double c) : celsius(c) {}
    double value() const { return celsius; }
};
```

For example, an object declared const can call value() but generally cannot call a non-const setter. const is part of the member function's signature rules and helps document intent.

## friend: special permission

A friend function is not a member, but a class gives it permission to access its private/protected members. Friendship is not inherited, not reciprocal automatically and not transitive. Use it only when a non-member operation naturally needs access, such as output formatting.

```cpp
#include <iostream>
class SecretNumber {
    int value;
public:
    explicit SecretNumber(int v) : value(v) {}
    friend void reveal(const SecretNumber& s);
};

void reveal(const SecretNumber& s) {
    std::cout << s.value << '\n';
}

int main() {
    const SecretNumber secret(42);
    reveal(secret);
}
```

**Output**
```text
42
```

## Practical mini-task
Create a VisitCounter class:
- store a shared static total;
- increment total when a new object is constructed;
- provide a static function to read the total;
- provide a const member function for each object's ID.

Check: does the static counter count objects created or objects currently alive? Those are different questions. Counting live objects requires handling copying, moving and destruction carefully.

## Common mistakes
- Trying to use this from a static function.
- Assuming static fields have a separate value for each object.
- Omitting const on a function that should only observe.
- Treating friend as a member function.
- Making many helpers friends instead of designing a clear public interface.

## Interview questions
1. **What is this?** A pointer to the object associated with a non-static member-function call.
2. **Can a static function be virtual?** No; it has no associated object or this pointer.
3. **What is a static data member?** One class-level value shared by all instances.
4. **What does const after a member function mean?** The function does not modify ordinary non-mutable object state through that function.
5. **Is a friend function a member?** No; it is granted access but remains a non-member.
6. **Is friendship inherited?** No.
7. **Why use Ticket::nextTicketId()?** The static operation belongs to the class and does not need an instance.
8. **Why are const functions valuable?** They document and enforce read-only operations.

---
[← Unit 10 overview](README.md) · [Next lesson: Object Relationships →](02-object-relationships.md)
