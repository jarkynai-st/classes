# class Student:
#     student_id = 0
#     def __init__(self,name,last_name,group):
#         self.name = name
#         self.last_name = last_name
#         self.group = group
#         Student.student_id += 1
#
#
# student1 = Student('akylbek','melisov','python')
# print(student1.student_id,student1.name)
# student2 = Student('jarkynai','satarova','python')
# print(student2.student_id,student2.name)
# student3 = Student('aigerim','kashkarbekova','pyton')
# print(student3.student_id,student3.name)
# student4 = Student('baiel','nurmatbek uulu','pyton')
# student5 = Student('nurjanat','abaeva','python')

# print(student1.group)


class Car:

    def __init__(self,mark,color,model,year):
        self.mark = mark
        self.color = color
        self.model = model
        self.year = year
        self.run = 0
        self.engine = ''
        self.boost = 0 #разгон

    def move(self,distance):
        if distance > 0:
            self.run += distance


    def set_engine(self,new_engine):
        self.engine = new_engine
        if new_engine == 'common':
            self.boost = 7
        elif new_engine == 'advanced':
            self.boost = 4
        elif new_engine == 'race':
            self.boost = 2


car1 = Car('bmw','black','x6','2020')
car2 = Car('mercedes','pink','s 600','2021')
car3 = Car('tesla','white','s 6','2021')
car3.set_engine('advanced')
print(car2.engine,car2.boost)
print(car3.engine,car3.boost)
