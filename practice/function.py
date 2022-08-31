#function to find the average marks
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks/total_subjects
    return average_marks

#calculate the grade and return it
def compute_grade(average_marks):
    if average_marks>=80:
        grade='A'
    elif average_marks>=60:
        grade='B'
    elif average_marks>=50:
        grade='C'
    else:
        grade='F'
    return grade

marks=[55,64,75,80,65]
average_marks=find_average_marks(marks)
print("your average marks is:",average_marks)

grade=compute_grade(average_marks)
print('your grade is:', grade)


#write once and many times we use it :
#define func:
def disp():
    name="python"
    print("1..","welcome to ",name)

#calling the function
disp()
disp()

#divide large task into small for easy debigging
#defining fun
#separate fun of addition
def add():
    x=10
    y=20
    c=x+y
    print(c)
add()
#separate fun of substract
def sub():
    x=50
    y=20
    c=x-y
    print(c)
sub()


#fun with argu and parameter
#fun with parameter
def add(y):
    x=30
    c=x+y
    print(c)

#calling fun with argu
add(20.56)

#fun without parameter r argu
def add():
    x=20
    y=30
    c=x+y
    print("4...",c)
#call the fun
add()

#return multiple statement
#define a func
def add(y):
    x=20
    c=x+y
    d=y-x
    return c,d
#call a fun
sum,sub=add(60)
print(sum)
print(sub)


#pass a func as parameter
def disp(sh):
    print("disp func"+sh())

def show():
    return"show func"

disp(show)

#write fun name follwed by(),placing any required arg within the brackets.
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, raina, From My Function!, I wish you a great year!"
my_function_with_args("raina", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)