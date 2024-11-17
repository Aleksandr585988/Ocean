
import random
from constants import Constants


class Cell:
    def __init__(self, owner, offset, image):
        # Валідація owner
        if not hasattr(owner, 'assign_cell_at'):
            raise ValueError('Owner has no assign_cell_at method')

        # Валідація offset (перевірка, що об'єкт має атрибути x і y)
        if not hasattr(offset, 'x') or not hasattr(offset, 'y'):
            raise ValueError('Offset has no x or y method')

        # Валідація image
        if not isinstance(image, str):
            raise ValueError("Image must be a string")

        self.owner = owner
        self.offset = offset
        self.image = image

    def get_offset(self):  # повертає координати клітини
        return self.offset

    def get_image(self):  # повертає зображення клітини
        return self.image

    # Переміщує клітину з одних координат на інші. Якщо нові координати відрізняються від поточних
    def move_from(self, from_coord, to_coord, default_image=Constants.DEFAULT_IMAGE):  # переміщує клітинку до нової координати, якщо вона відрізняється.
        # Валідація координат
        if not hasattr(from_coord, 'x') or not hasattr(from_coord, 'y'):
            raise ValueError("from_coord must have 'x' and 'y' attributes")
        if not hasattr(to_coord, 'x') or not hasattr(to_coord, 'y'):
            raise ValueError("to_coord must have 'x' and 'y' attributes")

        if to_coord != from_coord:  # Перевіряє, чи нові координати to_coord відрізняються від поточних
            self.owner.assign_cell_at(from_coord, Cell(self.owner, from_coord, default_image))  # Якщо координати відрізняються, призначає нову клітину з дефолтним зображенням у старі координати
            self.offset = to_coord  # Оновлює координати клітини на нові
            self.owner.assign_cell_at(to_coord, self)  # Призначає поточну клітину новим координатам

    def direction(self):
        # Перевірка коректності індексів
        if not (0 <= self.offset.y < self.owner.num_rows):
            raise ValueError(f"Y coordinate {self.offset.y} out of bounds")
        if not (0 <= self.offset.x < self.owner.num_cols):
            raise ValueError(f"X coordinate {self.offset.x} out of bounds")

        directions = [
            self.owner[(self.offset.y - 1) % self.owner.num_rows, self.offset.x],  # north
            self.owner[(self.offset.y + 1) % self.owner.num_rows, self.offset.x],  # south
            self.owner[self.offset.y, (self.offset.x + 1) % self.owner.num_cols],  # east
            self.owner[self.offset.y, (self.offset.x - 1) % self.owner.num_cols]  # west
        ]
        return directions

    # Повертає випадкову сусідню клітину
    def get_neighbor_with_image(self, an_image):  # отримує випадкову сусідню комірку з певним зображенням.
        # Фільтрує сусідів і зберігає лише ті, що мають зображення, яке відповідає
        neighbors = [cell for cell in self.direction() if cell.get_image() == an_image]
        # Повертає випадкову сусідню клітину з відповідним зображенням, в іншому випадку повертає саму клітину.
        return random.choice(neighbors) if neighbors else self

    # Шукає порожню сусідню клітину
    def get_empty_neighbor_coord(self, default_image=Constants.DEFAULT_IMAGE):  # знаходить випадкову порожні сусідні клітини.
        # Фільтрує сусідів, зберігаючи лише ті, що порожні.
        empty_neighbors = [cell for cell in self.direction() if cell.get_image() == default_image]
        # Повертає координати випадкової порожньої сусідньої клітини, в іншому випадку повертає координати самої клітини.
        return random.choice(empty_neighbors).get_offset() if empty_neighbors else self.offset

    # Шукає сусідню клітину, яка містить здобич
    def get_prey_neighbor_coord(self, default_num_prey_image=Constants.DEFAULT_NUM_PREY_IMAGE):  # знаходить сусідню клітинку, яка містить здобич.
        # Викликає метод get_neighbor_with_image, передаючи зображення здобичі, і повертає координати знайденої клітини.
        return self.get_neighbor_with_image(default_num_prey_image).get_offset()

    # Виводить зображення клітини на екран
    def display(self):
        # Виводить зображення клітини без переходу на новий рядок (використовується end='', щоб уникнути переходу).
        print(f"{self.image}", end='')

    def process(self):
        pass
