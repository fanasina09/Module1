#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self.height = height
        self._age = age

    def show(self):
        print(f"{self._name.capitalize()}: "
              f"{round(self.height, 1):.1f}cm, "
              f"{self._age} days old")

    def grow(self, growth):
        self.growth = growth
        for _ in range(growth):
            self.height += 2.1

    def age(self, days):
        self._age += days


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        print("=== Flower")
        super().show()
        print(f"Color: {self.color}")
        if (self.bloomed is True):
            print(f"{self._name} is blooming beautifully")
        elif (self.bloomed is False):
            print(f"{self._name} has not bloomed yet")
        print()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self.height, 1):.1f}cm long and "
            f"{round(self.trunk_diameter, 1):.1f}cm wide."
        )

    def show(self):
        print("=== Tree")
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 2):.1f}cm")
        self.produce_shade()
        print()


class Vegetable(Plant):
    def __init__(self, name, height, age,
                 harvest_season: str):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self, days) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, growth):
        super().grow(growth)

    def show(self) -> None:
        print("=== Vegetable")
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


if __name__ == "__main__":
    def ft_garden_analytics() -> None:
        
