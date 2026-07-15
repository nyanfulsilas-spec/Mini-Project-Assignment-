# smart_device_management_system.py
"""
Smart Device Management System
Author: Nyanful Silas Ali
Description: A mini-project demonstrating OOP principles in Python,
including inheritance, encapsulation, validation, and a command-line interface.
"""

# ==========================================
# 1. PARENT CLASS: SmartDevice
# ==========================================
class SmartDevice:
    def __init__(self, device_id: str, name: str):
        # Validate that device ID is not empty during initialization
        if not device_id or not device_id.strip():
            raise ValueError("Device ID cannot be empty.")
        
        # Private attributes (indicated by double underscores)
        self.__device_id = device_id.strip()
        self.__power_status = False  # Default power status is off
        
        # Public attribute
        self.name = name

    # Getter and Setter for device_id
    @property
    def device_id(self) -> str:
        return self.__device_id

    @device_id.setter
    def device_id(self, value: str):
        if not value or not value.strip():
            raise ValueError("Device ID cannot be empty.")
        self.__device_id = value.strip()

    # Getter and Setter for power_status
    @property
    def power_status(self) -> bool:
        return self.__power_status

    @power_status.setter
    def power_status(self, status: bool):
        if not isinstance(status, bool):
            raise TypeError("Power status must be a boolean (True/False).")
        self.__power_status = status

    # Methods to control power status
    def turn_on(self):
        """Turns the device on."""
        self.__power_status = True
        print(f" {self.name} has been turned ON.")

    def turn_off(self):
        """Turns the device off."""
        self.__power_status = False
        print(f"{self.name} has been turned OFF.")

    def display_info(self):
        """Displays common device information."""
        status_str = "ON" if self.__power_status else "OFF"
        print(f"--- Device Info: {self.name} ---")
        print(f"ID: {self.__device_id}")
        print(f"Power Status: {status_str}")


# ==========================================
# 2. CHILD CLASSES
# ==========================================

class TemperatureSensor(SmartDevice):
    def __init__(self, device_id: str, name: str, initial_temp: float = 24.0):
        # Use super() to initialize inherited attributes from parent class
        super().__init__(device_id, name)
        # Private sensor-specific attribute
        self.__temperature = initial_temp

    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, value: float):
        self.__temperature = value

    def read_temperature(self) -> float:
        """Simulates and prints the current temperature reading."""
        print(f"{self.name} reports a temperature of {self.__temperature}°C.")
        return self.__temperature


class SecurityCamera(SmartDevice):
    def __init__(self, device_id: str, name: str):
        super().__init__(device_id, name)
        # Private camera-specific attribute
        self.__recording_status = False

    @property
    def recording_status(self) -> bool:
        return self.__recording_status

    def start_recording(self):
        """Starts video recording if device is powered on."""
        if not self.power_status:
            print(f" Cannot start recording. {self.name} is powered OFF.")
            return
        
        self.__recording_status = True
        print(f" {self.name} has STARTED recording.")

    def stop_recording(self):
        """Stops video recording."""
        self.__recording_status = False
        print(f"{self.name} has STOPPED recording.")

    def display_info(self):
        # Extend parent class display_info
        super().display_info()
        rec_str = "RECORDING" if self.__recording_status else "IDLE"
        print(f"Recording Status: {rec_str}")


class SmartLight(SmartDevice):
    def __init__(self, device_id: str, name: str, initial_brightness: int = 50):
        super().__init__(device_id, name)
        # Brightness validation logic integrated directly
        if not (0 <= initial_brightness <= 100):
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = initial_brightness

    @property
    def brightness(self) -> int:
        return self.__brightness

    @brightness.setter
    def brightness(self, value: int):
        if not (0 <= value <= 100):
            raise ValueError("Brightness must be between 0 and 100.")
        self.__brightness = value

    def increase_brightness(self, amount: int = 10):
        """Increases brightness by a set amount, capping at 100."""
        if not self.power_status:
            print(f"Cannot adjust brightness. {self.name} is powered OFF.")
            return
        
        new_brightness = min(100, self.__brightness + amount)
        self.__brightness = new_brightness
        print(f" {self.name} brightness increased to {self.__brightness}%.")

    def decrease_brightness(self, amount: int = 10):
        """Decreases brightness by a set amount, bottoming out at 0."""
        if not self.power_status:
            print(f"Cannot adjust brightness. {self.name} is powered OFF.")
            return
        
        new_brightness = max(0, self.__brightness - amount)
        self.__brightness = new_brightness
        print(f" {self.name} brightness decreased to {self.__brightness}%.")

    def display_info(self):
        super().display_info()
        print(f"Brightness Level: {self.__brightness}%")


# ==========================================
# 3. INTERFACE AND RUNTIME MENU
# ==========================================

def display_menu():
    print("\n" + "=" * 40)
    print("  SMART DEVICE MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Display Device Information")
    print("2. Turn Device On")
    print("3. Turn Device Off")
    print("4. Read Temperature")
    print("5. Adjust Brightness")
    print("6. Start Recording")
    print("7. Exit")
    print("=" * 40)

def main():
    # Instantiate devices as required by the spec
    try:
        temp_sensor = TemperatureSensor("TEMP-001", "Living Room Sensor", 22.5)
        smart_light = SmartLight("LGT-002", "Bedroom Light", 75)
        security_cam = SecurityCamera("CAM-003", "Front Gate Camera")
    except ValueError as e:
        print(f"Error initializing devices: {e}")
        return

    # List storing all devices for easier index-based menu actions
    devices = [temp_sensor, smart_light, security_cam]

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            print("\n--- Displaying All Devices ---")
            for idx, dev in enumerate(devices, 1):
                print(f"[{idx}] ", end="")
                dev.display_info()
                print("-" * 30)

        elif choice in ["2", "3"]:
            print("\nSelect a device to control:")
            for idx, dev in enumerate(devices, 1):
                print(f"{idx}. {dev.name} ({dev.device_id})")
            
            try:
                idx_choice = int(input("Select device number: ")) - 1
                if 0 <= idx_choice < len(devices):
                    target_device = devices[idx_choice]
                    if choice == "2":
                        target_device.turn_on()
                    else:
                        # If turning off a camera, ensure it stops recording automatically
                        if isinstance(target_device, SecurityCamera) and target_device.recording_status:
                            target_device.stop_recording()
                        target_device.turn_off()
                else:
                    print("Invalid selection.")
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "4":
            # Direct operation on the TemperatureSensor instance
            print(f"\nAccessing {temp_sensor.name}:")
            temp_sensor.read_temperature()

        elif choice == "5":
            print(f"\nAccessing {smart_light.name}:")
            if not smart_light.power_status:
                print("
Smart Light is currently OFF. Turn it ON first.")
                continue
            
            print(f"Current brightness: {smart_light.brightness}%")
            print("1. Increase Brightness")
            print("2. Decrease Brightness")
            print("3. Set Specific Brightness Level")
            
            sub_choice = input("Select an option (1-3): ").strip()
            if sub_choice == "1":
                smart_light.increase_brightness()
            elif sub_choice == "2":
                smart_light.decrease_brightness()
            elif sub_choice == "3":
                try:
                    level = int(input("Enter brightness level (0-100): "))
                    smart_light.brightness = level
                    print(f" {smart_light.name} brightness set to {smart_light.brightness}%.")
                except ValueError as e:
                    print(f"Error: {e}")
            else:
                print("Invalid option.")

        elif choice == "6":
            # Operational validation on SecurityCamera
            print(f"\nAccessing {security_cam.name}:")
            if not security_cam.power_status:
                print("Security Camera is currently OFF. Turn it ON first.")
                continue
                
            print("1. Start Recording")
            print("2. Stop Recording")
            sub_choice = input("Select an option (1-2): ").strip()
            if sub_choice == "1":
                security_cam.start_recording()
            elif sub_choice == "2":
                security_cam.stop_recording()
            else:
                print("Invalid option.")

        elif choice == "7":
            print("\nExiting Smart Device Management System. Goodbye!")
            break
        else:
            print("Invalid entry. Please choose a number from 1 to 7.")

if __name__ == "__main__":
    main()
