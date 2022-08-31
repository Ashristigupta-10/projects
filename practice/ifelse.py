var1=6
var2=56

var3=int(input())
if var3 > var2:
    print("greater")
if var3==var2:
    print("equal")
else:
    print("lesser")

#elif condition if previous condition is not true then use..
var1=6
var2=56

var3=int(input())
if var3 > var2:
    print("greater")
elif var3==var2:
    print("equal")
else:
    print("lesser")


#print the age of a person whos age is greater so print you can drive otherwise not drive
print("whats the age?")
age = int(input())
if age<18:
    print("you can drive")
elif age==18:
    print("we will thinkl about you")
else:
    print("you are not eligible...")

#nestedif (if inside if)
x = 48

if x > 20:
  print("Above twenty,")
  if x > 30:
    print("and also above 30!")
  else:
    print("but not above 30.")


