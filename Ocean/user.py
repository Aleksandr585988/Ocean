
from constants import Constants


class User:
    def __init__(self, size, num_cols, default_num_obstacles=Constants.DEFAULT_NUM_OBSTACLES,
                 default_num_predators=Constants.DEFAULT_NUM_PREDATORS,
                 default_num_prey=Constants.DEFAULT_NUM_PREY):

        self.num_obstacles = self.prompt_for_count("obstacles", default_num_obstacles)
        self.num_predators = self.prompt_for_count("predators", default_num_predators)
        self.num_prey = self.prompt_for_count("prey", default_num_prey)

        self.num_cols = num_cols
        self.size = size

    def display_border(self):
        print('*' * self.num_cols)

    @staticmethod
    def prompt_for_count(name, default):
        while True:
            try:
                count = input(f"\nEnter number of {name}: (Default = {default}): ")

                # Якщо порожнє значення, використовуємо значення за замовчуванням
                if not count:
                    count = default
                else:
                    # Перетворити введений рядок на ціле число
                    count = int(count)

                # Перевіряємо, щоб значення було в межах допустимого діапазону
                if count <= 0:
                    print("Число не може бути від’ємним..")
                elif count > default:
                    print(f"Invalid number. The maximum possible number of {name}s is {default}.")
                else:
                    return count

            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def display_stats(self, iteration):
        print(f"\n\nIteration number: {iteration + 1}")
        print(f"Obstacles: {self.num_obstacles}")
        print(f"Predators: {self.num_predators}")
        print(f"Prey: {self.num_prey}")
        self.display_border()

    # def prompt_for_count(self, name, default, limit=0):
    #     count = int(input(f"\nEnter number of {name}: (Default = {default}): ") or default)
    #     max_count = self.size - limit
    #     return min(count, max_count)
