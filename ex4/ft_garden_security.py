class Plant:
    def __init__(self, name: str, height: float, age: int):
        self._name = name

        if height < 0:
            print(f"{name}: Error, height can't be negative")
            self._height = 0.0
        else:
            self._height = float(height)

        if age < 0:
            print(f"{name}: Error, age can't be negative")
            self._age = 0
        else:
            self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def set_height(self, height):
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = float(height)
        print(f"Height updated: {height}cm")

    def set_age(self, age):
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._age = age
        print(f"Age updated: {age} days")

    def show(self):
        print(f"Plant created: {self._name}: "
              f"{round(self._height, 1)} cm, "
              f"{self._age} days old")


def ft_garden_security() -> None:
    rose = Plant("Rose", 15, 10)
    print("=== Garden Security System ===")
    rose.show()
    rose.set_height(25)
    rose.set_age(30)
    print()

    print(f"Current state: {rose._name}: "
          f"{rose._height}cm, "
          f"{rose._age} days old")


if __name__ == "__main__":
    ft_garden_security()
