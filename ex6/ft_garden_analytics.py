#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name
        self.height = height
        self._age = age
        self._stats = Plant.Statistics()

    def show(self) -> None:
        print(f"{self._name.capitalize()}: "
              f"{round(self.height, 1):.1f}cm, "
              f"{self._age} days old")

    def grow(self, growth: int) -> None:
        self.growth = growth
        for _ in range(growth):
            self.height += 2.1
        self._stats.__grow_call += 1

    def age(self, days: int) -> None:
        self._age += days
        self._stats.age_call += 1

    @staticmethod
    def older_than_year(age: int) -> bool:
        result_year = age > 365
        print(f"Is {age} more than a year? {result_year}")
        return result_year

    @classmethod
    def anonymous(cls) -> 'Plant':
        return cls("Unknown Plant", 0.0, 0)

    class Statistics:
        def __init__(self) -> None:
            self.__grow_call = 0
            self.age_call = 0
            self.show_call = 0

        def display(self) -> None:
            print(f"Stats: {self.__grow_call} grow, "
                  f"{self.age_call} age, "
                  f"{self.show_call} show"
                  )

    def display_statistics(self) -> None:
        self._stats.display()


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
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
    def __init__(self, name: str, height: float,
                 age: int, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        self.shade_calls = 0

    def produce_shade(self) -> None:
        self.shade_calls += 1
        print(
            f"Tree {self._name} now produces a shade of "
            f"{round(self.height, 1):.1f}cm long and "
            f"{round(self.trunk_diameter, 1):.1f}cm wide."
        )

    def display_statistics(self) -> None:
        super().display_statistics()
        print(f"{self.shade_calls} shade")

    def show(self) -> None:
        print("=== Tree")
        super().show()
        print(f"Trunk diameter: {round(self.trunk_diameter, 2):.1f}cm")
        self.produce_shade()
        print()


class Vegetable(Plant):
    def __init__(self, name: str, height: float, age: int,
                 harvest_season: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = 0

    def age(self, days: int) -> None:
        super().age(days)
        self.nutritional_value += days

    def grow(self, growth: int) -> None:
        super().grow(growth)

    def show(self) -> None:
        print("=== Vegetable")
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int,
                 color: str, seeds: int) -> None:
        super().__init__(name, height, age, color)
        self.seeds = seeds

    def bloom(self) -> None:
        super().bloom()
        self.seeds = 42

    def show(self) -> None:
        print("=== Seed")
        super().show()
        if self.bloomed:
            print(f"Seeds: {self.seeds}")


def display_plant_statistics(plant: Plant) -> None:
    plant.display_statistics()


def ft_garden_analytics() -> None:
    rose = Flower("Rose", 15.0, 10, "Red")
    oak = Tree("Oak", 100.0, 100, 20.0)
    tomato = Vegetable("Tomato", 20.0, 30, "Summer")

    rose.bloom()
    rose.show()
    display_plant_statistics(rose)
    oak.show()
    display_plant_statistics(oak)
    tomato.show()
    display_plant_statistics(tomato)


if __name__ == "__main__":
    ft_garden_analytics()
