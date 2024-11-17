
from cell import Cell
from constants import Constants
from coordinate import Coordinate

# Оголошує клас Prey, який успадковується від класу Cell. Це означає, що Prey має всі властивості та методи класу Cell,
# а також може мати свої власні.


class Prey(Cell):
    def __init__(self, owner, offset, time_to_reproduce=Constants.TIME_TO_REPRODUCE,
                 default_num_prey_image=Constants.DEFAULT_NUM_PREY_IMAGE):
        # Валідація owner (має бути об'єктом, який підтримує get_cells())
        if not hasattr(owner, 'get_cells'):
            raise ValueError(f"Owner must have 'get_cells' method. Given: {type(owner)}")

        # Валідація offset (має бути об'єктом Coordinate)
        if not isinstance(offset, Coordinate):
            raise ValueError(f"Offset must be of type 'Coordinate'. Given: {type(offset)}")

        # Валідація time_to_reproduce (має бути позитивним числом)
        if not isinstance(time_to_reproduce, int) or time_to_reproduce <= 0:
            raise ValueError(f"time_to_reproduce must be a positive integer. Given: {time_to_reproduce}")

        # Валідація default_num_pred_image (наприклад, має бути рядком)
        if not isinstance(default_num_prey_image, str):
            raise ValueError(f"default_num_prey_image must be a string. Given: {type(default_num_prey_image)}")

        super().__init__(owner, offset, default_num_prey_image)
        self.time_to_reproduce = time_to_reproduce
        # Викликає конструктор батьківського класу Cell, передаючи координати offset і зображення для здобичі
        super().__init__(owner, offset, default_num_prey_image)
        # вказує, скільки ходів ще залишилося до розмноження здобичі
        self.time_to_reproduce = time_to_reproduce

    #  визначає поведінку здобичі
    def process(self, time_to_reproduce=Constants.TIME_TO_REPRODUCE):
        # Викликає метод get_empty_neighbor_coord, щоб знайти координати порожньої сусідньої клітини
        empty_coord = self.get_empty_neighbor_coord()
        # Перевіряє, чи координати порожньої клітини відрізняються від поточних координат здобичі.
        if empty_coord != self.offset:
            # Якщо порожня клітина знайдена, викликає метод move_from, щоб перемістити здобич до цих координат.
            self.move_from(self.offset, empty_coord)

        # Зменшує лічильник time_to_reproduce на одиницю, що означає, що пройшов ще один хід.
        self.time_to_reproduce -= 1
        # Перевіряє, чи настав час для розмноження
        if self.time_to_reproduce <= 0:
            # Якщо настав час для розмноження, скидає лічильник
            self.time_to_reproduce = time_to_reproduce
            # Шукає нові координати для розмноження
            new_offset = self.get_empty_neighbor_coord()
            # Перевіряє, чи були знайдені порожні координати
            if new_offset != self.offset:
                if self.owner[new_offset.y, new_offset.x].get_image() != Constants.DEFAULT_IMAGE:
                    raise ValueError(f"Cannot reproduce at {new_offset}. The cell is not empty.")

                # Якщо порожня клітина знайдена, викликає метод reproduce для створення нового об'єкта Prey
                self.owner.get_cells()[new_offset.y][new_offset.x] = self.reproduce(new_offset)

    # Створює нову жертву у вказаному місці.
    def reproduce(self, an_offset):
        # Валідація: перевіряємо, що клітина порожня
        if self.owner[an_offset.y, an_offset.x].get_image() != Constants.DEFAULT_IMAGE:
            raise ValueError(f"Cannot reproduce at {an_offset}. The cell is not empty.")

        return Prey(self.owner, an_offset)
