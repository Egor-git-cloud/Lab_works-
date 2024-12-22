class Circle():
    # radius = 7

    def __init__(self,radius):
        self.radius = radius

    def get_radius(self):
        print(self.radius)

    def set_radius(self, new_radius):
        self.new_radius = new_radius
        self.radius = self.new_radius
        return new_radius
x = Circle(9)
x.get_radius()
x.set_radius(4)
x.get_radius()