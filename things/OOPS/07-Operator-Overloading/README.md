# 07 — Operator Overloading

Operator overloading gives an operator an appropriate meaning for a user-defined type. At least one operand must be a user-defined or enumeration type; built-in operators cannot be redefined for two built-in operands.

## Complex number example
    #include <iostream>
    class Complex {
        double re, im;
    public:
        Complex(double r=0, double i=0): re(r), im(i) {}
        Complex operator+(const Complex& rhs) const {
            return {re + rhs.re, im + rhs.im};
        }
        friend std::ostream& operator<<(std::ostream& os, const Complex& c) {
            return os << c.re << (c.im < 0 ? "" : "+") << c.im << "i";
        }
    };
    int main() {
        Complex a(2,3), b(4,-1);
        std::cout << a+b << '\n'; // 6+2i
    }

## Prefix and postfix increment
    struct Number {
        int value;
        Number& operator++() { ++value; return *this; } // prefix
        Number operator++(int) { Number old=*this; ++value; return old; } // postfix
    };

The dummy int distinguishes postfix. Prefix usually returns a reference to the updated object; postfix returns the old value.

## Rules
Cannot invent new operator tokens or change precedence, associativity or arity. Operators such as ::, ., .*, ?: and sizeof cannot be overloaded. Overloads should preserve intuitive meaning. Stream insertion commonly returns std::ostream& to enable chaining.

## Interview questions
1. Can + be overloaded for two integers? No; both operands are built-in types.
2. Can precedence change? No.
3. Why return a stream reference from operator<<? To support chaining and return the same stream.
4. How is postfix increment distinguished? It takes a dummy int parameter.
