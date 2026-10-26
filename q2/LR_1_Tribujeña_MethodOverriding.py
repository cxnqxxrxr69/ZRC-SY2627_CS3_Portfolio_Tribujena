class Animal:
    def __init__(self, name: str):
        self.__name = name  

    def get_name(self) -> str:
        return self.__name

    def make_sound(self):
        pass

    def eat(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print(f"{self.get_name()} roars loudly!")

    def eat(self):
        print(f"{self.get_name()} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.get_name()} trumpets!")

    def eat(self):
        print(f"{self.get_name()} eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.get_name()} chatters!")

    def eat(self):
        print(f"{self.get_name()} eats bananas.")

if __name__ == "__main__":
    animals = [
        Lion("Simba"),
        Elephant("Dumbo"),
        Monkey("George")
    ]

    for animal in animals:
        animal.make_sound()
        animal.eat()
        print("-----")