# Unit 06 — Polymorphism

**Goal:** Know compile-time and runtime polymorphism, how virtual dispatch works, and how to avoid subtle errors.

## 1. Meaning

Polymorphism means “many forms”: the same operation name or interface can work with different types. In C++, distinguish compile-time selection (such as overload resolution and templates) from runtime selection through virtual functions.

## 2. Function overloading — compile-time

Functions may share a name if their parameter lists differ in a way overload resolution can distinguish.

```cpp
#include <iostream>
void print(int x) { std::cout << "int: " << x << '\n'; }
void print(double x) { std::cout << "double: " << x << '\n'; }
void print(const char* x) { std::cout << "text: " << x << '\n'; }

int main() {
    print(7);
    print(2.5);
    print("hello");
}
```

**Output**
```text
int: 7
double: 2.5
text: hello
```

Return type alone cannot distinguish overloaded functions because a call such as f(3) would not give overload resolution a parameter-based way to choose. Be careful with conversions: ambiguous or equally good conversions can make a call ill-formed.

## 3. Overriding — runtime polymorphism

A virtual function permits a matching derived implementation to become the final overrider. A call through a base pointer/reference then selects behaviour using the actual dynamic object type.

```cpp
#include <iostream>
#include <memory>
#include <vector>

class Shape {
public:
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    double radius;
public:
    explicit Circle(double r) : radius(r) {}
    double area() const override { return 3.141592653589793 * radius * radius; }
};

class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const override { return width * height; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(2));
    shapes.push_back(std::make_unique<Rectangle>(3, 4));
    for (const auto& shape : shapes)
        std::cout << shape->area() << '\n';
}
```

**Output**
```text
12.5664
12
```

The collection contains different concrete types behind one Shape interface. The virtual destructor matters because each object is owned/deleted through a base-type pointer.

## 4. Pure virtual functions and abstract classes

A declaration such as virtual double area() const = 0; is a pure virtual function. A class with a pure virtual function whose final overrider is still pure is abstract and cannot be instantiated directly. An abstract class may still have data members, constructors, regular member functions and a destructor.

The abstract class defines a contract. Each concrete derived class must implement the required operations before it can be instantiated.

## 5. Overloading vs overriding vs hiding

| Term | What happens | Binding |
|---|---|---|
| Overloading | Same function name, different parameter list | Compile-time overload resolution |
| Overriding | Derived class implements an inherited virtual function | Runtime dispatch through virtual calls |
| Hiding | Derived declaration hides base names/overloads in lookup | Name lookup; not itself runtime polymorphism |

Always mark intended overrides with override. The compiler will catch errors such as a missing const qualifier or wrong parameter type.

## 6. A classic trap: virtual vs non-virtual

```cpp
#include <iostream>
struct Base {
    virtual void virtualCall() const { std::cout << "Base virtual\n"; }
    void ordinaryCall() const { std::cout << "Base ordinary\n"; }
    virtual ~Base() = default;
};
struct Derived : Base {
    void virtualCall() const override { std::cout << "Derived virtual\n"; }
    void ordinaryCall() const { std::cout << "Derived ordinary\n"; }
};
int main() {
    Derived d;
    Base& b = d;
    b.virtualCall();
    b.ordinaryCall();
}
```

**Output**
```text
Derived virtual
Base ordinary
```

The first call is virtual and uses the dynamic type. The second is non-virtual and resolves according to the static type Base.

Other traps:
- Constructors cannot be virtual; static functions cannot be virtual.
- Function templates themselves cannot be virtual.
- Default arguments are chosen using static type even when the function is virtual.
- Virtual calls inside base constructors/destructors do not invoke overrides in a derived part that is not yet constructed or has already been destroyed.
- Object slicing can remove derived state when passing by value.

## 7. What about vtables?

Compilers commonly implement virtual dispatch with a vtable and a pointer in the object (often called a vptr). That is a common implementation technique, not a precise memory layout guaranteed by the C++ standard. In interviews, explain the language behaviour first; describe vtables as a common implementation detail.

## 8. Practical challenge — Notification Router (intermediate/tough)

### Problem statement
Create a base Notification interface with virtual send(message). Implement EmailNotification and SMSNotification. Write a NotificationService that holds multiple notifications and sends the same message to each. Use smart pointers, a virtual destructor and override. Do not use if/else checks for the concrete type inside the service.

### Worked solution
```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Notification {
public:
    virtual void send(const std::string& message) const = 0;
    virtual ~Notification() = default;
};

class EmailNotification : public Notification {
    std::string address;
public:
    explicit EmailNotification(std::string a) : address(std::move(a)) {}
    void send(const std::string& message) const override {
        std::cout << "Email to " << address << ": " << message << '\n';
    }
};

class SMSNotification : public Notification {
    std::string number;
public:
    explicit SMSNotification(std::string n) : number(std::move(n)) {}
    void send(const std::string& message) const override {
        std::cout << "SMS to " << number << ": " << message << '\n';
    }
};

class NotificationService {
    std::vector<std::unique_ptr<Notification>> channels;
public:
    void add(std::unique_ptr<Notification> n) {
        channels.push_back(std::move(n));
    }
    void broadcast(const std::string& message) const {
        for (const auto& channel : channels) channel->send(message);
    }
};

int main() {
    NotificationService service;
    service.add(std::make_unique<EmailNotification>("user@example.com"));
    service.add(std::make_unique<SMSNotification>("555-0101"));
    service.broadcast("Exam results are available");
}
```

**Output**
```text
Email to user@example.com: Exam results are available
SMS to 555-0101: Exam results are available
```

### Why it works
NotificationService programs against the abstract Notification contract. Adding PushNotification requires creating another implementation, not changing the broadcast loop. unique_ptr makes ownership explicit, and the base destructor allows safe destruction through the interface.

**Stretch task:** add a MockNotification for tests that counts how many times send() was called. Why is this easier when code depends on an interface?

## 9. End-of-unit interview questions with answers

**Q1. What is polymorphism?**  
A common interface or operation can represent different behaviours/types.

**Q2. Compile-time vs runtime polymorphism?**  
Overloading and templates are resolved primarily during compilation. Virtual function calls through base pointers/references select the final overrider using dynamic type at runtime.

**Q3. Overloading vs overriding?**  
Overloading changes the parameter list; overriding supplies a matching derived implementation of an inherited virtual function.

**Q4. What is an abstract class?**  
A class whose required pure virtual behaviour is not fully implemented. It cannot be instantiated directly.

**Q5. Why use override?**  
To tell the compiler the function is meant to override a virtual function and catch mismatched signatures.

**Q6. Why a virtual destructor?**  
When a derived object may be destroyed through a base pointer, virtual destruction invokes the correct derived-to-base destructor chain.

**Q7. Are vtables required by the C++ standard?**  
No. They are a common compiler implementation; the language defines virtual dispatch behaviour, not one required memory layout.

**Q8. Can static functions be virtual?**  
No, because static member functions are not tied to a particular object.

**Q9. What is object slicing?**  
Copying a derived object into a base object by value loses the derived part. Use references/pointers for polymorphic behaviour.

**Q10. Why should the service store interface pointers?**  
It can handle multiple concrete implementations uniformly and own them safely without type-specific branching.
