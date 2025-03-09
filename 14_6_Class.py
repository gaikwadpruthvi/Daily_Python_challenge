# Implement a recursive Fibonacci function.

class Car:
    def __init__(self, brand, speed=0):
        """Initialize car with brand and speed."""
        self.brand = brand
        self.speed = speed

    def accelerate(self, increase):
        """Increase the speed of the car."""
        if increase > 0:
            self.speed += increase
            print(f"{self.brand} accelerated by {increase} km/h. Current speed: {self.speed} km/h")
        else:
            print("Increase value must be positive.")


if __name__ == "__main__":
    brand = input("Enter car brand: ")
    car = Car(brand)

    while True:
        try:
            increase = int(input(f"Enter speed increase for {car.brand} (or -1 to exit): "))
            if increase == -1:
                print("Thanks")

                break
            car.accelerate(increase)
        except ValueError:
            print("Invalid input! Please enter an integer.")
