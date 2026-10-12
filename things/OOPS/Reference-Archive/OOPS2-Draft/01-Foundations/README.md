# 01 — OOP Foundations

## 1. What Is OOP?

OOP stands for **Object-Oriented Programming**. It is a programming approach that organizes code around **classes and objects**.

An object combines two things:

- **State:** Data or properties of an object.
- **Behaviour:** Operations or functions an object can perform.

For example, a bank account has a balance as its state and operations such as depositing and withdrawing money as its behaviour.

C++ supports OOP, but it is a **multi-paradigm programming language** because it also supports procedural and generic programming.

## 2. Class and Object

### Class

A **class** is a user-defined type that groups related data members and member functions into a single unit.

Think of a class as a blueprint used to create objects.

### Object

An **object** is an instance of a class. It has its own data and can use the functions defined in the class.

**Example:** `Student` is a class, while `s1` is an object created from that class.

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
```

### Output

```text
Name: Ritik
Age: 21
```

### Explanation

- `class Student` defines a class.
- `s1` is an object of the `Student` class.
- `name` and `age` are data members.
- `display()` is a member function.
- `public` allows these members to be accessed from outside the class.
- `s1.display()` calls the function using the object `s1`.

**Remember:** A class defines the structure, while an object is an instance of that class.

## 3. The Four Pillars of OOP

The four main pillars of object-oriented programming are:

1. **Encapsulation:** Combining data and related functions into a class while controlling access to the data.
2. **Abstraction:** Showing essential operations while hiding implementation details.
3. **Inheritance:** Creating a new class from an existing class.
4. **Polymorphism:** Allowing the same interface or operation to exhibit different behaviours.

*Detailed explanations and code examples of these four pillars will be covered in their respective chapters.*

## 4. Procedural Programming vs Object-Oriented Programming

| Procedural Programming | Object-Oriented Programming |
|---|---|
| Organizes code mainly around functions. | Organizes code around classes and objects. |
| Focuses on operations and procedures. | Combines data and related behaviour. |
| Data is often passed between functions. | Data can be protected using access control. |
| Suitable for straightforward computations. | Useful for modelling entities with state and behaviour. |

**Note:** Neither approach is universally better. The choice depends on the problem and the design requirements.

## 5. Advantages of OOP

- **Modularity:** Divides a program into manageable components.
- **Code reusability:** Allows existing code to be reused.
- **Maintainability:** Makes well-organized programs easier to update.
- **Data protection:** Access control helps prevent invalid modifications.
- **Extensibility:** Supports adding functionality through suitable designs.

## 6. Limitations of OOP

- Too many classes can make simple programs unnecessarily complicated.
- Deep inheritance hierarchies can be difficult to maintain.
- Excessive abstraction can make code harder to understand.
- OOP is not always the simplest approach for every problem.

## 7. Interview Questions and Answers

### Q1. What is OOP?

**Answer:** OOP is a programming approach that organizes code around classes and objects, combining data and behaviour.

### Q2. Is C++ a pure object-oriented programming language?

**Answer:** No. C++ is a multi-paradigm language that supports procedural, object-oriented, generic, and other programming styles.

### Q3. What is a class?

**Answer:** A class is a user-defined type that groups related data members and member functions.

### Q4. What is an object?

**Answer:** An object is an instance of a class that has its own instance data and can use the class's member functions.

### Q5. What is the difference between a class and an object?

**Answer:** A class defines the structure and behaviour, while an object is an instance created from that class.

### Q6. What are data members and member functions?

**Answer:**
- **Data members:** Variables declared inside a class.
- **Member functions:** Functions declared inside a class that define its operations.

### Q7. What are the four pillars of OOP?

**Answer:** Encapsulation, abstraction, inheritance, and polymorphism.

### Q8. What is the difference between procedural programming and OOP?

**Answer:** Procedural programming focuses mainly on functions and operations, whereas OOP organizes related data and behaviour around classes and objects.

### Q9. Does every class need inheritance?

**Answer:** No. Inheritance is useful when there is a genuine relationship between types. Many classes work perfectly well without inheritance.

### Q10. Can we create multiple objects from the same class?

**Answer:** Yes. We can create multiple objects from the same class, and each object can maintain its own instance data.

For example:

```cpp
Student s1;
Student s2;
Student s3;
```

Here, `s1`, `s2`, and `s3` are three separate objects of the `Student` class.

## 8. Quick Revision

- **OOP:** Organizes programs around classes and objects.
- **Class:** A user-defined type.
- **Object:** An instance of a class.
- **Data members:** Variables declared inside a class.
- **Member functions:** Functions declared inside a class.
- **Four pillars:** Encapsulation, abstraction, inheritance, and polymorphism.
- **C++:** A multi-paradigm programming language.

**Interview tip:** Understand the difference between a class and an object, practise writing the example program, and be able to explain its output in your own words.