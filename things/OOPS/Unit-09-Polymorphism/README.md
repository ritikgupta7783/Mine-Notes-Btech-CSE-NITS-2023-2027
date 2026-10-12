# Unit 9 — Polymorphism

**Prerequisite:** Member functions, inheritance, base pointers/references and constructors.
**Estimated time:** 2–3 hours.

## 1. The problem: one request, different behaviour

A drawing program may need to ask every shape to calculate its area. A Circle uses pi × radius × radius; a Rectangle uses width × height. We want one common request, area(), without writing a long if/else chain that checks each type. Polymorphism makes this possible.

**Polymorphism** means one interface or operation can work with different types/behaviours. In C++, distinguish compile-time forms such as overloading from runtime dispatch through virtual functions.

## 2. Function overloading — compile-time selection

Overloaded functions share a name but have distinguishable parameter lists. C++ chooses a matching function using the arguments when compiling the call.

```cpp
#include <iostream>
void show(int value) { std::cout << "Integer: " << value << '\n'; }
void show(double value) { std::cout << "Decimal: " << value << '\n'; }
void show(const std::string& value) { std::cout << "Text: " << value << '\n'; }

int main() {
    show(4);
    show(3.5);
    show(std::string("hello"));
}
```

**Output**
```text
Integer: 4
Decimal: 3.5
Text: hello
```

Return type alone cannot distinguish overloads. The parameters must help the compiler choose. Overloads are selected at compile time; no virtual dispatch is needed.

## 3. Function overriding — runtime behaviour

Overriding occurs when a derived class implements a matching inherited virtual function. When called through a base reference or pointer, the runtime object type determines the final overrider.

```cpp
#include <iostream>
#include <memory>
#include <string>
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
    double area() const override {
        return 3.141592653589793 * radius * radius;
    }
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

### What is happening?
- Shape is an abstract base because area() is pure virtual.
- Circle and Rectangle provide different area() formulas.
- unique_ptr<Shape> owns each concrete object but exposes the common Shape interface.
- shape->area() calls through a pointer. The arrow operator accesses a member through a pointer.
- Because area() is virtual, the right derived implementation is selected.
- The virtual destructor makes deletion through Shape safe.

A compiler commonly implements virtual dispatch with a vtable and an internal pointer, but the C++ standard does not require a particular memory layout. In an interview, distinguish guaranteed behaviour from common implementation details.

## 4. Overloading vs overriding vs hiding

| Concept | Meaning | Chosen how? |
|---|---|---|
| Overloading | Same name, different parameter lists | Compile-time overload resolution |
| Overriding | Matching derived method replaces inherited virtual behaviour | Runtime dispatch through virtual call |
| Hiding | A derived declaration hides base names/overloads during name lookup | Name lookup; not itself runtime polymorphism |

Always write override when you intend to override. It helps catch mistakes such as missing const or changing a parameter type accidentally.

## 5. Pure virtual functions and abstract classes

The syntax virtual double area() const = 0; declares a pure virtual function. A class is abstract while it has a pure virtual final overrider that is not implemented. You cannot create a direct object of that abstract class, but you can use its pointer/reference type to refer to derived objects.

C++ has no separate interface keyword. Abstract classes are often used as interface-style contracts, but they may also contain data members, constructors and implemented functions.

## 6. Operator overloading preview

Operator overloading gives a suitable meaning to an existing operator for a user-defined type. For example, Complex values can use + to add their real and imaginary parts. Operators cannot be invented, and precedence and arity cannot be changed.

```cpp
#include <iostream>
class Complex {
    int real, imag;
public:
    Complex(int r, int i) : real(r), imag(i) {}
    Complex operator+(const Complex& rhs) const {
        return Complex(real + rhs.real, imag + rhs.imag);
    }
    void print() const {
        std::cout << real << (imag >= 0 ? "+" : "")
                  << imag << "i\n";
    }
};
int main() {
    Complex a(2, 3), b(4, -1);
    Complex c = a + b;
    c.print();
}
```

**Output**
```text
6+2i
```

Here operator+ is a member function. a + b is translated conceptually into a call on a with b as the right-hand argument. This is a first preview; later notes and examples can go deeper into operator overload rules.

## 7. Common mistakes
- Calling a method through a base pointer and expecting dynamic behaviour when it is not virtual.
- Changing a signature and assuming it still overrides.
- Forgetting a virtual destructor for a polymorphic base that supports base-pointer deletion.
- Expecting an abstract class to be instantiated directly.
- Passing a derived object by value into a base variable, causing slicing.
- Assuming vtable/vptr layout is mandated by the standard.
- Believing overloading and overriding are the same concept.

## 8. Practical challenge — Shape Report (intermediate/tough)

### Problem statement
Create an abstract Shape with name() and area(). Implement Circle and Rectangle. Store both in one collection of smart pointers to Shape and print each shape's name and area. Do not use type-checking if/else branches in the print loop.

### Solution
```cpp
#include <iomanip>
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Shape {
public:
    virtual std::string name() const = 0;
    virtual double area() const = 0;
    virtual ~Shape() = default;
};

class Circle : public Shape {
    double radius;
public:
    explicit Circle(double r) : radius(r) {}
    std::string name() const override { return "Circle"; }
    double area() const override { return 3.141592653589793 * radius * radius; }
};

class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    std::string name() const override { return "Rectangle"; }
    double area() const override { return width * height; }
};

int main() {
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(2));
    shapes.push_back(std::make_unique<Rectangle>(3, 4));

    std::cout << std::fixed << std::setprecision(2);
    for (const auto& shape : shapes) {
        std::cout << shape->name() << ": " << shape->area() << '\n';
    }
}
```

**Output**
```text
Circle: 12.57
Rectangle: 12.00
```

### Explanation
The loop calls the same methods on the same base interface. The object determines the implementation. The derived types can be extended without adding a type-specific branch to the loop. The virtual destructor gives correct destruction when each object is owned through unique_ptr<Shape>.

**Stretch task:** implement Triangle with an appropriate area formula. Add it to the vector; no change should be needed in the reporting loop.

## 9. End-of-unit interview questions with answers

**Q1. Define polymorphism.**  
The ability to use a common interface or operation with different types/behaviours.

**Q2. Compile-time vs runtime polymorphism?**  
Overloading and templates are resolved primarily at compile time. Virtual calls through base pointers/references choose a final overrider using the dynamic type.

**Q3. Overloading vs overriding?**  
Overloading uses different parameter lists; overriding implements an inherited virtual function in a derived class.

**Q4. What is a pure virtual function?**  
A virtual function declared with = 0. It makes the class abstract while its final overrider remains pure.

**Q5. Why use override?**  
It tells the compiler to verify that the derived function really overrides a base virtual function.

**Q6. Why a virtual destructor?**  
To enable correct destruction of a derived object through a base pointer when that usage is allowed.

**Q7. What is object slicing?**  
Copying a derived object by value into a base object discards the derived-specific part.

**Q8. Are vtables required by C++?**  
No. They are a common implementation method; the standard specifies runtime virtual behaviour, not one particular internal layout.

**Q9. Can constructors be virtual?**  
No. Construction establishes the object's type/lifetime in stages; constructors cannot be virtual functions.

**Q10. Can static member functions be virtual?**  
No. Static functions do not operate on a particular object and have no this pointer.

## Quick revision and next step
Overloading chooses a function from the arguments at compile time. Overriding plus virtual calls lets different objects respond differently at runtime. Next, Unit 10 gathers other concepts—static, const, friends, object relationships, copying, memory, exceptions, templates, namespaces and file organization—after the prerequisites are in place.

## Additional practice — polymorphism checkpoint

1. **Easy:** Can return type alone distinguish two overloads?
2. **Easy:** What keyword in the base enables runtime dispatch?
3. **Beginner coding:** Add Square as another Shape implementation with area = side × side.
4. **Beginner coding:** Write two overloaded print() functions, one for int and one for std::string.
5. **Output prediction:**

```cpp
#include <iostream>
struct Base { virtual void f() const { std::cout << "B"; } };
struct Derived : Base { void f() const override { std::cout << "D"; } };
int main() { Derived d; Base* p = &d; p->f(); }
```

6. **Debugging:** The base declares virtual void print() const, but the derived declares void print() without const and adds override. What happens, and why?

### Hints and answers
1. No. Overloads must be distinguishable by their parameter lists and other language rules, not return type alone.
2. virtual.
3. Derive Square from Shape and override area().
4. Provide void print(int) and void print(const std::string&); call each with the appropriate input.
5. Output: D, because the call is virtual and the dynamic type is Derived.
6. The compiler rejects it because the function does not override the const-qualified base method. Add const to the derived declaration/definition.

---
[← Previous: Unit 8](../Unit-08-Inheritance/README.md) · [Course home](../README.md) · [Next: Unit 10 — Additional Concepts →](../Unit-10-Additional-OOP-Concepts/README.md)
