"""Python is an object-oriented programming language.
Object-oriented programming (OOP) allows us to model real-world entities as objects.
Objects have attributes (data) and methods (functions) to operate on the data.
OOP concepts include encapsulation, inheritance, and operator overloading.

Encapsulation
Encapsulation refers to the bundling of data (attributes) and methods together within a class.
Encapsulation hides the internal implementation details and provides a public interface
to interact with the object.
"""
class Car:
    def __init__(self, make, model):
      self.__make = make
      self.__model = model

    def get_make(self):
      return self.__make
    
    def get_model(self):
      return self.__model

    def start_engine(self):
       return "Ready to go!"

# instantiate a car object
my_car = Car("Mercedes", "cls 500")

# Accessing attributes using methods (encapsulation)
print(my_car.get_make())  # Output: "Toyota"
print(my_car.get_model())  # Output: "Corolla"

# Cannot directly access private attributes
print(my_car.__make)  # Raises an AttributeError