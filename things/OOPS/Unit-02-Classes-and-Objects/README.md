# Unit 2 — Classes and Objects

**Prerequisite:** Unit 0 variables and functions; Unit 1 why OOP is useful.
**Estimated time:** 75–100 minutes.

## 1. Real-life analogy

A cookie cutter describes a shape; each cookie made with it is a separate item. A class plays a role similar to the cutter, and each object is a separate instance created from the class. The analogy is limited: a C++ class is a type definition with rules, not a physical template.

## 2. First class and first object

```cpp
#include <iostream>

class Lamp {
public:
    bool isOn = false;

    void turnOn() {
        isOn = true;
    }

    void showState() const {
        std::cout << (isOn ? "ON" : "OFF") << '\n';
    }
};

int main() {
    Lamp deskLamp;
    deskLamp.showState();
    deskLamp.turnOn();
    deskLamp.showState();
}
```

**Output**
```text
OFF
ON
```

### Syntax explained
- class starts the definition; Lamp is the class name.
- public makes the following members accessible from outside.
- bool isOn is a data member: each Lamp object has its own boolean state.
- turnOn is a member function: it changes the state of the object that receives the call.
- showState() const is a member function that promises not to change the object's ordinary state.
- Lamp deskLamp; creates an object called deskLamp.
- deskLamp.turnOn(); uses the dot operator to call turnOn on that one object.
- The class ends with };. The semicolon is required after a class definition.

## 3. Multiple objects have separate state

```cpp
#include <iostream>
class Counter {
public:
    int value = 0;
    void increase() { ++value; }
};
int main() {
    Counter first;
    Counter second;
    first.increase();
    first.increase();
    second.increase();
    std::cout << first.value << '\n';
    std::cout << second.value << '\n';
}
```

**Output**
```text
2
1
```

Dry run:
| Step | first.value | second.value |
|---|---:|---:|
| Both objects created | 0 | 0 |
| first.increase() | 1 | 0 |
| first.increase() again | 2 | 0 |
| second.increase() | 2 | 1 |

The class definition is shared, but ordinary data members belong to each object separately.

## 4. A class and an object are not the same thing

A class defines what a Lamp object can contain and do. The statement Lamp deskLamp; creates an actual object with its own lifetime. Merely defining the class does not create a deskLamp object. An object can be local to a function, stored in a container, or created dynamically; dynamic allocation will be introduced later.

## 5. dot operator and member access

Use object.member to access a member through an object, such as deskLamp.turnOn() or deskLamp.isOn. You will later learn arrow syntax for pointers: pointer->member. Do not use arrow syntax on an ordinary object.

## 6. Common mistakes
- Forgetting the semicolon after the class body.
- Trying to call a member function as if it were a free function.
- Assuming all objects share ordinary data-member values.
- Using an object before declaring it.
- Using a name that differs in capitalization: Lamp and lamp are different identifiers.
- Putting logic in a class without considering whether it belongs to each object.

## 7. Practical challenge — Rectangle Calculator (beginner/intermediate)

### Problem
Create a Rectangle class with width and height. Create two rectangle objects with different dimensions. Add an area() member function and print the two areas. In this unit, keep the fields public for simplicity; the next units will improve access control.

### Solution
```cpp
#include <iostream>
class Rectangle {
public:
    int width;
    int height;

    int area() const {
        return width * height;
    }
};
int main() {
    Rectangle a{4, 3};
    Rectangle b{5, 6};
    std::cout << a.area() << '\n';
    std::cout << b.area() << '\n';
}
```

**Output**
```text
12
30
```

Dry run: a.area() returns 4 × 3 = 12; b.area() returns 5 × 6 = 30. One class supports multiple objects with different dimensions. Aggregate initialization like Rectangle a{4, 3}; uses the supplied values to initialize the public data members in order.

**Stretch task:** add perimeter(), defined as 2 × (width + height), and calculate it for both objects.

## Practice
1. What does a class describe?
2. What is an object?
3. Predict the two outputs if first.increase() is called three times and second.increase() is never called.
4. Add a reset() member function to Counter.
5. Debug this snippet: `Lamp p; p.turnOn;`. Why is a function call's parentheses needed?

### Hints and answers
1. A user-defined type's members and access rules.
2. An instance of a class with its own lifetime and state.
3. The first object prints 3; the second prints 0.
4. Define void reset() { value = 0; } inside Counter.
5. Write p.turnOn();. The parentheses call the function; without them, the expression refers to the function rather than invoking it.

## Quick revision
- A class defines the type; an object is an instance.
- Data members store state; member functions implement behaviour.
- Every object has its own non-static data members.
- Use dot notation with ordinary objects.
- Class definitions end with a semicolon.
- Public data is useful for learning but can permit invalid values.

## Connection to Unit 3
We have placed a function inside a class. Next we will slow down and study member functions themselves, including parameters, return values, defining functions outside the class, and the scope resolution operator.

---
[← Previous: Unit 1](../Unit-01-Why-Do-We-Need-OOP/README.md) · [Course home](../README.md) · [Next: Unit 3 — Member Functions →](../Unit-03-Functions-Inside-Classes/README.md)
