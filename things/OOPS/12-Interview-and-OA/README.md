# 12 — Interview and OA Practice

Questions below are representative C++ screening practice. They are not attributed to a specific company unless a dated source is recorded; interview content varies by role, location and year.

## Core interview Q&A
1. Four pillars? Encapsulation, abstraction, inheritance, polymorphism.
2. Is C++ pure OOP? No, it is multi-paradigm.
3. Class vs object? Type definition vs instance.
4. Copy constructor vs assignment? Creates a new object vs changes an existing one.
5. Why initializer lists? Direct initialization; required for const/reference members and members without suitable default constructors.
6. Overloading vs overriding? Different parameter lists vs replacing inherited virtual behaviour.
7. Why virtual destructor? Correct destruction through a base pointer.
8. Pure virtual function? A virtual function declared = 0; makes its class abstract.
9. Diamond problem? Duplicate common base subobjects through multiple paths; virtual inheritance can share the base.
10. Shallow vs deep copy? Copy pointer/address values vs duplicate the owned resource.
11. RAII? Tie resource lifetime to object lifetime.
12. What does std::move do? Casts to an xvalue to enable move-overload selection.
13. Object slicing? Copying derived into a base object by value loses derived-specific state.
14. Can constructors be virtual? No.
15. Can return type alone overload a function? No.
16. Can a static member function be virtual? No.
17. What does override do? Lets the compiler verify the function overrides a base virtual.
18. What is an abstract class? A class with an unimplemented pure virtual final overrider.
19. What is unique_ptr? Exclusive-ownership smart pointer.
20. What is stack unwinding? Destruction of automatic objects as exceptions propagate.

## Output tracing A — virtual dispatch
    #include <iostream>
    struct B { virtual void f(){std::cout<<"B";} virtual ~B()=default; };
    struct D:B { void f() override {std::cout<<"D";} };
    int main(){ D d; B& r=d; r.f(); }
Answer: D.

## Output tracing B — non-virtual call
    #include <iostream>
    struct B { void f(){std::cout<<"B";} };
    struct D:B { void f(){std::cout<<"D";} };
    int main(){ D d; B* p=&d; p->f(); }
Answer: B; the function is non-virtual.

## Output tracing C — construction/destruction order
    #include <iostream>
    struct A { A(){std::cout<<"A+";} ~A(){std::cout<<"A-";} };
    struct B { B(){std::cout<<"B+";} ~B(){std::cout<<"B-";} };
    struct C { A a; B b; C(){std::cout<<"C+";} ~C(){std::cout<<"C-";} };
    int main(){ C c; }
Answer: A+B+C+C-B-A-.

## Output tracing D — overload resolution
    #include <iostream>
    void f(int){std::cout<<"int";}
    void f(double){std::cout<<"double";}
    int main(){f(5);}
Answer: int.

## OA-style MCQs
1. Runtime dispatch through a base pointer? Virtual function.
2. Default inheritance for class D : Base? Private.
3. Default inheritance for struct D : Base? Public.
4. Which cannot be overloaded: +, [], ::, <<? The scope resolution operator ::.
5. Exclusive-ownership smart pointer? std::unique_ptr.
6. Can return type alone distinguish overloads? No.
7. What does std::move guarantee? An xvalue cast enabling move overload selection; it does not itself move.
8. Is virtual inheritance the same as a virtual function? No.
9. Why catch exceptions by const reference? Avoid copying and preserve dynamic type.
10. What should a polymorphic base have if deleted through a base pointer? A virtual destructor.

## Coding practice
1. Build a Student class with private roll number, validation and const getters.
2. Implement Complex with operator+ and operator<<.
3. Create abstract Shape, then Circle and Rectangle.
4. Demonstrate single, multilevel and multiple inheritance.
5. Show a diamond hierarchy with and without virtual inheritance.
6. Demonstrate copy construction vs copy assignment.
7. Write a custom exception and catch by const reference.
8. Implement a function template maximum.
9. Demonstrate object slicing and fix it using a base reference.
10. Replace raw owning pointers with std::unique_ptr.

## Company-specific research template
| Company/role | Date | Round | Exact question | Evidence URL |
|---|---|---|---|---|
| To be researched | — | OA/technical | — | Add a reliable public interview-experience source |

## Interview answer framework
Use definition → why it matters → short example → caveat. For virtual functions, define dynamic dispatch, explain base pointer/reference usage, and mention virtual destructors when deleting through a base pointer.
