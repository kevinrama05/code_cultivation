class Plant():
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def plant_profile(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old")

def main():
    print("=== Garden Plant Registry ===")
    rose = Plant("rose", 25, 30)
    sunflower = Plant("sunflower", 80, 45)
    cactus = Plant("cactus", 15, 120)
    rose.plant_profile()
    sunflower.plant_profile()
    cactus.plant_profile()

main()
