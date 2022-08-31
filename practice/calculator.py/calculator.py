from unittest import result
from functions import *
print("what do u want to do?")
print("1 Addition")
print("2 Subtraction")
print("3 Multiplication")
print("4 Divide")

choice=input("enter your choice:")

num1=float(input("enter Number 1:"))
num2=float(input("enter Number 2:"))

if choice=='1':
    addition(num1,num2)
elif choice=='2':
    subtraction(num1,num2)
elif choice=='3':
    multiplication(num1,num2)    
elif choice=='4':
    divide(num1,num2) 
else:
    print("Invalid choice")   
   
