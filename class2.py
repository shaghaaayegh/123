#tabe
def first(n):
    a=list()
    for i in range (1,n+1):
        a.append(i)
    return a
print(first(10))


def first_generator(n):
    for i in range(1,n+1):
        yield i

for i in first_generator(10):
    print(i)



'''class person:
    def __init__(self,age,ghad):          #self eshareh gar be khode class
        self.age=age
        self.ghad=ghad

    def set_age(self,age):
        self.age=age
    def get_age(self,age):
        print('the age is %d'%self.age)
    def info(self):
        print('the age is %d' % self.age)
        print('the ghad is %d' % self.ghad)

person_obj1=person(20,180)
person_obj1.info()

class student(person):           #ers bordan
    def __init__(self,name,age,ghad):
        self.name=name
        super().__init__(age,ghad)    #super:eshareh gar be classe pedar(zamani ke dar classe farzand bekhahim az methode classe pedar estefadeh konim)

    def info(self):
        print('the name is %s' % self.name)
        print('the age is %d' % self.age)
        print('the ghad is %d' % self.ghad)'''





#*********************HALE TAMRIN HA:***********************

student_obj1=student('mahan',25,177)
student_obj1.info()
