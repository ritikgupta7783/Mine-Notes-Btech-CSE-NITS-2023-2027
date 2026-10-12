# 02 — Classes and Objects

## Class syntax
    class Rectangle {
        double width, height; // private by default
    public:
        Rectangle(double w, double h) : width(w), height(h) {}
        double area() const { return width * height; }
    };

A class can contain data members, member functions, nested types, aliases, static members and friends.

## class vs struct
Both define class types and support the same capabilities. Defaults differ: members and base inheritance are private for class, public for struct. A common convention is struct for simple public aggregates and class for types with invariants.

## Access specifiers
- **public:** part of the caller-facing interface.
- **private:** directly accessible to the class's member functions and friends.
- **protected:** accessible to the class/friends and eligible derived-class contexts.

Access control is a compile-time language rule, not encryption.

## Objects and member access
    Rectangle r(3, 4);
    r.area();          // dot for an object
    Rectangle* p = &r;
    p->area();         // arrow for a pointer

Object size may include padding and alignment; it is not always just the sum of member sizes.

## this and const member functions
this refers to the object for a non-static member function and is unavailable in static member functions.
    class Counter {
        int value;
    public:
        explicit Counter(int v) : value(v) {}
        Counter& increment() { ++this->value; return *this; }
        int get() const { return value; }
    };

A trailing const promises that a member function will not modify ordinary non-mutable data through that function.

## Static members
A static data member belongs to the class rather than separately to each object. A static member function has no this pointer. C++17 permits inline static data members.
    class User {
        inline static int created = 0;
    public:
        User() { ++created; }
        static int count() { return created; }
    };

This tracks constructions, not necessarily currently alive objects.

## Friend functions
A friend function/class receives access to private/protected members. Friendship is not inherited, transitive or automatically reciprocal; use it sparingly.
    class Box {
        int width;
    public:
        explicit Box(int w): width(w) {}
        friend int getWidth(const Box& b) { return b.width; }
    };

## Interview questions
1. **Can main access a private field directly?** No; use public operations or a friend.
2. **Can a static function be virtual?** No; it is not tied to a particular object.
3. **Can a const object call a non-const member function?** Generally no.
4. **Why use explicit?** To prevent unintended implicit conversions through a constructor.
5. **Can a forward-declared class be an object by value?** Not until its complete definition is available; pointers/references may use an incomplete type.
