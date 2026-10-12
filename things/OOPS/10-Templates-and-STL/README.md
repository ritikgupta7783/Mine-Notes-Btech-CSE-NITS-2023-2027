# Unit 10 — Templates and the Standard Template Library

**Goal:** Understand generic programming, class/function templates, and how templates and STL containers support reusable C++ design.

## 1. Why templates exist

Without templates, you might write separate maximum functions for int, double and long long. The algorithms would be almost identical. A function template lets the compiler generate a suitable version for compatible types. This is often called compile-time or static polymorphism.

## 2. Function template

```cpp
#include <iostream>
#include <string>

template <typename T>
T maximum(T a, T b) {
    return (a < b) ? b : a;
}

int main() {
    std::cout << maximum(4, 9) << '\n';
    std::cout << maximum(2.5, 1.7) << '\n';
    std::cout << maximum(std::string("Ada"), std::string("Riya")) << '\n';
}
```

**Output**
```text
9
2.5
Riya
```

The type T is inferred from the arguments. The operations used by the template must make sense for T; in this case T values must be comparable with < and returnable by value.

## 3. Class template

```cpp
#include <iostream>
#include <string>
#include <utility>

template <typename T>
class Box {
private:
    T value;
public:
    explicit Box(T v) : value(std::move(v)) {}
    const T& get() const { return value; }
};

int main() {
    Box<int> number(42);
    Box<std::string> label("OOP");
    std::cout << number.get() << '\n';
    std::cout << label.get() << '\n';
}
```

**Output**
```text
42
OOP
```

Box<int> and Box<std::string> are different specializations. The template is a recipe; the specialized type is what the compiler instantiates for concrete template arguments.

## 4. Templates vs virtual functions

| Templates | Virtual dispatch |
|---|---|
| Usually instantiated/selected at compile time | Chooses a final overrider at runtime |
| Does not require inheritance | Uses a base/derived virtual interface |
| Often generates specialized code for each type | Often enables a heterogeneous collection through base pointers/references |
| Requires template argument operations to be valid | Uses a runtime contract expressed by a base class |

Templates and virtual dispatch solve related but different problems; neither replaces the other in every situation.

## 5. STL: containers, iterators and algorithms

The Standard Template Library is a central part of the C++ standard library. Common pieces include:
- **Containers:** vector, deque, list, map, unordered_map, set, queue and stack.
- **Iterators:** objects that let algorithms traverse ranges.
- **Algorithms:** sort, find, count, transform, binary_search and many others.
- **Function objects/callables:** functions or objects supplied to algorithms to customize behaviour.

```cpp
#include <algorithm>
#include <iostream>
#include <vector>

int main() {
    std::vector<int> values{5, 1, 4, 2, 2};
    std::sort(values.begin(), values.end());

    auto it = std::find(values.begin(), values.end(), 4);
    std::cout << "Sorted: ";
    for (int x : values) std::cout << x << ' ';
    std::cout << "\nFound 4: " << std::boolalpha
              << (it != values.end()) << '\n';
}
```

**Output**
```text
Sorted: 1 2 2 4 5
Found 4: true
```

STL use is OOP-friendly because containers expose stable interfaces and manage resources, while templates let algorithms work with many compatible types.

## 6. Generic programming good practices

- Prefer standard algorithms over hand-written loops when they express the intent clearly.
- Choose the container for the access pattern: vector for contiguous sequence/random access, map for ordered key lookup, unordered_map for hash lookup, queue for FIFO.
- Don't assume all containers have the same performance complexity.
- Template definitions normally need to be visible at the point of implicit instantiation, which is why they are commonly placed in headers.
- Template errors can be difficult to read; keep generic interfaces small and requirements clear.

## 7. Practical challenge — Generic Inventory Counter (intermediate/tough)

### Problem statement
Implement a generic Registry that stores items with string keys. It should support:
- adding/updating a key-value pair;
- finding a key and returning a pointer to its value, or nullptr if absent;
- reporting the number of distinct keys;
- printing keys in sorted order.
Use std::map. Demonstrate it with string-to-int stock counts and show both an existing and a missing key.

### Worked solution
```cpp
#include <iostream>
#include <map>
#include <string>
#include <utility>

template <typename T>
class Registry {
private:
    std::map<std::string, T> values;

public:
    void put(std::string key, T value) {
        values.insert_or_assign(std::move(key), std::move(value));
    }

    T* find(const std::string& key) {
        auto it = values.find(key);
        return it == values.end() ? nullptr : &it->second;
    }

    std::size_t size() const { return values.size(); }

    void print() const {
        for (const auto& [key, value] : values) {
            std::cout << key << ": " << value << '\n';
        }
    }
};

int main() {
    Registry<int> stock;
    stock.put("Keyboard", 12);
    stock.put("Mouse", 7);
    stock.put("Keyboard", 10); // update, not a new distinct key

    stock.print();
    std::cout << "Distinct items: " << stock.size() << '\n';

    if (int* count = stock.find("Mouse")) {
        std::cout << "Mouse stock: " << *count << '\n';
    }
    std::cout << "Missing key found: "
              << std::boolalpha << (stock.find("Monitor") != nullptr) << '\n';
}
```

**Output**
```text
Keyboard: 10
Mouse: 7
Distinct items: 2
Mouse stock: 7
Missing key found: false
```

### Explanation
Registry<T> is generic over the stored value type, while the key is always a string. std::map maintains keys in sorted order. insert_or_assign updates an existing value. find returns an address to the mapped value only while the element remains valid; callers must not keep such pointers across operations that erase the element or destroy the registry.

The example uses a C++17 structured binding in the range loop. Always match the compiler's language standard to the code.

**Stretch task:** make Registry work with integer keys too, by templating both Key and Value. What operations must Key support if you choose std::map?

## 8. End-of-unit interview questions with answers

**Q1. What is a template?**  
A compile-time recipe for generating functions or classes using type/value parameters.

**Q2. Are templates polymorphism?**  
They are commonly described as compile-time/static polymorphism. Virtual functions provide runtime polymorphism.

**Q3. Class template vs class?**  
A class template is a parameterized recipe; an instantiated specialization such as Box<int> is a concrete type.

**Q4. Why put template definitions in headers?**  
The compiler generally needs the definition visible where an implicit instantiation is required.

**Q5. What are STL containers?**  
Standard library types such as vector, map, set and queue that store data and manage their own resources.

**Q6. What is an iterator?**  
An object that provides a standardized way to traverse a range and interact with algorithms.

**Q7. vector vs map?**  
vector stores a sequence with contiguous elements and efficient indexed access; map stores ordered key-value pairs and provides logarithmic tree-based lookup/insertion/erasure.

**Q8. map vs unordered_map?**  
map keeps keys ordered and generally offers logarithmic operations. unordered_map uses hashing and offers average constant-time lookup, though worst-case complexity can be linear.

**Q9. Does a template guarantee code reuse without cost?**  
No. Instantiations may increase code size and compile time; use templates when generic type-safe code is valuable.

**Q10. Why should algorithms receive iterator ranges?**  
It decouples algorithms from specific container types and lets them operate on many compatible sequence/range types.
