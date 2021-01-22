class House:
    def __init__(self,rooms,bathroom,kitchen,hall,swimming_pool):
        self.rooms = rooms
        self.bathroom = bathroom
        self.kitchen = kitchen
        self.hall = hall
        self.swimming_pool = swimming_pool

    def description(self):
        print(self.rooms,self.bathroom,self.kitchen,self.hall,swimming_pool)

    def reconstruction(self,number):
        self.state = number
        if self.state < 30:
            print('Пора делать ремонт!')

    def repairs(self,workers):
        for house in workers:
            workers = (self.kitchen + self.bathroom)
        print(workers,self.kitchen + self.bathroom)
        if workers >= self.kitchen + self.bathroom:
            print("Ремонт успешно сделан")
            workers = (self.swimming_pool)
        print(workers,self.swimming_pool)
        if workers >= self.swimming_pool:
            print("Бассейн построен!")





house1=House(rooms=6,bathroom=3,kitchen=2,hall=1,swimming_pool=1)
house1.reconstruction(70)
house1.repairs('Kitchen')
house1.repairs('Bathroom')
house1.repairs('Swimming pool')









