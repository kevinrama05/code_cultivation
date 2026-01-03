class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def grow(self, cm: int = 1) -> None:
        self.height += cm

    def get_info(self) -> str:
        return f"{self.name}: {self.height}cm, {self.age} days old"

    @classmethod
    def category(cls):
        return "Regular plant"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self.color = color
        self.blooming = False

    def bloom(self) -> None:
        self.blooming = True

    def get_info(self) -> str:
        state = "blooming" if self.blooming else "not blooming"
        return (
            f"{self.name} (Flowering): {self.height}cm, "
            f"{self.age} days, {self.color} color [{state}]"
        )
    
    @classmethod
    def category(cls):
        return "Flowering plant"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, prize_points: int) -> None:
        super().__init__(name, height, age, color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Prize points: {self.prize_points}"

    @classmethod
    def category(cls):
        return "Prize flower"


class GardenManager:
    
    class GardenStats:
        @staticmethod
        def total_growth(plants: list[Plant]) -> int:
            total = 0
            for _ in plants:
                total += 1
            return total

        @staticmethod
        def count_flowering(plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                if plant.category() == "Flowering plant":
                    count += 1
            return count

        @staticmethod
        def count_prize(plants: list[Plant]) -> int:
            count = 0
            for plant in plants:
                if plant.category() == "Prize flower":
                    count += 1
            return count

        @staticmethod
        def count_plants(plants: list[Plant]) -> int:
            count = 0
            for _ in plants:
                count += 1
            return count

    def __init__(self) -> None:
        self.gardens: dict[str, list[Plant]] = {}

    def add_garden(self, owner: str) -> None:
        self.gardens[owner] = []

    def add_plant(self, owner: str, plant: Plant) -> None:
        self.gardens[owner].append(plant)
        print(f"Added {plant.name} to {owner}'s garden")

    def grow_all(self, owner: str) -> None:
        print(f"\n{owner} is helping all plants grow...")
        for plant in self.gardens[owner]:
            plant.grow()
            print(f"{plant.name} grew 1cm")

    def garden_report(self, owner: str) -> None:
        plants = self.gardens[owner]
        stats = self.GardenStats
        print(f"\n=== {owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in plants:
            if plant.category() == "Flowering plant":
                plant.bloom()
            print(f"f {plant.get_info()}")
        print(f"\nPlants added: {len(plants)}")
        print(f"Total growth: {stats.total_growth(plants)}cm")
        print(f"Flowering plants: {stats.count_flowering(plants)}")
        print(f"Prize flowers: {stats.count_prize(plants)}")

    @classmethod
    def create_garden_network(cls) -> str:
        return "Garden Network Initialized"

    @staticmethod
    def validate_height(height: int) -> bool:
        if height < 0:
            return False
        return True

print("=== Garden Management System Demo ===\n")

manager = GardenManager()
print(manager.create_garden_network())

manager.add_garden("Alice")
manager.add_garden("Bob")

oak = Plant("Oak Tree", 100, 180)
rose = FloweringPlant("Rose", 25, 30, "Red")
sunflower = PrizeFlower("Sunflower", 50, 90, "Yellow", 10)

manager.add_plant("Alice", oak)
manager.add_plant("Alice", rose)
manager.add_plant("Alice", sunflower)

manager.grow_all("Alice")
manager.garden_report("Alice")

print(f"\nHeight validation test: {manager.validate_height(-1)}")
print(f"Total gardens managed: {len(manager.gardens)}")
