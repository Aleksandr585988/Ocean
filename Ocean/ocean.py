
import random
from constants import Constants
from coordinate import Coordinate


class Ocean:
    def __init__(self, max_rows=Constants.MAX_ROWS, max_cols=Constants.MAX_COLS,
                 default_num_obstacles=Constants.DEFAULT_NUM_OBSTACLES,
                 default_num_predators=Constants.DEFAULT_NUM_PREDATORS,
                 defaylt_num_prey=Constants.DEFAULT_NUM_PREY):
        self.num_rows = max_rows  # кількість рядків в океан
        self.num_cols = max_cols  # кількість стовпців в океані
        self.size = self.num_rows * self.num_cols  # обчислює загальну кількість клітин в океані, множе іх

        # Запитує користувача кількість перешкод.
        self.num_obstacles = self.prompt_for_count("obstacles", default_num_obstacles)
        # хижаків
        self.num_predators = self.prompt_for_count("predators", default_num_predators, self.num_obstacles)
        # здобичі
        self.num_prey = self.prompt_for_count("prey", defaylt_num_prey, self.num_obstacles + self.num_predators)

        self.__cells = []  # Ініціалізація списку клітин океану
        self.init_cells()

    def __getitem__(self, item):
        row, col = item
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            return self.__cells[row][col]
        else:
            raise IndexError

    def __setitem__(self, key, value):
        row, col = key
        if 0 <= row < self.num_rows and 0 <= col < self.num_cols:
            self.__cells[row][col] = value
        else:
            raise IndexError

    # відповідає за призначення клітини
    def assign_cell_at(self, a_coord, a_cell):
        # Призначає передану клітину в масив клітин океану за вказаними координатами.
        self[a_coord.y, a_coord.x] = a_cell

    def north(self, cell):  # повертає сусідні клітинки на північ.
        return self[(cell.offset.y - 1) % self.num_rows, cell.offset.x]

    def south(self, cell):  # повертає сусідні клітинки на південь.
        return self[(cell.offset.y + 1) % self.num_rows, cell.offset.x]

    def east(self, cell):  # повертає сусідні клітинки на схід
        return self[cell.offset.y, (cell.offset.x + 1) % self.num_cols]

    def west(self, cell):  # повертає сусідні клітинки на захід.
        return self[cell.offset.y, (cell.offset.x - 1) % self.num_cols]

    def prompt_for_count(self, name, default, limit=0):  # запитує у користувача кількість об’єктів
        count = int(input(f"\nEnter number of {name}: (Default = {default}): ") or default)
        max_count = self.size - limit  # максимальна кількість об'єктів, що можуть бути розміщені в океані
        return min(count, max_count)  # повертаемо мінімум меіж введенним значенням і дозволеною кількостью

    def init_cells(self):  # Викликає методи ініціалізації комірок
        self.add_empty_cells()
        self.add_obstacles()
        self.add_predators()
        self.add_prey()
        self.display_stats(-1)
        self.display_cells()
        self.display_border()

    def add_empty_cells(self, default_image=Constants.DEFAULT_IMAGE):  # Ініціалізує сітку, заповнену порожніми клітинками
        from cell import Cell
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
        from obstacle import Obstacle
        self.add_entities(Obstacle, self.num_obstacles)

    def add_predators(self):
        from predator import Predator
        self.add_entities(Predator, self.num_predators)

    def add_prey(self):
        from prey import Prey
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

    def display_border(self):  # Відображення кордону океану
        print('*' * self.num_cols)

    def display_cells(self):  # відображає поточний стан сітки океану
        for row in self.__cells:
            for cell in row:
                cell.display()
            print()

    def display_stats(self, iteration):  # відображає поточну статистику
        print(f"\n\nIteration number: {iteration + 1}")
        print(f"Obstacles: {self.num_obstacles}")
        print(f"Predators: {self.num_predators}")
        print(f"Prey: {self.num_prey}")
        self.display_border()

    def run(self, default_num_iteration=Constants.DEFAULT_NUM_ITERATION):  # Основний цикл для запуску симуляції
        num_iterations = int(input("\n\nEnter number of iterations: (default = 1000): ") or 1000)
        num_iterations = min(num_iterations, default_num_iteration)
        print(f"\nNumber of iterations = {num_iterations}\nbegin...\n")

        for iteration in range(num_iterations):
            from prey import Prey
            from predator import Predator
            if self.num_predators > 0 and self.num_prey > 0:
                for row in self.__cells:  # проходить по всіх рядках океану
                    for cell in row:  # проходить по кожній клітинці
                        if isinstance(cell, Predator):
                            cell.process()
                        elif isinstance(cell, Prey):
                            cell.process()
                self.display_stats(iteration)
                self.display_cells()
                self.display_border()
        print("\n\nEnd of Simulation\n")
