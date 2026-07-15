# Smart Device Management System

An Object-Oriented Programming (OOP) mini-project designed to simulate a smart home hub interface. Built in Python.

## Features
- **SmartDevice Parent Class**: Features private encapsulated attributes `device_id` and `power_status`.
- **Child Classes**:
  - `TemperatureSensor`: Features a temperature reading capability.
  - `SecurityCamera`: Allows start/stop recording states.
  - `SmartLight`: Includes validation constraints on brightness (0-100%).
- **Interactive CLI Menu**: A loop-driven command interface simulating real-time system management.

## OOP Principles Demonstrated
1. **Encapsulation**: Protected instance attributes managed carefully using `@property` getters and setters.
2. **Inheritance**: Subclasses leverage the common parent class constructor via `super()`.
3. **Polymorphism**: Overridden `display_info()` methods across child classes.

## How to Run
Ensure you have Python 3 installed. Run the application via terminal:
```bash
python main.py
