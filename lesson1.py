
class Hero:

    # Конструктор класса
    def __init__(self, name, lvl, hp):
        # Атрибуты объекта класса
        self.hero_name = name
        self.hero_lvl = lvl
        self.hero_hp = hp

    # Это метод класса а не функция
    def action(self):
        print(f"{self.hero_name} Base action!!")

    def rest(self):
        print(f"{self.hero_name} rest!!")

kirito = Hero("Kirito", 100, 1000)
asuna = Hero("Asuna", 111, 1111)

# MageHero - Только для классов mageHero
# hero_kirito

