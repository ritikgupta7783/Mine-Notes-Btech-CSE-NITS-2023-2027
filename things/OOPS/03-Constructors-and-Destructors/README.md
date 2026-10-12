# 03 — Constructors and Destructors

## Constructors
A constructor initializes a new object and helps establish its invariants. It has the class name and no return type. Common forms are default, parameterized, copy (T(const T&)), move (T(T&&)) and converting constructors. Mark single-argument constructors explicit when implicit conversion is not intended.

A default constructor is not always generated or available; declaring other constructors can affect implicit generation.

## Member initializer lists
    #include <string>
    #include <utility>
    class Student {
        const int roll;
        std::string name;
    public:
        Student(int r, std::string n) : roll(r), name(std::move(n)) {}
    };

Members initialize in declaration order, not the order written in the initializer list. Initializer lists are required for references, const members and members without a suitable default constructor.

## Copy and move semantics
A copy constructor initializes a new object from another. A move constructor can transfer resources from an expiring object. std::move(x) is a cast enabling move-overload selection; it does not itself transfer resources.
    struct Label {
        std::string text;
        explicit Label(std::string s): text(std::move(s)) {}
        Label(const Label& x): text(x.text) { std::cout << "copy\n"; }
        Label(Label&& x) noexcept: text(std::move(x.text)) { std::cout << "move\n"; }
    };

## Destructor and order
A destructor (~Type) releases resources when object lifetime ends. Construction order: virtual bases, direct bases, members in declaration order, then constructor body. Destruction reverses this order. If construction throws, already-constructed subobjects are destroyed.

A polymorphic base that permits deletion through a base pointer should have a virtual destructor:
    struct Base { virtual ~Base() = default; };
    struct Derived : Base { ~Derived() override = default; };

## Rule of three, five and zero
- **Rule of three:** destructor, copy constructor and copy assignment.
- **Rule of five:** also consider move constructor and move assignment.
- **Rule of zero:** prefer std::string, std::vector and smart pointers so resource management is delegated to safe members.

## Interview questions
1. Can constructors be virtual? No; the object is not fully constructed yet.
2. Can a destructor be overloaded? No.
3. Copy construction vs assignment? The former creates a new object; the latter changes an existing object.
4. Why initializer lists? Direct initialization and support for const/reference/no-default-constructor members.
5. What is a delegating constructor? One constructor calls another of the same class in its initializer list.
6. Why should destructors not throw? An exception escaping during stack unwinding can terminate the program.
