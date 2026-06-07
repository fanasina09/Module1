class Plant:
    def __init__(self, name: str, height: float, age: int):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: "
              f"{round(self.height, 1)} cm, "
              f"{self.age} days old")

    def age_grow(self):
        self.age += 1

    def grow(self):
        self.height += 0.8


def ft_plant_growth() -> None:
    rose = Plant("Rose", 25, 30)
    print("=== Garden Plant Growth ===")
    daygrow = 7
    initheight = rose.height
    rose.show()
    for day in range(1, daygrow + 1, 1):
        print(f"=== Day {day} ===")
        rose.grow()
        rose.age_grow()
        rose.show()
    lastheight = rose.height - initheight
    print(f"Growth this week: {round(lastheight, 1)}")


if __name__ == "__main__":
    ft_plant_growth()
