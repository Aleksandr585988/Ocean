
class Constants:
    # Визначає максимальні розміри сітки океану.
    MAX_ROWS = 25  # Максимальна кількість рядків
    MAX_COLS = 70  # Максимальна кількість стовбців

    # Встановлює кількість за замовчуванням для перешкод, хижаків, здобичі та ітерацій
    DEFAULT_NUM_OBSTACLES = 75  # Число препятствий
    DEFAULT_NUM_PREDATORS = 20  # Число хищников
    DEFAULT_NUM_PREY = 150  # Число жертв
    DEFAULT_NUM_ITERATION = 1000  # Итерация по умолчанию

    # Визначає зображення за замовчуванням для комірок
    DEFAULT_IMAGE = '-'
    DEFAULT_NUM_PREY_IMAGE = 'f'
    DEFAULT_NUM_PRED_IMAGE = 'S'
    OBSTACLE_IMAGE = '#'

    # Визначає константи часу для живлення та розмноження.
#    TIME_TO_FEED = 6  # Час годувати
    TIME_TO_REPRODUCE = 6  # Час для відтворення
