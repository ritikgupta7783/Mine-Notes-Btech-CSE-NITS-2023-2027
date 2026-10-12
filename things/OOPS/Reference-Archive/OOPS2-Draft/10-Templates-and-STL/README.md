# 10 — Templates and STL

Templates support generic programming and are often called compile-time/static polymorphism. They are not the same mechanism as virtual dispatch.

## Function template
```cpp
template <typename T>
T maximum(T a, T b) { return a < b ? b : a; }
```
The compiler can deduce `T` when the arguments satisfy template deduction rules.

## Class template
```cpp
template <typename T>
class Box {
    T value;
public:
    explicit Box(T v): value(std::move(v)) {}
    const T& get() const { return value; }
};
```
`Box<int>` and `Box<std::string>` are different specializations.

## Templates vs virtual functions
| Templates | Virtual dispatch |
|---|---|
| Usually resolved/instantiated at compile time | Chooses implementation at runtime |
| Works with compatible types without inheritance | Uses a base/derived virtual interface |
| Can generate specialized code per type | Often useful for heterogeneous collections |

## STL and OOP
The Standard Template Library includes containers, iterators, algorithms and function objects. Containers such as `std::vector` and `std::map` are class types; algorithms such as `std::sort` operate on compatible iterators.
```cpp
#include <algorithm>
#include <iostream>
#include <vector>
int main() {
    std::vector<int> v{5,1,4,2};
    std::sort(v.begin(), v.end());
    for (int x : v) std::cout << x << ' '; // 1 2 4 5
}
```

## Interview questions
1. **Are templates polymorphism?** Commonly described as compile-time polymorphism.
2. **What is specialization?** A tailored implementation for particular template arguments; class templates also support partial specialization.
3. **Why are template definitions usually in headers?** Their definitions generally need to be visible where implicit instantiation occurs.
4. **Is STL only containers?** No; algorithms, iterators and function objects are also central parts.
