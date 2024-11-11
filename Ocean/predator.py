
from cell import Cell
from constants import Constants

# клас Predator, який успадковується від класу Cell. Це означає, що Predator має всі властивості та методи Cell,
# а також може мати додаткові функціональності.


class Predator(Cell):
    def __init__(self, owner, offset, time_to_reproduce=Constants.TIME_TO_REPRODUCE,
                 default_num_pred_image=Constants.DEFAULT_NUM_PRED_IMAGE):
        # Викликає конструктор батьківського класу Cell, передаючи координати і зображення за замовчуванням для хижака
        super().__init__(owner, offset, default_num_pred_image)
        # вказує, скільки ходів ще залишилося до розмноження хижака
        self.time_to_reproduce = time_to_reproduce

    def process(self, time_to_reproduce=Constants.TIME_TO_REPRODUCE):  # керує рухом (до здобичі чи порожніх місць) і логікою розмноження хижаків.
        # Викликає метод get_prey_neighbor_coord, щоб отримати координати сусідньої клітини, що містить здобич
        prey_coord = self.get_prey_neighbor_coord()
        # Перевіряє, чи були знайдені координати здобичі.
        if prey_coord:
            # Якщо здобич знайдена, викликає метод move_from, щоб перемістити хижака до координат
            self.move_from(self.offset, prey_coord)
            # Зменшує кількість здобичі в океані на одиницю
            self.owner.num_prey -= 1
        # якщо здобич не знайдена
        else:
            # Викликає метод get_empty_neighbor_coord, щоб знайти координати порожньої сусідньої клітини
            empty_coord = self.get_empty_neighbor_coord()
            # Перевіряє, чи координати порожньої клітини відрізняються від поточних координат хижака.
            if empty_coord != self.offset:
                # Якщо координати порожньої клітини відрізняються, хижак переміщується до цієї клітини.
                self.move_from(self.offset, empty_coord)

        # Зменшує лічильник time_to_reproduce на одиницю, вказуючи, що пройшов один хід
        self.time_to_reproduce -= 1
        # Перевіряє, чи настав час для розмноження
        if self.time_to_reproduce <= 0:
            # Якщо настав час для розмноження, скидає лічильник.
            self.time_to_reproduce = time_to_reproduce
            # Шукає нові координати, викликаючи метод get_empty_neighbor_coord і зберігаючи їх у змінній new_offset.
            new_offset = self.get_empty_neighbor_coord()
            # Перевіряє, чи були знайдені порожні координати для нової клітини.
            if new_offset != self.offset:
                # Якщо порожня клітина знайдена, викликає метод reproduce для створення нового об'єкта, призначає його в океані.
                self.owner.get_cells()[new_offset.y][new_offset.x] = self.reproduce(new_offset)

    # Оголошує метод reproduce, який приймає координати an_offset для нової хижаківської клітини.
    def reproduce(self, an_offset):  # створює нову сутність хижака у вказаному місці.
        # Створює новий об'єкт Predator в зазначених координатах і повертає його
        return Predator(self.owner, an_offset)
