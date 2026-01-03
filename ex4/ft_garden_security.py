class SecurePlant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        if height < 0:
            self._height = 0
        else:
            self._height = height
        if age < 0:
            self._age = 0
        else:
            self._age = age

    def set_height(self, new_height: int) -> None:
        if new_height < 0:
            print(f"Invalid operation attempted: height {new_height}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self._height = new_height
            print(f"Height update: {self._height}cm")

    def set_age(self, new_age: int) -> None:
        if new_age < 0:
            print(f"Invalid operation attempted: age {new_age} days old [REJECTED]")
            print(f"Security: Negative age rejected")
        else:
            self._age = new_age
            print(f"Age update: {self._age} days old")

    def get_height(self) -> int:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_info(self) -> None:
        print(f"Current plant: {self.name.capitalize()} ({self._height}cm, {self._age} days)")
