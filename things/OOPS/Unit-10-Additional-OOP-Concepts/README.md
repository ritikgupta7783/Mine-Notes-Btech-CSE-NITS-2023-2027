# Unit 10 — Additional OOP Concepts and C++ Project Structure

**Prerequisite:** Units 0–9. This unit collects concepts that are useful after classes, access control, constructors, encapsulation, inheritance and polymorphism are understood.
**Estimated time:** 3–5 hours across the linked lessons.

Do not try to memorise every advanced feature at once. Read each short lesson, run its example, and return when a project needs that feature.

## Learning path

1. [this, static members, const functions and friend](01-this-static-const-friend.md)
2. [Association, aggregation and composition](02-object-relationships.md)
3. [Copying, destructors, dynamic memory, RAII and smart pointers](03-copy-memory-raii.md)
4. [Exception handling](04-exceptions.md)
5. [Templates, namespaces, header files and source files](05-templates-namespaces-headers.md)

## What should feel familiar already?
You have already created objects and called member functions. You know that private data protects class rules, constructors initialize objects, inheritance connects related types, and virtual functions enable dynamic behaviour. This unit adds tools for writing maintainable and resource-safe C++ programs.

## Practical challenge — Employee Payroll Assembly

At the end of this unit, build a small payroll program by combining:
- an Employee class that validates its own monthly salary;
- a static counter for the number of employees created;
- a const print function;
- a Department class that contains employees or refers to them according to a clearly stated ownership model;
- an exception for invalid salary input;
- a template helper that prints a collection count or generic value.

A guided solution is included in [Project 8: Multi-class Payroll System](../Unit-11-Practical-Projects/08-Multi-Class-Payroll-System/README.md).

## Quick revision
- this refers to the current object in a non-static member function.
- static data belongs to the class, not each instance.
- const member functions are useful for reading state.
- friend grants special access and should be used deliberately.
- composition represents has-a; association represents a connection.
- RAII and smart pointers make resource ownership safer.
- exceptions report failures; templates enable generic code.
- namespaces avoid name clashes; headers expose declarations to other files.

## Connection to Unit 11
These features become easier to understand when used together. The next unit turns them into complete projects with requirements, class designs, compilable code, expected output, tests and extensions.

---
[← Previous: Unit 9](../Unit-09-Polymorphism/README.md) · [Course home](../README.md) · [Next: Unit 11 — Projects →](../Unit-11-Practical-Projects/README.md)
