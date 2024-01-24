class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
# Creating instances of Rectangle and Circle
rectangle = Rectangle(4, 5)  # length and breadth of the rectangle
circle = Circle(3)  # radius of the circle

# Calling the area methods for each shape
rectangle_area = rectangle.area()
circle_area = circle.area()

# Printing the areas
print(f"Area of the rectangle: {rectangle_area}")
print(f"Area of the circle: {circle_area}")

