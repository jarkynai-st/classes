class Beaver:

    finished_bridges = 0

    def __init__(self, name, age, weight, power):
        self.name = name
        self.age = age
        self.weight = weight
        self.power = power
        self.finished_bridges = 0
        if self.age > 11:
            self.power -= 5

    def __str__(self):
        return "{} {}".format(self.name, self.age)

    def building(self, bridge):
        if (self.weight * self.power) >= bridge.weight:
            self.finished_bridges += 1
        else:
            print('{} слишком слаб!'.format(self.name))


class Bridge:

    def __init__(self, legth, weight):
        self.length = legth
        self.weight = weight
        self.material = 'tree'


    def building(self,team:list):
        group_power = 0
        for beaver in team:
            group_power += (beaver.weight + beaver.power)
        print(group_power,self.weight+self.length)
        if group_power >= self.weight + self.length:
            print('Мост успешно построен!')
            Beaver.finished_bridges += 1
        else:
            print('Команда слишком слабая! Наберите другую!')



beaver1 = Beaver(name='Bobrik',age=5, weight=9, power=10)
beaver2 = Beaver(name='Musya',age=7, weight=4, power=3)
beaver3 = Beaver(name='Sam',age=8, weight=11,power=14)
beaver4 = Beaver(name='John',age=12,weight=12,power=14)
beaver5 = Beaver(name='Aktan',age=10,weight=14,power=14)
beaver6 = Beaver(name='Trump', age=9,weight=12,power=17)

bridge1 = Bridge(legth=10, weight=100)


beaver_team = (beaver1,beaver2,beaver3,beaver4,beaver5,beaver6)
bridge1.building(beaver_team)
print(Beaver.finished_bridges)



















