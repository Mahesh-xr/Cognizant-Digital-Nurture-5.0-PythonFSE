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
# Additional Design Patterns

## 7. Strategy Pattern

### Purpose

Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.

### Example

```java
interface PaymentStrategy {
    void pay(int amount);
}

class CreditCardPayment implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid ₹" + amount + " using Credit Card");
    }
}

class UPIPayment implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid ₹" + amount + " using UPI");
    }
}

class PaymentContext {
    private PaymentStrategy strategy;

    public PaymentContext(PaymentStrategy strategy) {
        this.strategy = strategy;
    }

    public void executePayment(int amount) {
        strategy.pay(amount);
    }
}
```

### Usage

```java
PaymentContext payment =
        new PaymentContext(new UPIPayment());

payment.executePayment(1000);
```

### Real-World Examples

* Payment Gateway Selection
* Sorting Algorithms
* Route Navigation Systems

---

## 8. Facade Pattern

### Purpose

Provides a simplified interface to a complex subsystem.

### Example

```java
class AudioPlayer {
    void playAudio() {
        System.out.println("Playing Audio");
    }
}

class VideoPlayer {
    void playVideo() {
        System.out.println("Playing Video");
    }
}

class MediaFacade {

    private AudioPlayer audio = new AudioPlayer();
    private VideoPlayer video = new VideoPlayer();

    public void playMedia() {
        audio.playAudio();
        video.playVideo();
    }
}
```

### Usage

```java
MediaFacade media = new MediaFacade();
media.playMedia();
```

### Real-World Examples

* Spring Boot Starter
* Database Utility Classes
* Multimedia Applications

---

# Architecture Patterns

## 9. MVC (Model-View-Controller)

### Components

### Model

* Stores data
* Contains business logic

### View

* Displays data to users
* User Interface

### Controller

* Handles user requests
* Updates Model and View

### Flow

```
User → Controller → Model
                  ↓
                View
```

### Advantages

* Separation of Concerns
* Easy Maintenance
* Better Testing

### Example

```
Student (Model)
StudentView (View)
StudentController (Controller)
```

### Used In

* Spring MVC
* ASP.NET MVC
* Django

---

## 10. MVVM (Model-View-ViewModel)

### Components

### Model

* Business Logic
* Database Operations

### View

* UI Layer

### ViewModel

* Connects View and Model
* Provides Data Binding

### Flow

```
View ↔ ViewModel ↔ Model
```

### Advantages

* Better UI Separation
* Easier Testing
* Supports Data Binding

### Used In

* Android Development
* Jetpack Compose
* WPF
* Flutter (similar architecture)

---

# Design Patterns Covered

| Pattern   | Category      |
| --------- | ------------- |
| Singleton | Creational    |
| Factory   | Creational    |
| Builder   | Creational    |
| Adapter   | Structural    |
| Decorator | Structural    |
| Facade    | Structural    |
| Observer  | Behavioral    |
| Strategy  | Behavioral    |
| MVC       | Architectural |
| MVVM      | Architectural |

---

## Key Takeaways

* Learned commonly used design patterns.
* Understood object creation techniques.
* Learned how to reduce coupling.
* Improved software maintainability.
* Gained knowledge of enterprise application architecture.
* Explored MVC and MVVM design architectures used in modern applications.
