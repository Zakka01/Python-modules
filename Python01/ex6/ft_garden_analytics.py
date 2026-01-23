class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.__height = height
        self.__age = age
    def grow(self):
        self.__height += 1
    def Age(self):
        self.__age += 1
    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.age} days")

class FloweringPlant(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color 
    def bloom(self):
        print(f"{self.name} is blooming in {self.color} color!")
            
class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, age, color, prize_points):
        super().__init__(name, height, age, color)
        self.prize_points = prize_points
    def show_prize(self):
        print(f"{self.name} has {self.prize_points} prize points!")
      
      
class GardenManager:
    def __init__(self, garden):
        self.gradens = garden

    def add_garden(self, garden):
        self.gardens.append(garden)
        print(f"Added {self.name} Tree to {self.gradens}'s garden")

    def remove_garden(self, index):
        if 0 <= index < len(self.gardens):
            self.gardens.pop(index)
            print(f"Garden at index {index} removed!")
        else:
            print("Invalid index!")

