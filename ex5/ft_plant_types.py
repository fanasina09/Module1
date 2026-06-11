#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = float(height)
        self._age = age

    def age(self, days: int) -> None:
        self._age += days

    def grow(self) -> None:
        self._height += 2.1
        self.show()

    def show(self) -> None:
        print(f"Plant created: {self._name}: "
              f"{round(self._height, 1)} cm, "
              f"{self._age} days old")


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.bloomed = False

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float, age: int,
                 trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.trunk_diameter}cm")

    def produce_shade(self) -> None:
        print(f"{self._name} now produces a shade of"
              f"{round(self.get_height(), 1)}cm long and "
              f"{round(self.trunk_diameter, 1)}cm wide")


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def grow(self) -> None:
        super().grow()
        self.nutritional_value += 1

    def age(self, days: int) -> None:
        super()._age(days)
        self.nutritional_value += days

    def show(self) -> None:
        super().show()
        print(f"Harvest Season: {self.harvest_season}")
        print(f"Nutritional Value: {self.nutritional_value}")


if __name__ == "__main__":
    def ft_plant_types():
        rose = Flower("Oak", 15, 10, "Brown")
        rose.show()
        # print("\n[asking the rose to bloom]")
        rose.bloom()
        rose.show()
