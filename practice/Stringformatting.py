#basic string formatting
#concatenate the string
myage=21
broage=32
number=2
print("my age is"+ str(myage))

#using string formatting
print("my age is {}".format(myage))
print("my age is {} and my bro age is {}".format(myage,18))

#working with position
#value put in other placeholder
#change the value position through index number 
print("my age is {1} and my bro age is {0},{2}".format(myage,18,19))

#type conversion using format (int to float)
print("number is{0:.2f}".format(number))

#caret symbol(^)for using text in centre\
print("{0:*^6s}".format("abcde"))
print("{0:*^7s}".format("abcde"))
print("{0:*^10s}".format("abcde"))
print("{0:*^11s}".format("abcde"))
print("{0:*^13s}".format("abcde"))

#print 1t0 9 number square and cube through string format
for i in range(10):
    print("{} {} {} ".format(i,i**2,i**3))

#format specification
print("{num:5d}".format(num=15))
print("{num:5d}".format(num=15))
print("{num:05d}".format(num=15))
print("{num:+5d}".format(num=15))
print("{num:5d}".format(num=15))
print("{num:<5d}".format(num=15))
print("{num:>5d}".format(num=15))
print("{num:*<5d}".format(num=15))
print("{num:*>5d}".format(num=15))
print("{num:^5d}".format(num=15))

d1={'abc':3000,'xyz':4000}
print("{abc} {xyz}".format(**d1))