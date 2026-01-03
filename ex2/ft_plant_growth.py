class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def plant_profile(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def plant_age(self):
        self.plant_grow()
        self.age += 1

    def plant_grow(self):
        if self.age < 10:
            self.height += 2
        else:
            self.height += 1

    def one_week_growth(self):
        day = 1
        old_height = self.height
        print("=== Day 1 ===")
        self.plant_profile()
        while day < 7:
            self.plant_age()
            day += 1
        print("=== Day 7 ===")
        self.plant_profile()
        print(f"Growth this week: +{self.height - old_height}")

def main():
    rose = Plant("rose", 25, 30)
    rose.one_week_growth()

main()
