# Unit 1 — Why Do We Need OOP?

**Prerequisite:** Unit 0 — basic variables, functions, structs and conditions.
**Estimated time:** 60–90 minutes.

## 1. Start with a real problem

Imagine you must store data for three students. You could write separate variables:
```cpp
#include <iostream>
#include <string>

int main() {
    std::string name1 = "Asha";
    int marks1 = 82;
    std::string name2 = "Kabir";
    int marks2 = 91;
    std::string name3 = "Mira";
    int marks3 = 76;

    std::cout << name1 << ": " << marks1 << '\n';
    std::cout << name2 << ": " << marks2 << '\n';
    std::cout << name3 << ": " << marks3 << '\n';
}
```

**Output**
```text
Asha: 82
Kabir: 91
Mira: 76
```

The program works, but scaling it to hundreds of students makes variable names and repeated code difficult to manage. Related values are separated, and every new operation must remember which name belongs with which marks.

## 2. Procedural programming

Procedural programming organizes work around functions. Functions are useful and remain important in C++. A small improvement is to group data and pass it to a print function.

```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    int marks;
};

void printStudent(Student student) {
    std::cout << student.name << ": " << student.marks << '\n';
}

int main() {
    Student students[] = {{"Asha", 82}, {"Kabir", 91}, {"Mira", 76}};
    for (Student s : students) {
        printStudent(s);
    }
}
```

**Output**
```text
Asha: 82
Kabir: 91
Mira: 76
```

This is already much better. A struct groups data, and a function performs a reusable operation. The function receives a copy of each record (passing by value). OOP builds on this idea by allowing a type to also define its operations and control how its state can be changed.

## 3. What is OOP?

**Object-oriented programming (OOP)** is a way to organize software around objects. An object has state (data) and behaviour (operations). A class describes what objects of a type contain and what they can do.

Think about a bank account. Its state includes the current balance. Its behaviour includes deposit and withdraw. If every part of a program can change the balance directly, invalid values can appear. A class can protect that rule.

## 4. A tiny first class

```cpp
#include <iostream>

class Counter {
public:
    int value = 0;

    void increase() {
        ++value;
    }
};

int main() {
    Counter c;
    c.increase();
    c.increase();
    std::cout << c.value << '\n';
}
```

**Output**
```text
2
```

A line-by-line explanation:
- class starts a class definition; Counter is the type's name.
- Curly braces contain the class's members.
- public means code outside the class may access these members.
- int value stores the counter's state and starts at zero.
- increase is a member function, a function that belongs to the class.
- ++value increases the current object's value by one.
- The semicolon after the closing brace completes the class definition.
- Counter c; creates an object named c.
- c.increase() calls the member function on that specific object.
- cout prints c's current value.

We intentionally made value public to keep this first example small. Unit 4 will explain why important data is often private.

## 5. When is OOP useful?

OOP can be a good fit when the program has entities with meaningful state and rules: bank accounts, students, inventory items, shapes or orders. It is also useful when different kinds of object should provide a common interface.

OOP is not required for every task. A one-line calculation or simple data transformation may be clearer as a free function. Good design chooses the simplest structure that fits the problem.

## 6. Four pillars — a preview

- **Encapsulation:** keep state and operations together and control access.
- **Abstraction:** expose what a caller needs without making them manage every detail.
- **Inheritance:** model a valid type relationship, such as Dog being an Animal.
- **Polymorphism:** let different types respond differently through a shared interface.

These are not four magic keywords. Each is a design idea we will learn through working code in later units.

## 7. Practical challenge — Mini Student Directory (beginner/intermediate)

### Problem
Store at least three students without creating separate variables for every field. Use a struct and a function to print each student as Name — Marks. Then explain which part is procedural and which part groups data.

### Sample solution
```cpp
#include <iostream>
#include <string>

struct Student {
    std::string name;
    int marks;
};

void print(const Student& s) {
    std::cout << s.name << " - " << s.marks << '\n';
}

int main() {
    Student classList[] = {{"Asha", 82}, {"Kabir", 91}, {"Mira", 76}};
    for (const Student& s : classList) {
        print(s);
    }
}
```

**Output**
```text
Asha - 82
Kabir - 91
Mira - 76
```

**Dry run:** the loop visits the first element, binds s to Asha's record and calls print; it repeats for Kabir and Mira. The struct groups data; the free function holds the printing procedure. OOP becomes useful when each kind of data needs behaviour and rules closely connected to it.

## Practice
1. Why do six unrelated variables become inconvenient for many students?
2. What does a struct improve in the mini directory?
3. Predict what would happen if the array contained four students instead of three.
4. Modify the print function so it also prints whether marks are at least 40.
5. Debug the class: what happens if you write class Counter { public: int value; } without the semicolon after the closing brace?

**Hints:** A loop can process each record; class and struct definitions end with a semicolon.

### Answers
1. Related information is scattered and repeated operations become harder to maintain.
2. It groups each student's related fields into one value.
3. The same loop works for each array element; it processes however many elements are present in the array.
4. Add an if/else inside print, based on s.marks >= 40.
5. It is a compile-time syntax error; write }; after the class body.

## Quick revision
- Procedural programming organizes around functions.
- A struct can group related data.
- OOP organizes a program around objects with state and behaviour.
- A class defines a type; an object is an instance of the type.
- OOP helps organize entities with state and rules, but is not always necessary.
- The four commonly taught pillars are encapsulation, abstraction, inheritance and polymorphism.

## Connection to Unit 2
We used a Counter class, but we still need to understand exactly what class members and objects are. Next we create small classes, make several objects and observe how each object holds separate state.

---
[← Previous: Unit 0](../Unit-00-Preparation-and-Basic-Cpp-Revision/README.md) · [Course home](../README.md) · [Next: Unit 2 — Classes and Objects →](../Unit-02-Classes-and-Objects/README.md)
