mystr="understand python is easy"
#print(len(mystr))
print(mystr.isalnum())

mystr="understandpythoniseasy"
#print(mystr.isalnum())
print(mystr.count("t"))

#.upper()
#return string in uppercase
a=" hello , world "
print(a.upper())
print(a.strip())#remove whitespace
print(a.replace("h","j"))#replace string
print(a.split())#split string into substring

#concatenate variable(merge)
a="string"
b="python"
c=a+b
print(c)

#format()
#insert numbers into string
height=6
text="my height is {}"
print(text.format(height))

#example 2
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))


#use index number{0} 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {2} pieces of item {0} for {1} dollars."
print(myorder.format(quantity, itemno, price))

#center()
text="shiva triology"
x=text.center(40)
print(x)

#encode(utf-8 encode string)
txt="my name is dåinå"
x=txt.encode()
print(x)

#expandtabs expand the word
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs(5))
print(txt.expandtabs(10))
print(txt.expandtabs(15))
print(txt.expandtabs(20))

#title()capital first letter of every word
txt="welcome to python"
x=txt.title()
print(x)

#.strip remove whitespaces
txt = "     of python    "

x = txt.strip()

print("of all topic", x, "is my favorite")


#rpartition()partition the word
txt="welcome to python"
x=txt.rpartition("to")
print(x)

#rindex() count the index munber of string
txt="welcome to python"
x=txt.rindex("python")
print(x)