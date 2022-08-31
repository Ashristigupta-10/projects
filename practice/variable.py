#creating variables
x=5
y="john"
print(x)
print(y)

#variables
a=89
b=12
c=a+b
print(c)

user_one_name="welcome droisys" #snake case writing

#give input
print("enter your number")
inpnum=input()
print("you entered",int(inpnum)+10)

#escape sequence
print("hello \"world\" world")

#backslash n
print("hello python \n all code are done")


#exercise1
#this id double \\
print("this is \\\\ bcakslash")

#print these are mountains/\/\/\/\
print("these are /\\/\\/\\/\\ mountains")

#print emoji
print("\U0001F602")

#floating point division
print(2/2)
print(4/2)
print(8/6)
print(4//2)#integer division

#Assign value to multiple variables
a,b,c=(89,22,23)
print(a,b,c)

#printing the type of variable
a="harry"
b=345
c=45.32
d=True
print(type(a))
print(type(b))
print(type(c))
print(type(d))


print("enter 1st no:")
inta=input()
print("enter second number:")
intb=input()
print(int(inta)+int(intb))

#global variable
#create var outside of a func and use it inside func
x="cgfhcjkh"

def myfunc():
    print("python is"+ x)
myfunc()

#create Var inside func, with same name as GV
x="shiva triology"

def myfunc():
    x="is written by "
    print("a novel"+ x)

myfunc()

print("amish tripathi"+ x)

