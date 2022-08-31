#parent class
class person(object):
    #__init__is known as constructor
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber= idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)

#child class
class emp(person):
    def __init__(self, name, idnumber,salary,post):
        self.salary=salary
        self.post=post

        #invoking the __init__ of the parent class
        person.__init__(self,name,idnumber)

#creation of an object variable or instance
a=emp('EL',888888,2008888,"INTERN")

#calling a fun of the class person using its instance
a.display()
