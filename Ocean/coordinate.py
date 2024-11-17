
class Coordinate:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value <= 0:
            raise ValueError("x incorrect coordinates")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value <= 0:
            raise ValueError("y incorrect coordinates")
        self.__y = value

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False

    def __repr__(self):
        return f"Coordinate(x={self.x}, y={self.y})"
