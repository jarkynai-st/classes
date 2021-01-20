class Cat:
    def __init__(self,name,color,breed,weight):
        self.name = name
        self.color = color
        self.breed = breed
        self.weight = weight
        print("Кошка создана!")
        print(f"{self.name} родился!")

    def voice(self):
        print(f"{self.name} мяу!")
    def fly(self):
        if self.weight <= 5:
            print(f"{self.name} летит по воздуху!")
        else:
            print('Не поднять')
    def eat(self):
        print(f"{self.name} кушать подано!")

    def run(self):
        self.possition = self.possition + 10
        print(f"{self.name} побежал!")


mursik = Cat(name='Mursuk',color='Grey',breed='Sphynx',weight=4)
barsik = Cat(name='Barsik',color='white',breed='swedish',weight=6)
mursik.fly()
mursik.run()
barsik.run()
