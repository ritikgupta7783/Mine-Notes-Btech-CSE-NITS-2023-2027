# Unit 3 — Functions Inside Classes

**Prerequisite:** Unit 0 functions; Unit 2 classes and objects.
**Estimated time:** 60–90 minutes.

## 1. First, recall an ordinary function

A function is a named block of code. It may receive inputs through parameters and may return a result. A member function is a function that belongs to a class and usually works on the object used to call it.

## 2. A function inside a class

```cpp
#include <iostream>

class Calculator {
public:
    int add(int a, int b) {
        return a + b;
    }
};

int main() {
    Calculator calc;
    std::cout << calc.add(3, 4) << '\n';
}
```

**Output**
```text
7
```

Read Calculator calc as “create an object of type Calculator, named calc.” Then calc.add(3, 4) calls that object's add member function. The values 3 and 4 are passed into parameters a and b; return sends the result back to the calling expression; cout prints it.

## 3. Return type, parameters and void

In int add(int a, int b), int before add is the return type. The function promises to return an integer. int a and int b are parameters. A parameter is a named input that receives its value when the function is called.

A void function does not return a value. It can still do useful work, such as printing:
```cpp
#include <iostream>
class Greeting {
public:
    void sayHello() {
        std::cout << "Hello!\n";
    }
};
int main() {
    Greeting g;
    g.sayHello();
}
```

**Output**
```text
Hello!
```

## 4. Defining a member function outside the class

When a function becomes long, its declaration can remain in the class while its definition appears below it. The scope resolution operator :: tells the compiler which class the definition belongs to.

```cpp
#include <iostream>

class Rectangle {
public:
    int width = 0;
    int height = 0;
    int area() const;
};

int Rectangle::area() const {
    return width * height;
}

int main() {
    Rectangle r;
    r.width = 4;
    r.height = 5;
    std::cout << r.area() << '\\n';
}
```

**Output**
```text
20
```

### Read the syntax carefully
- Rectangle::area says the area function belongs to Rectangle.
- The two colon characters together form the scope resolution operator.
- int before the function name states that area returns an integer.
- The parentheses contain parameter declarations, if any.
- const after the parentheses states that area does not change the ordinary state of the object.
- A semicolon inside the class ends the declaration; curly braces below contain the definition.

For now we create the object first and assign its public fields. Unit 5 will show how a constructor can initialize members as the object is created.

## 5. Calling one member function from another

A member function can call another member function on the same object. You generally do not need to write the object name again inside the class.

```cpp
#include <iomanip>
#include <iostream>

class Temperature {
public:
    double celsius = 0;

    double toFahrenheit() const {
        return celsius * 9.0 / 5.0 + 32.0;
    }

    double toKelvin() const {
        return celsius + 273.15;
    }

    void print() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Celsius: " << celsius << '\\n';
        std::cout << "Fahrenheit: " << toFahrenheit() << '\\n';
        std::cout << "Kelvin: " << toKelvin() << '\\n';
    }
};

int main() {
    Temperature t;
    t.celsius = 25;
    t.print();
}
```

**Output**
```text
Area: 12
Perimeter: 14
```

The print function reuses the logic in area() and perimeter(). That avoids repeating the formulas in multiple places. Constructor initialization is deliberately left for Unit 5.

## 6. Dry run

For r.print():
1. r was constructed with width 4 and height 3.
2. print calls area(), which returns 4 × 3 = 12.
3. print calls perimeter(), which returns 2 × (4 + 3) = 14.
4. print sends both results to the output stream.

## 7. Common mistakes
- Calling a member function without an object outside the class.
- Forgetting to return a value from a non-void function.
- Returning a value from a void function.
- Writing Rectangle.area() instead of defining the function with Rectangle::area().
- Declaring a function inside the class but never defining it when the program requires a definition.
- Confusing a function declaration ending in semicolon with a definition that has a body.

## 8. Practical challenge — Temperature Converter

### Problem statement
Create a Temperature class that stores Celsius and provides member functions to convert to Fahrenheit and Kelvin. Use the formulas F = C × 9 / 5 + 32 and K = C + 273.15. Add a print() function that calls both conversion functions. Show the output for 25°C.

### Solution
```cpp
#include <iomanip>
#include <iostream>

class Temperature {
    double celsius;
public:
    explicit Temperature(double value) : celsius(value) {}

    double toFahrenheit() const {
        return celsius * 9.0 / 5.0 + 32.0;
    }

    double toKelvin() const {
        return celsius + 273.15;
    }

    void print() const {
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "Celsius: " << celsius << '\n';
        std::cout << "Fahrenheit: " << toFahrenheit() << '\n';
        std::cout << "Kelvin: " << toKelvin() << '\n';
    }
};

int main() {
    Temperature t(25);
    t.print();
}
```

**Output**
```text
Celsius: 25.00
Fahrenheit: 77.00
Kelvin: 298.15
```

### Why this design helps
Each conversion formula is defined once. print() reuses those member functions, so the program avoids duplicated calculations. const means the conversion functions inspect the temperature but do not change it.

**Stretch task:** add toCelsiusFromFahrenheit(double f) as a separate named constructor or helper; explain which formula needs to be used.

## Practice
1. What is a member function?
2. What does void mean as a return type?
3. Predict the result of add(8, 9).
4. Write an int multiply(int a, int b) member function.
5. Debug this declaration: int area() const; followed by int Rectangle.area() const { ... }.
6. Why might a long member function be defined outside the class?

**Hints and answers**
1. A function that belongs to a class.
2. It means the function does not return a value.
3. 17.
4. Return a * b from the body.
5. In C++, use Rectangle::area, not dot notation, in the out-of-class definition.
6. It keeps the class declaration easier to scan and separates interface from implementation.

## Quick revision
- Member functions belong to a class.
- Parameters receive inputs; return values send results to the caller.
- void means no return value.
- :: connects an out-of-class member function definition with its class.
- One member function can call another member function.
- Reuse named operations rather than duplicating formulas.

## Connection to Unit 4
We now know where class data and functions live. But who is allowed to use or change that data? Next we introduce public, private and protected and learn how C++ reports invalid access.

---
[← Previous: Unit 2](../Unit-02-Classes-and-Objects/README.md) · [Course home](../README.md) · [Next: Unit 4 — Access Specifiers →](../Unit-04-Access-Specifiers/README.md)
