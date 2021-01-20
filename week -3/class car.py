class Car:
    wheels = 4
    def __init__(self,name,year,color,model,is_crashed):
        self.name = name
        self.color = color
        self.model = model
        self.year = year
        self.fuel = 100
        self.run = 0
        self.speed = 0
        self.is_crashed = is_crashed
        self.V = 20
        self.position = 0
        print(f"{self.name} created!")

    def drive_to(self,city,km):
        result = self.V / 100
        result = result * km
        if result < self.fuel:
            self.fuel -= result
            if self.fuel >= 0:
                print(f"{self.name} drive to{city}")
        else:
            print('Road so far...')

    def charge(self):
        if self.fuel < 20:
            self.fuel = 100

    def crash(self,another_car):
         if another_car.position == self.position:
             self.is_crashed = True
             another_car.is_crashed = True
             print(f"{another_car.name} and {self.name} were crash")



class Human:

    def __init__(self,full_name,age,nation,height,weight):
        self.full_name = full_name
        self.age = age
        self.nation = nation
        self.height = height
        self.weight = weight
        self.position = 0
        self.health = 100
        self.is_alive = True
    def move(self):
        self.position += 1

    def accident(self,car,trafficlight):
        if car.position == self.position and trafficlight.green:
            if self.health > 40:
                if 5<car.speed < 20:
                    self.health -= 20
                elif car.speed > 20:
                    self.health -= 40

            else:
                self.health = 0
                self.is_alive = False
        print(f"{self.full_name} попал в аврию, его сбила машина {car.name}, осталось здоровье {self.health}")


class TrafficLights:
    def __init__(self):
        self.red = False
        self.yellow = False
        self.green = False

    def set_color(self,color:int):
        if color % 2 == 1:
            self.red = True
            self.yellow = False
            self.green = False
        elif color == 'yellow':
            self.green = False
            self.red = False
            self.yellow = True
        elif color % 2 == 0:
            self.red = False
            self.green = True
            self.yellow = False



audi = Car(name='AUDI',year=2021,color='grey',model='RX 8',is_crashed=False)
bmw = Car(name='BMW',year=2020,color='black',model='X 6',is_crashed=False)
honda = Car(name='HONDA',year=2020,color='white',model='X 5',is_crashed=False)


human1 = Human(full_name='Bob',age=22,height=100,weight=80,nation='french')

traffic_light = TrafficLights()
traffic_light.set_color(5)
audi.speed = 50
print(traffic_light.red,traffic_light.yellow,traffic_light.green)
for i in range(1,10):
    if human1.health > 0:
        traffic_light.set_color(i)
        human1.accident(audi, traffic_light)


audi.drive_to('Los-Angeles',100)
audi.crash(another_car=honda)
print(audi.is_crashed,bmw.is_crashed,honda.is_crashed)


human1.accident(audi,traffic_light)
print('Здоровье человека:', human1.health,human1.is_alive)



