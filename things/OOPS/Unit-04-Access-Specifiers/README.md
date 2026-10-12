# Unit 4 — Access Specifiers: public, private and protected

**Prerequisite:** Units 2–3.
**Estimated time:** 60–80 minutes.

## 1. Why control access?

Suppose a bank account contains a balance. If every part of the program can write account.balance = -500, the object may enter an invalid state. Access specifiers tell C++ which code can use each class member. They are compiler-enforced access rules, not password protection or encryption.

## 2. The three specifiers

- **public:** accessible from ordinary code that has an object and follows normal rules.
- **private:** accessible directly from member functions of the same class and its friends.
- **protected:** accessible from the class/friends and eligible derived-class contexts; we'll use it more in inheritance.

In a class, members are private by default. In a struct, members are public by default.

## 3. A valid access example

```cpp
#include <iostream>

class ExamResult {
private:
    int marks = 88;
public:
    int getMarks() const {
        return marks;
    }
};

int main() {
    ExamResult result;
    std::cout << result.getMarks() << '\n';
}
```

**Output**
```text
88
```

The marks variable is private, so main cannot directly access it. The public getMarks() function provides a controlled way to read it.

## 4. Example of a compile-time error

```cpp
class ExamResult {
private:
    int marks = 88;
};

int main() {
    ExamResult result;
    // result.marks = 50; // Uncommenting this causes a compile-time error.
}
```

There is no runtime output. If the commented line is uncommented, compilation fails because marks is private. A compile-time error is not an expected printed message; it is a compiler diagnostic.

## 5. Access table

| Where is access attempted? | public member | private member | protected member |
|---|---|---|---|
| Ordinary code using an object | Yes | No | No |
| Member function of same class | Yes | Yes | Yes |
| Friend function/class | Yes | Yes | Yes |
| Derived class code | Yes, subject to inheritance access | Not directly | Yes, subject to inheritance rules |

The exact protected rule has details when one derived type accesses a protected member through objects of another type. For beginners, remember that protected is mainly intended for the class and derived-class implementations, not general callers.

## 6. Default access: class vs struct

```cpp
struct PublicRecord {
    int value = 10; // public by default
};

class PrivateRecord {
    int value = 10; // private by default
public:
    int getValue() const { return value; }
};

int main() {
    PublicRecord a;
    a.value = 20; // allowed

    PrivateRecord b;
    // b.value = 20; // compile-time error
    int x = b.getValue();
}
```

No output is produced because this example demonstrates valid assignments and a getter without printing anything. The important difference is the default access level, not a difference in capability between class and struct.

## 7. Common mistakes
- Assuming all class members are public unless marked private.
- Trying to use private members directly from main.
- Treating protected as “public but safer.” It is intended for derived-class access.
- Thinking private access is a runtime check.
- Adding a public setter that lets anyone violate the class's rules.

## 8. Practical challenge — Validated Exam Marks

### Problem statement
Create a Marks class that stores a score from 0 to 100, starting at 0. The score must be private. A public setScore() should reject invalid values and report success/failure. Add a getter and demonstrate both an accepted and rejected update.

### Solution
```cpp
#include <iostream>

class Marks {
private:
    int score = 0;
public:
    bool setScore(int value) {
        if (value < 0 || value > 100) return false;
        score = value;
        return true;
    }

    int getScore() const { return score; }
};

int main() {
    Marks m;
    std::cout << m.setScore(85) << '\n';
    std::cout << m.setScore(130) << '\n';
    std::cout << m.getScore() << '\n';
}
```

**Output**
```text
1
0
85
```

The two booleans appear as 1 and 0 by default. std::boolalpha would display true and false. The invalid value 130 is rejected and leaves score at 85.

**Stretch task:** make the constructor reject invalid starting values with an exception instead of substituting zero. What should the calling code do?

## Practice
1. Which access level permits ordinary callers to use a member?
2. What is the default access inside class?
3. Predict the output if setScore(101) is called after setScore(40).
4. Change the valid score range to 0–50.
5. Why doesn't the invalid-line example have runtime output?
6. Debug: a program tries to print obj.secret when secret is private.

**Hints and answers**
1. public.
2. private.
3. The call returns false and the stored score remains 40.
4. Change the upper-bound test from 100 to 50.
5. An uncommented direct private access prevents compilation.
6. Provide a suitable public getter or an operation, rather than accessing the private field directly.

## Quick revision
- public is accessible from ordinary callers.
- private is directly accessible to class members and friends.
- protected mainly supports derived class implementation.
- class defaults to private; struct defaults to public.
- Invalid private access is a compile-time error.
- Getters/setters should protect useful rules, not exist mechanically for every field.

## Connection to Unit 5
Access control gives us a way to protect data, but we also need to guarantee that a new object starts in a valid state. Next we learn constructors and the different ways to initialize objects.

---
[← Previous: Unit 3](../Unit-03-Functions-Inside-Classes/README.md) · [Course home](../README.md) · [Next: Unit 5 — Constructors →](../Unit-05-Constructors-and-Object-Initialization/README.md)
