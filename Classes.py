class Point:
    default_colour = "red"

    @classmethod
    def zero(cls):
        return cls(0, 0)  # it is equal to call Point(0, 0)

    def __init__(self, x, y) -> None:
        self.x = x

        self.y = y

    def draw(self):
        print(f"{self.x, self.y}")

    def __str__(self):
        return f"{self.x, self.y}"

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __add__(self, __o: object):
        return Point(self.x + __o.x, self.y + __o.y)


point1 = Point(1, 2)

point1.draw()

print(point1.default_colour)  # using instance references

print(Point.default_colour)  # using class references

point2 = Point.zero()  # call the class methode

print(point2)  # it is calling point2.__self__ methode

point3 = Point(1, 2)

print(point1 == point3)

print(point1 + point3)

print("create tag class")


class TagCloud:

    def __init__(self) -> None:
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)  # it is for iterater thorought for loop


cloud = TagCloud()

cloud["python"] = 10
print(len(cloud))

cloud.add("python")

cloud.add("Python")

cloud.add("python")


# print(cloud.__tags) #canot accessible outside because it is private


# class Product:
#     def __init__(self, price):
#         self.price = price
#
#     @property
#     def price(self):
#         return self.price
#
#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("value cannot be negative")
#         self.price = value
#
#
# product = Product(10)
# print(product.price())

class Animal(object):
    def __init__(self):
        age = 1

    def eat(self):
        return "eating"


class Mammal(Animal):

    def walk(self):
        return "walking"


class Fish(Animal):

    def swim(self):
        return "swiming"


class Bird(Animal):

    def fly(self):
        return "flying"


m = Mammal()
print(isinstance(m, Animal))
print(issubclass(Fish, Animal))

from collections import namedtuple

Point = namedtuple("Point", ["x", "y"]);

p1 = Point(x=121, y=123)
p2 = Point(x=121, y=123)
print(f"namedtuple instances p1 and p2 are equal is {p1 == p2}.")
