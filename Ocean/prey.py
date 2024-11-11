
from cell import Cell
from constants import Constants

# Оголошує клас Prey, який успадковується від класу Cell. Це означає, що Prey має всі властивості та методи класу Cell,
# а також може мати свої власні.


class Prey(Cell):
    def __init__(self, owner, offset, time_to_reproduce=Constants.TIME_TO_REPRODUCE,
                 default_num_prey_image=Constants.DEFAULT_NUM_PREY_IMAGE):
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
                # Якщо порожня клітина знайдена, викликає метод reproduce для створення нового об'єкта Prey
                self.owner.get_cells()[new_offset.y][new_offset.x] = self.reproduce(new_offset)

    # Створює нову жертву у вказаному місці.
    def reproduce(self, an_offset):
        return Prey(self.owner, an_offset)
