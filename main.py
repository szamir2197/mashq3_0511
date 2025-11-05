class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        return self.width * self.height

    @area.setter
    def area(self, new_area):
        self.height = new_area / self.width


r = Rectangle(10, 5)
print(r.area)  
r.area = 100
print(r.height) 
