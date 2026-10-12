# C++ OOP Troubleshooting Guide

This guide focuses on the errors beginners most often encounter while compiling the examples.

## 1. Missing semicolon after class

**Symptom:** compiler reports an error near the next statement after a class.
```cpp
class Lamp {
public:
    void turnOn() {}
}; // Required semicolon
```
A class definition ends with };. The semicolon is required even though the body uses braces.

## 2. Private member is inaccessible

**Symptom:** “is private within this context” or similar diagnostic.
```cpp
class Account {
    int balance = 100; // private by default
public:
    int getBalance() const { return balance; }
};
```
Use an appropriate public operation. Do not simply make every member public if the object has rules to protect.

## 3. No matching constructor

**Symptom:** compiler says no matching constructor or no default constructor exists.
```cpp
class Student {
public:
    explicit Student(int roll) {}
};
int main() {
    // Student s; // invalid: only the int constructor exists
    Student s(20);
}
```
Either provide an explicit default constructor or pass the required argument.

## 4. Function declared but not defined

**Symptom:** compilation succeeds but the linker reports an undefined reference.
A member function was declared but no matching definition was linked. Check spelling, parameters, const qualification, namespace/class scope, and whether all .cpp files were compiled.

## 5. Wrong override signature

**Symptom:** compiler says the function marked override does not override.
```cpp
struct Base { virtual void print() const {} };
struct Child : Base {
    void print() const override {} // matching signature
};
```
Check parameter types, const qualifiers, reference qualifiers where relevant and the base declaration.

## 6. Forgot a standard header

**Symptom:** a type/function such as string, vector, cout or unique_ptr is not declared.
Include the appropriate header: iostream for stream input/output, string for std::string, vector for std::vector, memory for smart pointers, stdexcept for common exception types, utility for std::move/exchange, and algorithm for many standard algorithms.

## 7. Namespace issue

**Symptom:** compiler says cout or string is not declared.
Prefer std::cout and std::string in beginner code. Avoid scattering using namespace std into headers, because it can create name conflicts in files that include those headers.

## 8. Compile multiple files correctly

If a project has main.cpp, Student.cpp and Student.hpp, compile both .cpp files:
```bash
g++ -std=c++17 -Wall -Wextra -pedantic main.cpp Student.cpp -o app
```
Compiling only main.cpp may leave required definitions out of the link.

## 9. Output differs because of formatting

- bool prints as 1/0 by default; std::boolalpha prints true/false.
- Floating-point values may have many decimal digits; std::fixed and std::setprecision(2) set a two-decimal display.
- A newline in a printed string is different from typing the two literal characters backslash and n. In C++, '\n' is the common newline escape in a character/string literal.
- Input prompts may appear beside the user's typed input in some terminals.

## 10. Runtime bugs
- Uninitialized local variables have indeterminate values.
- Array indexes start at zero and must stay within bounds.
- A pointer can dangle after its target's lifetime ends.
- Deleting the same allocation twice is undefined behaviour.
- Deleting a derived object through a base pointer requires a virtual base destructor when using that ownership pattern.
- A function can throw; make sure the caller has a suitable handler or the failure is intentionally allowed to terminate.

## How to debug systematically
1. Read the first compiler error, not only the last.
2. Inspect the line named in the error and a few lines above it.
3. Check punctuation, braces, semicolons and includes.
4. Compile the smallest reproducible version.
5. Fix one error, then compile again.
6. Compare actual output with expected output.
7. Do not treat undefined behaviour as if it has a guaranteed output.
