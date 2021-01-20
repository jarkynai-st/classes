class Human:

    def __init__(self,name,age,nation,gender):
        self.name = name
        self.age = age
        self.nation = nation
        self.health = 100
        self.citizenship = ''
        self.gender = gender
        self.documents = []
        self.married = False

    def description(self):
        print(self.name,self.age,self.nation,self.gender,self.health,self.citizenship)


    def damage(self,number):
        self.health -= number
        if self.health < 0:
            print('Пора в больницу!')


    def set_documents(self,document):
        if document == 'pasport' and self.age > 16:
            self.documents.append(document)
        if document == 'visa' and self.age > 18:
            self.documents.append(document)
        else:
            print(f"{self.name} не может получить данный документ!")




human1 = Human('Harry Potter',11,'english','male')
human2 = Human('Aigerim',18,'kyrgyz','female')
human1.damage(101)
human1.set_documents('visa')
human1.set_documents('passport')

human1.description()