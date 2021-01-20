class Person:
    def __init__(self,name,race):
        self.name = name
        self.race = race
        self.power = 0
        self.damage = 0
        self.armor = 0
        self.level = 0
        self.exp = 0
        if self.race == 'fairy':
            self.health = 10
            self.mana = 2000
        elif self.race == 'goblin':
            self.health = 200
            self.mana = 100
        else:
            self.health = 150
            self.mana = 150
        self.power = 0
        self.damage = 0
        self.armor = 0
        self.level = 0
        self.exp = 0
        self.position = 0
        print('Персонаж успешно создан!')
    def description(self):
        print(f"Имя: {self.name}, Здоровье: {self.health}, Мана: {self.mana},"
              f"Раса: {self.race},Сила: {self.power}, Урон: {self.damage}, Уровень: {self.level},Броня:{self.armor}")


    def level_up(self,exp):
        self.exp += exp
        if self.exp == 100:
            self.level += 1
            self.power += 100// 20
            self.damage += 100// 20
            self.armor += 100// 20

    def wear(self,cloth):
        if cloth == 'pentaarmor':
            self.armor += 20
        elif cloth == 'legendary dress':
            self.armor += 100
            self.health += 50
        elif cloth == 'witch jacket':
            self.mana += 100

        elif cloth == 'legendary plate':
             self.mana += 20
             self.armor += 500
             self.health += 200

    def set_weapon(self,weapon):
        if weapon == 'sword':
            self.power += 1
            self.range = 2
        elif weapon == 'axe':
            self.power += 1
            self.damage += 2
            self.range = 2
        elif weapon == 'bow':
            self.power += 1
            self.damage += 2
            self.mana += 5
            self.range = 100

    def move(self):
        self.position += 1

    def attack(self,object):
        if (self.position - object.position) <= self.range:
            object.health -= self.damage
            print("Здоровье монстра после атаки нашего героя",object.health)

class Monster:

    def __init__(self,position):
        self.position = position
        self.health = 20

monster = Monster(2)



warrior1 = Person('Tiffany','goblin')
warrior1.level_up(100)
warrior1.wear('Legendary plate')
warrior1.set_weapon('bow')
warrior2 = Person('Bloom','fairy')
warrior2.wear('witch jacket')
warrior1.attack(monster)
warrior1.attack(monster)



