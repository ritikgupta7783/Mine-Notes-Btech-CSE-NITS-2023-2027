````
# 01 — OOP Foundations

## What is OOP?

OOP stands for **Object-Oriented Programming**. It is a programming approach that organizes code around **classes and objects**.

An object combines two things:

- **State:** Data or properties of an object.
- **Behaviour:** Operations or functions an object can perform.

For example, a bank account has a balance as its state and operations such as deposit and withdraw as its behaviour.

C++ supports OOP, but it is a **multi-paradigm programming language** because it also supports procedural and generic programming.

## Class and Object

**Class:** A user-defined type that groups related data members and member functions.

**Object:** An instance of a class.

Think of a class as a blueprint and an object as something created using that blueprint.

### Code Example

```cpp
#include <iostream>
#include <string>
using namespace std;

class Student {
public:
    string name;
    int age;

    void display() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};

int main() {
    Student s1;

    s1.name = "Ritik";
    s1.age = 21;

    s1.display();

    return 0;
}
````

### Output

```
Name: Ritik
Age: 21
```

### Explanation

- `class Student` defines a class.
- `s1` is an object of the `Student` class.
- `name` and `age` are data members.
- `display()` is a member function.
- `public` allows these members to be accessed from outside the class.

## The Four Pillars of OOP

The four main pillars of OOP are:

1. Encapsulation: Combining data and related functions into a class while controlling access to the data.
2. Abstraction: Showing essential operations while hiding implementation details.
3. Inheritance: Creating a new class from an existing class.
4. Polymorphism: Allowing the same interface or operation to exhibit different behaviours.

Detailed explanations of these four pillars will be covered in their respective chapters.

## Procedural vs Object-Oriented Programming

| Procedural Programming                    | Object-Oriented Programming                            |
| ----------------------------------------- | ------------------------------------------------------ |
| Organizes code mainly around functions    | Organizes code around classes and objects              |
| Focuses on operations and procedures      | Combines data and related behaviour                    |
| Data is often passed between functions    | Data can be protected using access control             |
| Suitable for straightforward computations | Useful for modelling entities with state and behaviour |

Neither approach is universally better; the choice depends on the problem.

## Advantages of OOP

- Modularity: Divides a program into manageable components.
- Code reuse: Allows existing code to be reused.
- Maintainability: Makes well-organized programs easier to update.
- Data protection: Access control helps prevent invalid modifications.
- Extensibility: Supports adding new functionality through suitable designs.

## Limitations of OOP

- Too many classes can make simple programs unnecessarily complicated.
- Deep inheritance hierarchies can be difficult to maintain.
- Objects and abstractions may introduce additional complexity.
- OOP is not always the simplest choice for every problem.

## Interview Questions and Answers

Q1. What is OOP?

OOP is a programming approach that organizes code around classes and objects, combining data and behaviour.

Q2. Is C++ a pure object-oriented language?

No. C++ is a multi-paradigm language that supports procedural, object-oriented, generic, and other programming styles.

Q3. What is a class?

A class is a user-defined type that groups data members and member functions.

Q4. What is an object?

An object is an instance of a class with its own instance data.

Q5. What is the difference between a class and an object?

A class defines the structure and behaviour, while an object is an instance created from that class.

Q6. What are the four pillars of OOP?

Encapsulation, abstraction, inheritance, and polymorphism.

Q7. What is the difference between procedural programming and OOP?

Procedural programming focuses mainly on functions and operations, whereas OOP organizes related data and behaviour around classes and objects.

Q8. Does every class need inheritance?

No. Inheritance is useful when there is a genuine relationship between types. Many classes work perfectly well without inheritance.

## Quick Revision

- OOP: Organizes programs around classes and objects.
- Class: A user-defined type.
- Object: An instance of a class.
- Data members: Variables declared in a class.
- Member functions: Functions declared in a class.
- Four pillars: Encapsulation, abstraction, inheritance, and polymorphism.
- C++: A multi-paradigm programming language.

```
```