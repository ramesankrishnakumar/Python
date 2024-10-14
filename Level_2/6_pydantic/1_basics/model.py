from dataclasses import dataclass

from pydantic import BaseModel, ValidationError


class NormalClass:

    def __init__(self, value1: int, value2: str):
        self.value1 = value1
        self.value2 = value2

# normal class we have to define __repr__ & constructor and other special methods

n = NormalClass(1, "2")
# normal classes does not have this and developer has to implement repr and str
# print(f"str: {str(n)}") # <__main__.NormalClass object at 0x102bd5a10>
# print(f"repr: {repr(n)}") # <__main__.NormalClass object at 0x102bd5a10>

# E.g.

class Point:

    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

# If you don't define a __str__() method for a class,
# then the built-in object implementation calls the __repr__() method instead

point = Point(1, 2)
# print(f"str: {str(point)}") # str: Point(x=1, y=2)
# print(f"repr: {repr(point)}") # repr: Point(x=1, y=2)


@dataclass
class DataPoint:
    x: int
    y: int


dp = DataPoint(1, 2) # default implementation of constructor
# default implementation of repr
# print(f"str: {str(dp)}")  # str: DataPoint(x=1, y=2)
# print(f"repr: {repr(dp)}") # default implementation of repr


# Pydantic class
# provide constructor, implementation of str and repr
# validation, serialization and deserialization and many more on top of regular python classes

class Person(BaseModel):
    first_name: str # field, attribute
    last_name: str
    age: int

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

# require keyword arguments not positional arguments
p = Person(first_name="John", last_name="Doe", age=23)
# p = Person("John", "Doe", 23) # fails


# property never gets printed
# print(str(p)) # first_name='John' last_name='Doe' age=23
# print(repr(p)) # Person(first_name='John', last_name='Doe', age=23)
# print(p.full_name) # John Doe



"""
{   
    'first_name': FieldInfo(annotation=str, required=True),
     'last_name': FieldInfo(annotation=str, required=True), 
     'age': FieldInfo(annotation=int, required=True)
}
"""
# print(p.model_fields)
# print(Person.model_fields) # same response

# try:
## validation happen during the creation of the object
#     person = Person(first_name="John") # throws pydantic_core._pydantic_core.ValidationError
# except ValidationError as e:
#     print(e) # prints all validation errors

p.age = "twenty" # goes through without any issues
print(str(p)) # first_name='John' last_name='Doe' age='twenty'




