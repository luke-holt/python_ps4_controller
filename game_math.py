class Hitbox:
    def __init__(self, *vertices):
        self.vertices = vertices


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Add two positions and return a new one
        return Point2D(self.x + other.x, self.y + other.y)

    def __str__(self):
        # Define the textual representation of a Point
        return f"Point(x={self.x}, y={self.y}"
