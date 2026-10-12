# 02 — Classes and Objects

## Class syntax
```cpp
class Rectangle {
    double width, height; // private by default
public:
    Rectangle(double w, double h) : width(w), height(h) {}
    double area() const { return width * height; }
};
```
A class may contain data members, member functions, nested types, aliases, static members and friends.

## `class` vs `struct`
Both define class types and support the same capabilities. Defaults differ: members and base inheritance are private for `class`, public for `struct`. A common convention is `struct` for simple public aggregates and `class` for types with invariants.

## Access specifiers
- `public`: part of the caller-facing interface.
- `private`: directly accessible to the class's member functions and friends.
- `protected`: accessible to the class/friends and eligible derived-class contexts.
Access control is a compile-time language rule, not encryption.

## Objects and member access
```cpp
Rectangle r(3, 4);
r.area();        // dot for an object
Rectangle* p=&r;
p->area();       // arrow for a pointer
```
Object size may include padding/alignment; it is not always the sum of member sizes.

## `this` and const members
`this` refers to the object for a non-static member function. It is unavailable in static member functions.
```cpp
class Counter {
    int value;
public:
    explicit Counter(int v) : value(v) {}
    Counter& increment() { ++this->value; return *this; }
    int get() const { return value; }
};
```
A trailing `const` on a member function promises not to modify ordinary non-mutable data through that function.

## Static members
A static data member belongs to the class rather than separately to every object. A static member function has no `this` pointer.
```cpp
class User {
    inline static int created = 0; // C++17
public:
    User() { ++created; }
    static int count() { return created; }
};
```
This counts constructions, not necessarily currently alive objects.

## Friends
A friend function/class receives access to private/protected members. Friendship is not inherited, transitive or automatically reciprocal; use it sparingly.
```cpp
class Box {
    int width;
public:
    explicit Box(int w): width(w) {}
    friend int getWidth(const Box& b) { return b.width; }
};
```

## Interview questions
1. **Can `main()` access a private field directly?** No; use public operations or a friend.
2. **Can a static function be virtual?** No; it is not tied to an object.
3. **Can a const object call a non-const member function?** Generally no.
4. **Why use `explicit`?** To prevent unintended implicit conversions through a constructor.
5. **Can a forward-declared class be an object by value?** Not until its complete definition is available; pointers/references can be declared to an incomplete type.
