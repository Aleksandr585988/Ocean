
from cell import Cell
from constants import Constants


class Obstacle(Cell):
    def __init__(self, owner, coord, constants_obstacle_image=Constants.OBSTACLE_IMAGE):
        super().__init__(owner, coord, constants_obstacle_image)

# super() — це функція, яка дозволяє викликати методи батьківського класу.
# Вона використовується для того, щоб звертатися до методів і атрибутів
# батьківсько