# classes uses pascal naming convention rather than
# regular python naming convention
class Point:
    def move(self):
        print("move")


    def draw(self):
        print("draw")


point = Point()
point.move()
point.draw()
point.x = 10 # wierd ?? why is this allowed
point.y = 20
print(point.x, point.y)

another_point = Point()

# print(another_point.x, another_point.y) # throws errors, again this is wierd

# create a class
class Room:
    length = 0.0 # called as attributes
    breadth = 0.0

    # method to calculate area
    def calculate_area(self):
        print("Area of Room =", self.length * self.breadth)


# create object of Room class
study_room = Room()

# assign values to all the properties
study_room.length = 42.5
study_room.breadth = 30.8

# access method inside class
study_room.calculate_area()

"""
 Constructor
"""

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f"moved to x: {self.x}, y: {self.y}")


    def draw(self):
        print(f"drawing at coordinates: {self.x}, {self.y}")


point = Point2D(10, 20)
point.move()
point.x = 30
point.draw()


class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print(f"Hello I'm {self.name}")



paul = Person("Paul")
paul.talk()


"""
    To String()
"""

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


p1 = Point(1, 2)
p2 = Point(2, 3)

print(f"Point: {p1}, {p2}")


# Output: (3,5)