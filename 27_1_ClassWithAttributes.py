#	Create a Vehicle class with attributes for speed, fuel, and mileage.

class Vehicle:
    def __init__(self, speed, fuel, mileage):
        self.speed = speed  # Speed in km/h
        self.fuel = fuel  # Fuel level in liters
        self.mileage = mileage  # Mileage in km/l
    
    def display_info(self):
        print(f"Speed: {self.speed} km/h")
        print(f"Fuel: {self.fuel} liters")
        print(f"Mileage: {self.mileage} km/l")
    
    def calculate_range(self):
        return self.fuel * self.mileage  # Total range in km

# Taking input from the user
speed = float(input("Enter speed (km/h): "))
fuel = float(input("Enter fuel level (liters): "))
mileage = float(input("Enter mileage (km/l): "))

# Creating a Vehicle object
car = Vehicle(speed, fuel, mileage)
car.display_info()

# Calculating and displaying the range
print(f"Estimated range: {car.calculate_range()} km")
