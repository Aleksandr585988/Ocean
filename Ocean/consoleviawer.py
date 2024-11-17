
from constants import Constants
from predator import Predator
from prey import Prey
from ocean import Ocean


class ConsoleViaWer(Ocean):
    def run(self, default_num_iteration=Constants.DEFAULT_NUM_ITERATION):
        while True:
            try:
                num_iterations = input(f"\n\nEnter number of iterations: (default = {default_num_iteration}): ")

                if not num_iterations:
                    num_iterations = default_num_iteration
                else:
                    num_iterations = int(num_iterations)

                if num_iterations < 1:
                    print("The number of iterations cannot be less than 1. Please enter a valid number.")
                else:
                    if num_iterations > default_num_iteration:
                        print(f"Number of iterations cannot exceed {default_num_iteration}. Using default value.")
                        num_iterations = default_num_iteration
                    break
            except ValueError:
                print("Invalid input! Please enter a valid number.")

        print(f"\nNumber of iterations = {num_iterations}\nbegin...\n")

        for iteration in range(num_iterations):
            if self.num_predators > 0 and self.num_prey > 0:
                for row in ocean.get_cells():
                    for cell in row:
                        if isinstance(cell, Predator):
                            cell.process()
                        elif isinstance(cell, Prey):
                            cell.process()

                self.display_stats(iteration)
                self.display_cells()
                self.display_border()

        print("\n\nEnd of Simulation\n")


if __name__ == "__main__":
    ocean = ConsoleViaWer()
    ocean.run()
