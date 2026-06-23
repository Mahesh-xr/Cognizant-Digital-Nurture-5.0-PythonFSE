# Design Patterns in Java


### Overview

Design Patterns are reusable solutions to commonly occurring software design problems. They help developers build applications that are maintainable, scalable, flexible, and easy to understand.

This repository demonstrates the implementation and understanding of the following design patterns:

* Singleton Pattern
* Factory Pattern
* Builder Pattern
* Adapter Pattern
* Decorator Pattern
* Observer Pattern

These patterns are among the most widely used patterns in modern software development. 

---

# Design Pattern Categories

| Category   | Patterns                    |
| ---------- | --------------------------- |
| Creational | Singleton, Factory, Builder |
| Structural | Adapter, Decorator          |
| Behavioral | Observer                    |

---

# 1. Singleton Pattern

## Purpose

Ensures that only one instance of a class exists throughout the application and provides a global access point to it.

## Example

```java
public class Singleton {

    private static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if(instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
```

### Usage

```java
Singleton obj1 = Singleton.getInstance();
Singleton obj2 = Singleton.getInstance();

System.out.println(obj1 == obj2); // true
```

### Use Cases

* Database Connections
* Logger Services
* Configuration Management

---

# 2. Factory Pattern

## Purpose

Creates objects without exposing the object creation logic to the client.

## Example

### Product Interface

```java
interface Vehicle {
    void drive();
}
```

### Concrete Products

```java
class Car implements Vehicle {
    public void drive() {
        System.out.println("Driving Car");
    }
}

class Bike implements Vehicle {
    public void drive() {
        System.out.println("Driving Bike");
    }
}
```

### Factory Class

```java
class VehicleFactory {

    public Vehicle createVehicle(String type) {

        if(type.equalsIgnoreCase("car"))
            return new Car();

        if(type.equalsIgnoreCase("bike"))
            return new Bike();

        return null;
    }
}
```

### Usage

```java
VehicleFactory factory = new VehicleFactory();

Vehicle vehicle = factory.createVehicle("car");
vehicle.drive();
```

### Use Cases

* Payment Gateways
* Notification Systems
* Vehicle Manufacturing Applications

---

# 3. Builder Pattern

## Purpose

Constructs complex objects step-by-step.

## Example

```java
class User {

    private String name;
    private String email;
    private int age;

    private User(Builder builder) {
        this.name = builder.name;
        this.email = builder.email;
        this.age = builder.age;
    }

    public static class Builder {

        private String name;
        private String email;
        private int age;

        public Builder(String name) {
            this.name = name;
        }

        public Builder setEmail(String email) {
            this.email = email;
            return this;
        }

        public Builder setAge(int age) {
            this.age = age;
            return this;
        }

        public User build() {
            return new User(this);
        }
    }
}
```

### Usage

```java
User user = new User.Builder("Mahesh")
                    .setEmail("mahesh@gmail.com")
                    .setAge(20)
                    .build();
```

### Use Cases

* User Profiles
* Configuration Objects
* Immutable Objects

---

# 4. Adapter Pattern

## Purpose

Allows incompatible interfaces to work together.

## Example

### Existing Class

```java
class OldPrinter {

    public void printOld() {
        System.out.println("Old Printer");
    }
}
```

### Target Interface

```java
interface Printer {
    void print();
}
```

### Adapter

```java
class PrinterAdapter implements Printer {

    private OldPrinter oldPrinter;

    public PrinterAdapter(OldPrinter oldPrinter) {
        this.oldPrinter = oldPrinter;
    }

    public void print() {
        oldPrinter.printOld();
    }
}
```

### Usage

```java
Printer printer = new PrinterAdapter(new OldPrinter());
printer.print();
```

### Use Cases

* Third-party APIs
* Legacy System Integration
* Payment Gateway Integration

---

# 5. Decorator Pattern

## Purpose

Adds functionality to objects dynamically without modifying their structure.

## Example

### Component

```java
interface Coffee {
    String getDescription();
}
```

### Concrete Component

```java
class SimpleCoffee implements Coffee {

    public String getDescription() {
        return "Simple Coffee";
    }
}
```

### Decorator

```java
class MilkDecorator implements Coffee {

    private Coffee coffee;

    public MilkDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    public String getDescription() {
        return coffee.getDescription() + " + Milk";
    }
}
```

### Usage

```java
Coffee coffee = new MilkDecorator(new SimpleCoffee());

System.out.println(coffee.getDescription());
```

### Output

```
Simple Coffee + Milk
```

### Use Cases

* Text Formatting
* UI Components
* Food Ordering Systems

---

# 6. Observer Pattern

## Purpose

Defines a one-to-many dependency so that when one object changes state, all dependent objects are notified automatically.

## Example

### Observer Interface

```java
interface Observer {
    void update(String message);
}
```

### Concrete Observer

```java
class User implements Observer {

    private String name;

    public User(String name) {
        this.name = name;
    }

    public void update(String message) {
        System.out.println(name + " received: " + message);
    }
}
```

### Subject

```java
import java.util.*;

class Channel {

    private List<Observer> subscribers = new ArrayList<>();

    public void subscribe(Observer observer) {
        subscribers.add(observer);
    }

    public void notifySubscribers(String message) {

        for(Observer observer : subscribers) {
            observer.update(message);
        }
    }
}
```

### Usage

```java
Channel channel = new Channel();

channel.subscribe(new User("Mahesh"));
channel.subscribe(new User("Kishore"));

channel.notifySubscribers("New Video Uploaded");
```

### Output

```
Mahesh received: New Video Uploaded
Kishore received: New Video Uploaded
```

### Use Cases

* YouTube Notifications
* Stock Market Updates
* Event Handling Systems

---

# Summary

| Pattern   | Type       | Purpose                         |
| --------- | ---------- | ------------------------------- |
| Singleton | Creational | Single instance creation        |
| Factory   | Creational | Object creation abstraction     |
| Builder   | Creational | Step-by-step object creation    |
| Adapter   | Structural | Connect incompatible interfaces |
| Decorator | Structural | Add behavior dynamically        |
| Observer  | Behavioral | Notify dependent objects        |

---

# Key Learnings

* Improved understanding of object-oriented design.
* Learned how to reduce coupling between classes.
* Understood code reusability and scalability.
* Applied industry-standard design patterns.
* Gained knowledge of real-world software architecture concepts.

---

