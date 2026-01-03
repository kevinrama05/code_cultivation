class Plant():
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def plant_profile(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

    def plant_age(self) -> None:
        self.plant_grow()
        self.age += 1

    def plant_grow(self) -> None:
        if self.age < 10:
            self.height += 2
        else:
            self.height += 1

    def one_week_growth(self) -> None:
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

class PlantFactory():
    def generate_plants(plant_list: list[tuple[str, int, int]]) -> list[Plant]:
        plants = []
        for name, height, age in plant_list:
            plants.append(Plant(name, height, age))
        return plants

    def plants_display(plants: list[Plant]) -> None:
        print("=== Plant Factory Outptut ===")
        for plant in plants:
            print(f"Created: {plant.name.capitalize()} ({plant.height}cm, {plant.age} days)")
        print(f"\nTotal plants created: {len(plants)}")

def main() -> None:
    plants_tup = [
        ("rose", 25, 30),
        ("oak", 200, 365),
        ("cactus", 5, 90),
        ("sunflower", 80, 45),
        ("fern", 15, 120)
    ]
    plants = PlantFactory.generate_plants(plants_tup)
    PlantFactory.plants_display(plants)

main()
