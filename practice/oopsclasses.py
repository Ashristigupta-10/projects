#create class 
class Student:
    pass 

abc=Student()
xzy=Student()

abc.name="ABC"
abc.std= 12
abc.section=1
xzy.std=9
xzy.subjects=["math","geo"]
print(">>>",abc.section,xzy.std,xzy.subjects)

#inatance &class variable
print(">>>")
class emp:
    no_of_leaves=9
    pass 

abc=emp()
xzy=emp()

abc.name="ABC"
abc.salary=7000
abc.role= "hr"
xzy.name="XZY"
xzy.salary=7000
xzy.role="developer"
print(abc.no_of_leaves)
print(xzy.no_of_leaves)
print(emp.no_of_leaves)
#want to changes in leave so we can do with emp only
abc.no_of_leaves=10
emp.no_of_leaves=10
print(emp.no_of_leaves)
print(xzy.__dict__)
xzy.no_of_leaves=10
print(xzy.__dict__)#add no_of_leaves in xzy dict
print(emp.no_of_leaves)


# define the Vehicle class
print(">>>")
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
# your code goes here
car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00


# test code
print(car1.description())
print(car2.description())


#attributes name
#define the class with the name snake
print(">>>")
class Snake:
    name="python"#set an attribute 'name' of the class
    def change_name(self,new_name):#the first argument is self
        self.name= new_name #access the class attribute with the self keywords

#initiate the class snake and assign it to variable snake
snake=Snake()
#access the class attribute name inside the class snake
print(snake.name)
#change the name using the change_name method
snake.change_name("anaconda")
print(snake.name)


#add 2 complex numbers
print(">>>")
class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag

    def add(self,number):#self is n1 and number is n2
        real=self.real+number.real
        imag=self.imag+number.imag
        result=Complex(real,imag)
        return result

n1=Complex(5,6)
n2=Complex(-4,2)
#calling the add method on n1 object and pass to n2 obj
result=n1.add(n2)
print("real =",result.real)
print("imag =",result.imag)

#create a new class and object 
print(">>>")
class Parrot:
    #class attributes
    species="bird"

    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age

#instantiate the parrot class
blu=Parrot("Blu",10)
woo=Parrot("woo",15)

#access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("woo is also a {}".format(woo.__class__.species))

#access the instance attributes
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))


#create methods
print(">>>")
class peaku:
    #instance attributes
    def __init__(self,name,age):
        self.name=name
        self.age=age

    #instance method
    def sing(self,song):
        return "{} sings {}".format(self.name,song)

    def dance(self):
        return "{} is how dancing".format(self.name)

#instantiate the object
blu=peaku("blu",10)

#call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance())

#use of inheritance in python 
#parent class
print(">>>")
class Bird:
    def __init__(self):
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("swim faster")

#child class
class penguin(Bird):
    def __init__(self):
        #call super() function
        super().__init__() #allow to run init method of parent class inside child class
        print("penguin is ready")

    def __init__(self):
        #call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy= penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()


#Data encapsulation in python
print(">>>")
class Computer:
    def __init__(self):#using init method to store maximum selling price of c
        self.__maxprice=900

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice=price

c= Computer()
c.sell()

#change the price
c.__maxprice=1000 #try to modify the maxprice outside the class
c.sell()

#using setter function
c.setMaxPrice(1000) #private varible not seen on output
c.sell()



#using polymorphism
class Parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("Parrot can't swim ")

class Penguin:
    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("penguin can swim")

#common interface
def flying_test(bird):
    bird.fly()

#instantiate objects
blu=Parrot()
peggy=Penguin()

#passing the objects
flying_test(blu)
flying_test(peggy)


#object class define 
# use docstring
class MyNewClass:
    '''created new class'''
    pass

class header:
    "this is a header class"
    width=20
    height=30

    def footer(self):
        print('site header & footer is important')

#output:20,30
print(header.height)
print(header.width)

#output:<func header.site>
print(header.footer)

#output:print doc "this is site important parts"
print(header.__doc__)


#constructor in python
class ComplexNumber:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def get_data(self):
        print(f'{self.real}+{self.imag}j')


#dir()
numbers_list=[1,2]
print(">>>",dir(numbers_list))

result=numbers_list.__add__([3,4,5,6,7])
print(result)

#id()
number1=5
print(">>>",id(number1))

number2=10
print(id(number2))



# Create a new ComplexNumber object
num1 = ComplexNumber(5, 5)

# Call get_data() method
# Output: 2+3j
num1.get_data()

# Create another ComplexNumber object
# and create a new attribute 'attr'
num2 = ComplexNumber(10)
num2.attr = 10

# Output: (10, 0, 20)
print((num2.real, num2.imag, num2.attr))

# but c1 object doesn't have attribute 'attr'
# AttributeError: 'ComplexNumber' object has no attribute 'attr'
print(num1.attr)


#deleting attributes and objects
num1=ComplexNumber(3,4)
del num1.imag
num1.get_data()

del ComplexNumber.get_data
num1.get_data()

c1=ComplexNumber(3,4)
del c1
c1


