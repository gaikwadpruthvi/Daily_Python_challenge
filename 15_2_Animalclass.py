# Build an Animal base class with Dog and Cat subclasses.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return "Some generic sound"

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Dog")
        self.breed = breed

    def make_sound(self):
        return "Woof! Woof!"

    def fetch(self):
        return f"{self.name} is fetching the ball."

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Cat")
        self.color = color

    def make_sound(self):
        return "Meow! Meow!"

    def climb(self):
        return f"{self.name} is climbing the tree."

# User input
animal_type = input("Enter animal type (Dog/Cat): ").strip().lower()
name = input("Enter the animal's name: ")

if animal_type == "dog":
    breed = input("Enter the dog's breed: ")
    pet = Dog(name, breed)
elif animal_type == "cat":
    color = input("Enter the cat's color: ")
    pet = Cat(name, color)
else:
    print("Invalid animal type!")
    exit()

print(pet)
print("Sound:", pet.make_sound())
if isinstance(pet, Dog):
    print(pet.fetch())
elif isinstance(pet, Cat):
    print(pet.climb())
