class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
    
    def get_info(self) -> None:
        print(f"{self.name.capitalize()} (Flower): {self.height}cm, {self.age} days, {self.color} color")

    def bloom(self) -> None:
        print(f"{self.name.capitalize()} is blooming beautifully!")

class Tree(Plant):
    def __init__(self, name: str, height: int, age: int, trunk_diameter: int) -> None:
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def get_info(self) -> None:
        print(f"{self.name.capitalize()} (Tree): {self.height}cm, {self.age} days, {self.trunk_diameter}cm diameter")

    def produce_shade(self) -> None:
        print(f"{self.name.capitalize()} provides {(self.trunk_diameter * 1.55):.0f} square meters of shade")

class Vegetable(Plant):
    def __init__(self, name: str, height: int, age: int, harvest_season: str, nutrition_value: str) -> None:
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutrition_value = nutrition_value

    def get_info(self) -> None:
        print(f"{self.name.capitalize()} (Vegetable): {self.height}cm, {self.age} days, {self.harvest_season} harvest")
        print(f"{self.name.capitalize()} is rich in {self.nutrition_value}")

rose = Flower("rose", 25, 30, "red")
sunflower = Flower("sunflower", 80, 45, "yellow")
oak = Tree("oak", 500, 1825, 50)
palm = Tree("palm", 420, 1020, 20)
tomato = Vegetable("tomato", 80, 90, "summer", "vitamin C")
carrot = Vegetable("carrot", 30, 80, "autumn", "vitamin A")
print("=== Garden Plant Type ===")
rose.get_info()
rose.bloom()
print()
sunflower.get_info()
sunflower.bloom()
print()
oak.get_info()
oak.produce_shade()
print()
palm.get_info()
palm.produce_shade()
print()
tomato.get_info()
print()
carrot.get_info()
print()
