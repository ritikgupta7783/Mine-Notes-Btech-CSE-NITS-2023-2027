# Unit 5 — Constructors and Object Initialization

**Prerequisite:** Units 2–4.
**Estimated time:** 90 minutes.

## 1. Why do constructors exist?

Suppose a Student object has a name and age. If we create it and forget to assign the name or age, it may not represent a valid student. A constructor is a special member function that initializes a newly created object. It has the class name and no return type.

## 2. The simplest parameterized constructor

```cpp
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;
public:
    Student(std::string studentName, int studentAge) {
        name = studentName;
        age = studentAge;
    }

    void print() const {
        std::cout << name << ", " << age << '\n';
    }
};

int main() {
    Student s("Ritik", 20);
    s.print();
}
```

**Output**
```text
Ritik, 20
```

### Read Student s("Ritik", 20); slowly
- Student is the class name, so the variable will be an object of that type.
- s is the name chosen for this object.
- Parentheses contain argument values passed to the constructor.
- "Ritik" is a string literal that provides the first argument.
- 20 is an integer literal that provides the second argument.
- The constructor's parameters receive those values and initialize name and age.
- The semicolon ends the statement.

The constructor name matches the class name and it has no return type—not even void.

## 3. Default constructor and constructor overloading

A default constructor can be called without providing arguments. Constructor overloading means that one class has multiple constructors with different parameter lists.

```cpp
#include <iostream>
#include <string>

class Point {
private:
    int x;
    int y;
public:
    Point() {
        x = 0;
        y = 0;
    }

    Point(int xValue, int yValue) {
        x = xValue;
        y = yValue;
    }

    void print() const {
        std::cout << x << ", " << y << '\n';
    }
};

int main() {
    Point origin;
    Point point(3, 5);
    origin.print();
    point.print();
}
```

**Output**
```text
0, 0
3, 5
```

Point origin; chooses the no-argument constructor. Point point(3, 5); chooses the constructor that takes two integers. A parameterized constructor doesn't automatically mean the no-argument constructor exists; define it if needed.

## 4. Initialization versus assignment

Initialization establishes the initial value as the object is created. Assignment changes a value after the object/member has already been initialized. Constructor parameters and member initializer lists let us initialize members directly.

```cpp
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;
public:
    Student(std::string n, int a)
        : name(n), age(a) {
    }
    void print() const {
        std::cout << name << ", " << age << '\n';
    }
};

int main() {
    Student s("Mira", 19);
    s.print();
}
```

**Output**
```text
Mira, 19
```

### Initializer-list syntax explained
In Student(std::string n, int a), the part in parentheses declares parameters. The colon after the parameter list starts a member initializer list. name(n) means initialize the member name using parameter n. age(a) initializes the member age using parameter a. The braces form the constructor body, which is empty here because members were initialized already.

Members initialize in the order they are declared in the class, not the order typed in the initializer list. Initializer lists are essential for const members, references, bases and members that cannot be default-initialized.

## 5. Default arguments: use carefully

A constructor may provide default argument values, but this is different from defining a separate default constructor when overloads already exist.
```cpp
class User {
    int level;
public:
    explicit User(int userLevel = 1) : level(userLevel) {}
};
```
With this definition, User u; and User u(3); are valid. The single constructor has a default value for its parameter. Do not also add a conflicting zero-argument overload unless you understand how overload resolution works.

## 6. this pointer — first look

Inside a non-static member function, this refers to the object associated with that call. You may see this->member when a parameter has the same name as a member.

```cpp
class Counter {
    int value;
public:
    explicit Counter(int value) : value(value) {}
    void increase() { this->value++; }
    int get() const { return value; }
};
```

The first value inside value(value) is the member selected by this->value implicitly; the second value is the constructor parameter. The initializer-list spelling can be confusing at first, so use different parameter names (such as startValue) until you are comfortable. this is not available in static member functions because they are not called on a particular object.

## 7. Construction order
Base classes are initialized before members of a derived object. Within a class, data members are initialized in declaration order. Then the constructor body executes. We will explore base-class construction in Unit 8.

## 8. Common mistakes
- Giving a constructor a return type.
- Expecting a default constructor when only a parameterized constructor exists.
- Assigning to a const member in the constructor body instead of initializing it.
- Expecting members to initialize in initializer-list text order.
- Forgetting that default arguments are compile-time defaults for omitted arguments.
- Using this inside a static member function.

## 9. Practical challenge — Student Profile Builder (intermediate)

### Problem statement
Create a Student class with name, age and roll number. Provide a default constructor producing name "Unknown", age 0 and roll number -1, and a parameterized constructor. Use an initializer list. Print two objects and show the difference between their data.

### Solution
```cpp
#include <iostream>
#include <string>

class Student {
private:
    std::string name;
    int age;
    int roll;

public:
    Student() : name("Unknown"), age(0), roll(-1) {}

    Student(std::string n, int a, int r)
        : name(n), age(a), roll(r) {}

    void print() const {
        std::cout << "Name: " << name
                  << ", age: " << age
                  << ", roll: " << roll << '\n';
    }
};

int main() {
    Student unknown;
    Student realStudent("Riya", 20, 27);
    unknown.print();
    realStudent.print();
}
```

**Output**
```text
Name: Unknown, age: 0, roll: -1
Name: Riya, age: 20, roll: 27
```

### Explanation
The default constructor explicitly initializes each member. The parameterized constructor copies its arguments into the three members. Each object has its own values. For simplicity, the string parameters are copied; later you may see const references or move operations used for efficiency, but those are not needed for this unit.

**Stretch task:** reject a negative age. Choose whether invalid input should create an exception, return a validation result through a factory function, or use a documented fallback. Explain your choice.

## Practice
1. Why is a constructor useful?
2. Does a constructor return int or void?
3. Predict output for Point p; p.print();.
4. Add a constructor that accepts only x and sets y to zero.
5. Debug: class A { public: int x; A(int a) { x = a; } }; int main(){ A obj; }.
6. Why would a const member require an initializer list?

**Hints and answers**
1. It initializes newly created objects.
2. It has no return type.
3. With the shown default constructor, output is 0, 0.
4. Add Point(int xValue) : x(xValue), y(0) {} or the equivalent body-based initialization.
5. A(int) is the only constructor; obj has no argument, so the call is invalid. Define a default constructor or supply an argument.
6. A const member cannot be assigned a new value after it has been initialized.

## Quick revision
- Constructor name matches the class; it has no return type.
- A default constructor can be called without arguments.
- Parameterized constructors take initialization values.
- Overloaded constructors have different parameter lists.
- Initializer lists initialize members directly.
- Members initialize in declaration order.
- this refers to the current object in non-static functions.

## Connection to Unit 6
Constructors give an object a starting state. Now we will use constructors, private data and carefully designed methods together to preserve rules throughout the object's entire lifetime. That idea is called encapsulation.

---
[← Previous: Unit 4](../Unit-04-Access-Specifiers/README.md) · [Course home](../README.md) · [Next: Unit 6 — Encapsulation →](../Unit-06-Encapsulation/README.md)
