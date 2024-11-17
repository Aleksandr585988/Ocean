
import random
from cell import Cell
from constants import Constants
from coordinate import Coordinate
from user import User
from predator import Predator
from prey import Prey
from obstacle import Obstacle


class Ocean(User):
    def __init__(self, max_rows=Constants.MAX_ROWS, max_cols=Constants.MAX_COLS,):
        self.num_rows = max_rows  # кількість рядків в океан
        self.num_cols = max_cols  # кількість стовпців в океані
        self.size = self.num_rows * self.num_cols  # обчислює загальну кількість клітин в океані, множе іх

        super().__init__(self.size, self.num_cols)

        self.__cells = []  # Ініціалізація списку клітин океану
        self.init_cells()

    def validation_index(self, row, col):
        if not (0 <= row < self.num_rows):
            raise IndexError(f"Row index {row} is out of bounds (0-{self.num_rows - 1})")
        if not (0 <= col < self.num_cols):
            raise IndexError(f"Column index {col} is out of bounds (0-{self.num_cols - 1})")

    def __getitem__(self, item):
        row, col = item
        self.validation_index(row, col)
        return self.__cells[row][col]

    def __setitem__(self, key, value):
        row, col = key
        self.validation_index(row, col)
        self.__cells[row][col] = value

    # відповідає за призначення клітини
    def assign_cell_at(self, a_coord, a_cell):
        self.validation_index(a_coord.y, a_coord.x)
        # Призначає передану клітину в масив клітин океану за вказаними координатами.
        self[a_coord.y, a_coord.x] = a_cell

    def north(self, cell):
        """Повертає осередок на півдні щодо поточного."""
        row = (cell.offset.y - 1) % self.num_rows
        col = cell.offset.x
        self.validation_index(row, col)  # Проверка индекса после вычисления
        return self[row, col]

    def south(self, cell):
        """Повертає осередок на півдні щодо поточного."""
        row = (cell.offset.y + 1) % self.num_rows
        col = cell.offset.x
        self.validation_index(row, col)  # Проверка индекса после вычисления
        return self[row, col]

    def east(self, cell):
        """Повертає осередок на сході щодо поточного."""
        row = cell.offset.y
        col = (cell.offset.x + 1) % self.num_cols
        self.validation_index(row, col)  # Проверка индекса после вычисления
        return self[row, col]

    def west(self, cell):
        """Повертає комірку на заході щодо поточної."""
        row = cell.offset.y
        col = (cell.offset.x - 1) % self.num_cols
        self.validation_index(row, col)  # Проверка индекса после вычисления
        return self[row, col]

    def init_cells(self):  # Викликає методи ініціалізації комірок
        self.add_empty_cells()
        self.add_obstacles()
        self.add_predators()
        self.add_prey()
        self.display_stats(-1)
        self.display_cells()
        self.display_border()

    def add_empty_cells(self, default_image=Constants.DEFAULT_IMAGE):  # Ініціалізує сітку, заповнену порожніми клітинками
        # Заповнюється сітка клітин об'єктами
        self.__cells = [[Cell(self, Coordinate(col, row), default_image) for col in range(self.num_cols)]
                        for row in range(self.num_rows)]

    # метод додавання об’єктів
    def add_entities(self, entity_class, count):
        # кожна клітина отримуе коордінати тазображення за замовчуванням
        for _ in range(count):
            empty = self.get_empty_cell_coord()
            self.__cells[empty.y][empty.x] = entity_class(self, empty)

    # спеціальні методи додавання відповідних сутностей
    def add_obstacles(self):
        self.add_entities(Obstacle, self.num_obstacles)

    def add_predators(self):
        self.add_entities(Predator, self.num_predators)

    def add_prey(self):
        self.add_entities(Prey, self.num_prey)

    # повертає випадкову координату порожньої комірки
    def get_empty_cell_coord(self, default_image=Constants.DEFAULT_IMAGE):
        while True:
            x = random.randint(0, self.num_cols - 1)
            y = random.randint(0, self.num_rows - 1)
            # як що зображення за замовчуванням
            if self.__cells[y][x].get_image() == default_image:
                # повертае коордінати порожньо клитину ї клітини
                return Coordinate(x, y)

    def get_cells(self):
        return self.__cells

    def display_cells(self):  # відображає поточний стан сітки океану
        for row in self.__cells:
            for cell in row:
                cell.display()
            print()
