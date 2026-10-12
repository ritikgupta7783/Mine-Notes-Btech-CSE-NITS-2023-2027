# Unit 02 — Classes and Objects

**Goal:** Design a class, create objects, use access control correctly, and understand member functions, const, static and friend.

## 1. A class is a user-defined type

A class describes which data an object stores and which operations are allowed. The class declaration defines the type; writing a variable of that type creates an object.

```cpp
#include <iostream>
#include <string>

class Phone {
public:
    std::string brand;
    void ring() const {
        std::cout << brand << " is ringing!\n";
    }
};

int main() {
    Phone p;
    p.brand = "Nova";
    p.ring();
}
```

**Output**
```text
Nova is ringing!
```

This first example keeps brand public so the syntax is easy to see. A real class should consider whether arbitrary callers should be able to change it.

## 2. class vs struct

In C++, both define class types and both can have constructors, member functions, access control, inheritance and virtual functions. The defaults differ:

| Feature | class | struct |
|---|---|---|
| Default member access | private | public |
| Default inheritance access | private | public |
| Capabilities | Same | Same |

Common style: use struct for simple public data records and class when protecting an invariant. This is a convention, not a technical requirement.

## 3. Access specifiers

- **public:** callers can use the member subject to normal access rules.
- **private:** only the class's members and friends can directly access it.
- **protected:** class/friends and eligible derived-class contexts may access it.

Private does not mean encrypted or secure against every possible low-level inspection. It is compile-time access control that makes accidental misuse harder.

```cpp
#include <iostream>

class Exam {
private:
    int marks;
public:
    explicit Exam(int m) : marks(m) {}
    int getMarks() const { return marks; }
};

int main() {
    Exam e(88);
    std::cout << e.getMarks() << '\n';
    // e.marks = -1; // compilation error: marks is private
}
```

**Output**
```text
88
```

## 4. Creating objects and accessing members

```cpp
Phone p;       // automatic object
Phone* ptr = &p;
p.ring();      // dot operator
ptr->ring();   // arrow operator for a pointer
```

The arrow operator is shorthand for dereferencing a pointer and accessing a member. A pointer does not itself own an object unless an ownership design says it does.

### Object memory
Non-static data members are stored per object. Static data members are shared at class level. A class's object size can include padding for alignment and implementation details, so don't assume it always equals the sum of member sizes. Empty classes still have nonzero size as objects.

## 5. The this pointer

Within a non-static member function, this points to the object on which the function was called. It is useful when a parameter has the same name as a member or when returning the current object.

```cpp
#include <iostream>

class Counter {
private:
    int value;
public:
    explicit Counter(int value) : value(value) {}

    Counter& increment() {
        ++this->value;
        return *this;
    }

    int get() const { return value; }
};

int main() {
    Counter c(5);
    c.increment().increment();
    std::cout << c.get() << '\n';
}
```

**Output**
```text
7
```

The constructor's value parameter shadows the member name, so value(value) means initialize the member from the parameter. In increment(), *this refers to the current object. Returning a reference enables chaining.

A static member function has no this pointer because no particular object is implied by calling it.

## 6. const member functions

Mark observer functions const when they should not change the object's ordinary state.

```cpp
class Temperature {
    double celsius;
public:
    explicit Temperature(double t) : celsius(t) {}
    double getCelsius() const { return celsius; }
};
```

A const object generally cannot call a non-const member function. const correctness lets the compiler catch accidental modification and makes APIs easier to reason about. A mutable member is a deliberate exception for certain logically-constant implementation details such as caches.

## 7. Static members

A static data member belongs to the class rather than to each instance. A static member function can be called with the class name and cannot directly access non-static members without an object.

```cpp
#include <iostream>

class Session {
    inline static int created = 0; // C++17
public:
    Session() { ++created; }
    static int creationCount() { return created; }
};

int main() {
    Session a, b, c;
    std::cout << Session::creationCount() << '\n';
}
```

**Output**
```text
3
```

This counts constructor calls, not currently living objects. To count live objects, design and test the copy/move constructors and destructor too.

## 8. Friend functions

A friend function is not a member function, but it is granted access to private/protected members. Friendship is not automatically inherited, reciprocal or transitive. Use it where it creates a natural interface, for example stream insertion operators, rather than making everything a friend.

```cpp
#include <iostream>

class Box {
    int width;
public:
    explicit Box(int w) : width(w) {}
    friend void printWidth(const Box& b);
};

void printWidth(const Box& b) {
    std::cout << b.width << '\n';
}

int main() {
    const Box b(12);
    printWidth(b);
}
```

**Output**
```text
12
```

## 9. Practical challenge — Library Book Tracker (intermediate)

### Problem
Implement a Book type with a title, author, and availability status. Title and author must not be directly writable after construction. Provide:
- a constructor that rejects an empty title;
- borrowBook() that fails if the book is already borrowed;
- returnBook() that fails if it was not borrowed;
- const observer functions;
- a static counter for the number of Book objects constructed.

Show one successful borrow, one rejected borrow, a return and the count.

### Worked solution
```cpp
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>

class Book {
private:
    std::string title;
    std::string author;
    bool available = true;
    inline static int constructed = 0;

public:
    Book(std::string t, std::string a)
        : title(std::move(t)), author(std::move(a)) {
        if (title.empty()) throw std::invalid_argument("Title cannot be empty");
        ++constructed;
    }

    bool borrowBook() {
        if (!available) return false;
        available = false;
        return true;
    }

    bool returnBook() {
        if (available) return false;
        available = true;
        return true;
    }

    bool isAvailable() const { return available; }
    const std::string& getTitle() const { return title; }

    static int constructionCount() { return constructed; }
};

int main() {
    Book b("Clean Code", "Robert C. Martin");
    std::cout << b.borrowBook() << '\n';
    std::cout << b.borrowBook() << '\n';
    std::cout << b.returnBook() << '\n';
    std::cout << b.getTitle() << ": " << b.isAvailable() << '\n';
    std::cout << "Constructed: " << Book::constructionCount() << '\n';
}
```

**Output**
```text
1
0
1
Clean Code: 1
Constructed: 1
```

### Why this design works
The private availability flag protects the book's state. Each operation validates the current state before changing it. The static counter is shared across instances. In production, an empty title could be validated before construction or represented as a richer validation result; here the constructor throws to demonstrate a clear failure path.

**Stretch task:** count currently alive books, not constructed books. What happens when a Book is copied? Explain which constructors/destructor must update the count consistently.

## 10. End-of-unit interview questions with answers

**Q1. What is the difference between a class and an object?**  
A class defines a type and its member/access rules. An object is an instance with storage, state and lifetime.

**Q2. Why prefer private data with public operations?**  
It helps preserve invariants and keeps callers from depending directly on the representation. Public data is still acceptable for simple aggregate records.

**Q3. Can private members be accessed by a derived class?**  
Not directly. They exist as part of the base subobject, but derived code must use accessible base operations or friendship if appropriate.

**Q4. What is this?**  
A pointer available inside non-static member functions that refers to the current object.

**Q5. Can a static member function be virtual?**  
No. Virtual dispatch applies to a call associated with an object; static functions have no this pointer.

**Q6. What is a const member function?**  
A member function whose implicit object parameter is const-qualified; it cannot modify ordinary non-mutable members through this.

**Q7. class versus struct in C++?**  
They have the same capabilities. Default member and base access are private for class and public for struct.

**Q8. What is friendship?**  
Explicit permission for a non-member function or another class to access private/protected members. It should be used selectively.

**Q9. Why use an initializer list?**  
It initializes members directly and is necessary for references, const members and members without suitable default constructors.

**Q10. What is a static data member?**  
One class-level member shared by instances rather than a separate member in each object. It needs appropriate definition/initialization according to the C++ standard version.
