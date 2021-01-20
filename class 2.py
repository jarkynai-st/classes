class Dog:

    def __init__(self,name,poroda,age):
        self.name = name
        self.poroda = poroda
        self.age = age
        print("Собака создана!")
        print(f"{self.name} родился!")

    def sit(self):
        print(f"{self.name} присел!")
    def aport(self):
        print(f"{self.name} принеси палку!")
    def jump(self):
        print(f"{self.name} подпрыгнул!")


dog1 = Dog('Hatiko','Husky',10)
dog2 = Dog('Strelka','common',6)
print(dog1.name,dog2.name)
dog1.sit()
dog2.aport()
dog1.jump()


