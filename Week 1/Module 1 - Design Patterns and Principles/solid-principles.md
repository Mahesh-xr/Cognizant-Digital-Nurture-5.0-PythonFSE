# SOLID Principles in Object-Oriented Programming

## Week 1 Assignment - Cognizant Learning Program

### Overview
SOLID is a collection of five object-oriented design principles that help developers write clean, maintainable, scalable, and flexible software.

---

# S - Single Responsibility Principle (SRP)

## Definition
A class should have only one responsibility and one reason to change.

### ❌ Violation

```java
class Book {
    private String title;
    private String content;

    public void printBook() {
        System.out.println(content);
    }
}
```

The `Book` class handles both book data and printing.

### ✅ Solution

```java
class Book {
    private String title;
    private String content;
}

class BookPrinter {
    public void print(Book book) {
        System.out.println("Printing Book...");
    }
}
```

### Benefits
- Easier maintenance
- Better testing
- Reduced coupling

---

# O - Open/Closed Principle (OCP)

## Definition
Software entities should be open for extension but closed for modification.

### ❌ Violation

```java
class PaymentProcessor {

    public void pay(String type) {
        if(type.equals("CreditCard")) {
            System.out.println("Credit Card Payment");
        } else if(type.equals("UPI")) {
            System.out.println("UPI Payment");
        }
    }
}
```

Adding a new payment method requires modifying existing code.

### ✅ Solution

```java
interface Payment {
    void pay();
}

class CreditCardPayment implements Payment {
    public void pay() {
        System.out.println("Credit Card Payment");
    }
}

class UPIPayment implements Payment {
    public void pay() {
        System.out.println("UPI Payment");
    }
}
```

### Benefits
- Easy to add new features
- Reduces risk of bugs

---

# L - Liskov Substitution Principle (LSP)

## Definition
Subclasses should be replaceable for their parent classes without affecting program behavior.

### ❌ Violation

```java
class Bird {
    void fly() {
        System.out.println("Flying");
    }
}

class Penguin extends Bird {
    @Override
    void fly() {
        throw new UnsupportedOperationException();
    }
}
```

Penguins cannot fly.

### ✅ Solution

```java
interface Bird {}

interface FlyingBird extends Bird {
    void fly();
}

class Sparrow implements FlyingBird {
    public void fly() {
        System.out.println("Flying");
    }
}

class Penguin implements Bird {
}
```

### Benefits
- Reliable inheritance
- Predictable behavior

---

# I - Interface Segregation Principle (ISP)

## Definition
Clients should not be forced to implement methods they do not use.

### ❌ Violation

```java
interface Worker {
    void work();
    void eat();
}

class Robot implements Worker {

    public void work() {
        System.out.println("Working");
    }

    public void eat() {
        throw new UnsupportedOperationException();
    }
}
```

Robots don't eat.

### ✅ Solution

```java
interface Workable {
    void work();
}

interface Eatable {
    void eat();
}

class Human implements Workable, Eatable {

    public void work() {
        System.out.println("Working");
    }

    public void eat() {
        System.out.println("Eating");
    }
}

class Robot implements Workable {

    public void work() {
        System.out.println("Working");
    }
}
```

### Benefits
- Cleaner interfaces
- Easier implementation

---

# D - Dependency Inversion Principle (DIP)

## Definition
High-level modules should depend on abstractions, not concrete implementations.

### ❌ Violation

```java
class Keyboard {
}

class Computer {

    private Keyboard keyboard = new Keyboard();
}
```

Computer is tightly coupled with Keyboard.

### ✅ Solution

```java
interface Keyboard {
}

class MechanicalKeyboard implements Keyboard {
}

class Computer {

    private Keyboard keyboard;

    public Computer(Keyboard keyboard) {
        this.keyboard = keyboard;
    }
}
```

### Benefits
- Loose coupling
- Easier testing
- Better scalability

---

# Summary Table

| Principle | Description |
|------------|------------|
| SRP | One class, one responsibility |
| OCP | Open for extension, closed for modification |
| LSP | Subclasses should replace parent classes safely |
| ISP | Don't force unnecessary methods |
| DIP | Depend on abstractions, not implementations |

---

# Why SOLID Matters

Following SOLID principles helps developers:

- Write clean code
- Reduce bugs
- Improve maintainability
- Increase scalability
- Simplify testing
- Build enterprise-level applications

---


## Reference

Baeldung - SOLID Principles Guide :contentReference[oaicite:0]{index=0}