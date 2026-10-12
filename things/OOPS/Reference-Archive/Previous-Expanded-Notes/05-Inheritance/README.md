# Unit 05 — Inheritance

**Goal:** Understand base and derived classes, inheritance types, access rules, ambiguity, the diamond problem and safe substitutability.

## 1. What inheritance means

Inheritance creates a new class from one or more existing classes. A base class defines common state or behaviour; a derived class may extend it or provide a specialized implementation.

```cpp
#include <iostream>
#include <string>
#include <utility>
#include <string>

class Animal {
public:
    explicit Animal(std::string name) : name(std::move(name)) {}
    virtual void speak() const {
        std::cout << name << " makes a sound\n";
    }
    virtual ~Animal() = default;
protected:
    std::string name;
};

class Dog : public Animal {
public:
    using Animal::Animal;
    void speak() const override {
        std::cout << name << " barks\n";
    }
};

int main() {
    Animal a("Animal");
    Dog d("Bruno");
    a.speak();
    d.speak();
}
```

**Output**
```text
Animal makes a sound
Bruno barks
```

Dog inherits the public interface and overrides speak(). Public inheritance should express an is-a relationship: a Dog can be treated as an Animal when it obeys the Animal contract.

## 2. Types of inheritance

- **Single:** one direct base class.
- **Multilevel:** class C derives from B, and B derives from A.
- **Multiple:** a class derives directly from more than one base.
- **Hierarchical:** several classes derive from one base.
- **Hybrid:** a combination of these structures.

These names describe hierarchy shape rather than different language mechanisms.

## 3. public, protected and private inheritance

Access mode controls how inherited public/protected members are exposed through the derived class.

| Base member | public inheritance | protected inheritance | private inheritance |
|---|---|---|---|
| public | public | protected | private |
| protected | protected | protected | private |
| private | not directly accessible | not directly accessible | not directly accessible |

Default mode is private for class and public for struct. A private base member remains part of the base subobject, but derived code cannot directly name it.

## 4. Constructor and destructor order

When a Derived object is constructed, its virtual bases are constructed first, then direct bases, then data members in declaration order, then the constructor body. Destruction reverses that sequence. The derived class must not assume base initialization has already happened before it starts.

Also remember: virtual calls during a base constructor/destructor do not dispatch into derived overrides for parts not yet constructed or already destroyed.

## 5. Function hiding and ambiguity

A derived declaration with a given name can hide overloads of that name from the base during name lookup. Use using Base::functionName when the base overload set should remain visible.

Multiple inheritance can create ambiguity when two bases contribute a member with the same name:
```cpp
#include <iostream>
struct Printer { void run() { std::cout << "print\n"; } };
struct Scanner { void run() { std::cout << "scan\n"; } };
struct Machine : Printer, Scanner {};

int main() {
    Machine m;
    m.Printer::run();
    m.Scanner::run();
    // m.run(); // ambiguous: both bases provide run()
}
```

**Output**
```text
print
scan
```

Qualified names resolve this particular lookup ambiguity. This is different from the diamond problem, where duplicate base subobjects may also exist.

## 6. The diamond problem and virtual inheritance

If B and C both inherit from A, and D inherits from both B and C, D may contain two A subobjects. Virtual inheritance tells C++ that the shared virtual base should appear once in the most-derived object.

```cpp
#include <iostream>

struct Person {
    int id = 0;
};
struct Student : virtual Person {};
struct Employee : virtual Person {};
struct TeachingAssistant : Student, Employee {};

int main() {
    TeachingAssistant ta;
    ta.id = 42;
    std::cout << ta.id << '\n';
}
```

**Output**
```text
42
```

Without virtual inheritance, ta.id would be ambiguous because two Person subobjects would exist. Virtual inheritance and virtual functions solve different problems: one affects base-subobject sharing; the other affects function dispatch.

## 7. When should inheritance be used?

Ask three questions:
1. Is the derived type genuinely a subtype, not merely a convenient place to reuse code?
2. Can every derived object safely honour the base class's promises?
3. Would composition be simpler and less coupled?

If a Square derives from Rectangle but permits callers to set width and height independently, it can violate expected Rectangle behaviour. This is a classic substitutability design warning, not just syntax trivia.

## 8. Practical challenge — University Roles (intermediate/tough)

### Problem statement
Build a small university role model:
- Person stores a name and has a virtual describe() method.
- Student adds a roll number.
- Employee adds an employee ID.
- TeachingAssistant is both a Student and an Employee.
- Make the shared Person base virtual so TeachingAssistant contains one Person.
- Store references/pointers to different people and call describe() polymorphically.
- Ensure deletion through a base pointer is safe.

### Worked solution
```cpp
#include <iostream>
#include <memory>
#include <string>
#include <vector>

class Person {
protected:
    std::string name;
public:
    explicit Person(std::string n) : name(std::move(n)) {}
    virtual void describe() const {
        std::cout << "Person: " << name << '\n';
    }
    virtual ~Person() = default;
};

class Student : virtual public Person {
protected:
    int roll;
public:
    Student(std::string n, int r) : Person(std::move(n)), roll(r) {}
    void describe() const override {
        std::cout << "Student: " << name << ", roll " << roll << '\n';
    }
};

class Employee : virtual public Person {
protected:
    int employeeId;
public:
    Employee(std::string n, int id)
        : Person(std::move(n)), employeeId(id) {}
    void describe() const override {
        std::cout << "Employee: " << name << ", id " << employeeId << '\n';
    }
};

class TeachingAssistant : public Student, public Employee {
public:
    TeachingAssistant(std::string n, int r, int id)
        : Person(n), Student(n, r), Employee(n, id) {}

    void describe() const override {
        std::cout << "Teaching assistant: " << name
                  << ", roll " << roll
                  << ", employee id " << employeeId << '\n';
    }
};

int main() {
    std::vector<std::unique_ptr<Person>> people;
    people.push_back(std::make_unique<Student>("Asha", 11));
    people.push_back(std::make_unique<Employee>("Dev", 71));
    people.push_back(std::make_unique<TeachingAssistant>("Mira", 21, 81));

    for (const auto& person : people) person->describe();
}
```

**Output**
```text
Student: Asha, roll 11
Employee: Dev, id 71
Teaching assistant: Mira, roll 21, employee id 81
```

### Why the solution works
- Student and Employee virtually inherit Person, so TeachingAssistant has one shared Person base.
- TeachingAssistant initializes the virtual base Person; the most-derived class is responsible for that initialization.
- describe() is virtual, so each concrete type supplies its own behaviour.
- unique_ptr<Person> preserves dynamic type and owns each object.
- Person's virtual destructor permits safe destruction through a Person pointer.

**Stretch task:** add a ResearchAssistant subtype and decide whether it should inherit Student, Employee or both. Explain the domain relationship before implementing it.

## 9. End-of-unit interview questions with answers

**Q1. What is inheritance?**  
A mechanism to derive a class from one or more base classes to reuse/extend interfaces and model valid subtype relationships.

**Q2. What is the difference between public, protected and private inheritance?**  
They determine the visibility of inherited public/protected members in the derived class. Public inheritance keeps public base members public; protected makes them protected; private makes them private.

**Q3. Does a derived class directly access private base members?**  
No. The base subobject contains that state, but direct access is prohibited. Use accessible base operations.

**Q4. Explain the diamond problem.**  
Two inheritance paths lead to the same base, potentially creating two base subobjects and ambiguous member access. Virtual inheritance shares the common virtual base.

**Q5. Is virtual inheritance the same as a virtual function?**  
No. Virtual inheritance controls shared base-subobject structure; virtual functions enable runtime dispatch.

**Q6. Why should a polymorphic base destructor be virtual?**  
To ensure destruction through a base pointer invokes the derived destructor chain correctly.

**Q7. What does override do?**  
It asks the compiler to verify that a derived member function really overrides a virtual base function. It catches accidental signature mismatches.

**Q8. What is object slicing?**  
Copying a derived object by value into a base object discards the derived-specific portion. References and pointers preserve polymorphic identity.

**Q9. What is the difference between hiding and overriding?**  
Overriding replaces a virtual function's behaviour for dynamic dispatch. Hiding is a name-lookup effect where a derived declaration hides base names/overloads.

**Q10. When is inheritance a bad choice?**  
When the relationship is has-a/uses-a, when the derived class cannot honour the base contract, or when it is used only to share implementation. Composition is often more flexible.
