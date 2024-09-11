class Animal:
    # attribute and method of the parent class
    name = ""


    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walk")



class Dog(Animal):


    def __init__(self, name, breed):
        self.breed = breed
        print("calling super class constructor")
        super().__init__(name) # In case of multi level inheritance super refers to immediate parent class
       # Animal.__init__(self, name) # even this works


    def listen(self):
        print(f"Hey {self.name} come here !!!")

    def walk(self): # method overriding
        print("calling super class walk")
        super().walk()  # calling super class methods
        # simple super() doesn't work
        print(f"{self.name} likes to go for a walk!!!")



class Cat(Animal):
   # pass # just to satisfy python compiler which doesn't like empty class

    def __init__(self, name):
        super().__init__(name)


dog = Dog("roku", "labrador")
dog.walk()
dog.listen()

cat = Cat("lilly")
cat.walk()


""" 
    Multilevel Inheritance
"""

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")


class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")


class Bat(Mammal, WingedAnimal):
    pass # just to satisfy python compiler which doesn't like empty class




class SuperClass:

    def super_method(self):
        print("Super Class method called")


# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")


# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")


# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"


"""
    Multiple Inheritance & Method Resolution Order (MRO) in Python
    In this case, the MRO specifies that methods should be inherited
    from the leftmost superclass first, so info() of SuperClass1 is called 
    rather than that of SuperClass2.
"""

class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()

# Output: "Super Class 1 method called"
