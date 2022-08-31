#dictionary is nothing but key value pairs



d1={"Amish Tripathi":"shiva triology",
    "Agatha Christie":"the ABC murder",
    "Gilbert patten":"Frank marriewell at yale",
    "Jane Austen":"pride and prejudice",
    "Agatha Christie":{"1":"the ABC murder","2":"endless evil underthe sun",}}
print("1...",d1)
print("2...",d1["Agatha Christie"])
print("3...",d1["Agatha Christie"]["2"])

#add new items
d1["Amish"]="Sita"
d1["f.scott"]="The great gatsby"
print("4...",d1)

#del & copy() 
d2=d1.copy()
del d2["Amish Tripathi"]
print("5...",d1)

print("6...",d1.get("Amish"))
print("7...",d1.keys())
print("8...",d1.items())


#brand value
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print("9...",thisdict["brand"])


#boolean list
thisdict = {
  "brand": "Ford",
  "electric":False,
  "model": "Mustang",
  "year": 1964,
  "colors":["red","white","blue"]
}
print("10...",thisdict)




#create a dictionary and take input from the user and return the meaning if the word from the dictionary
print("11...","Welcome to Dictionary")
Dictionary={"abase":" cause to feel shame","mellifluous":"sweet or musical","Halidom":"a holy place", "Petrichor":"who love the smell of rain","benefit":"advantage", "Astropille":"a lover of stars","callow":"young and inexperienced", "dally":"waste time", "endear":"make attractive"}
print("The required meaning is:")
Search=input()
print(Dictionary[Search])
print("Thanks for using Dictionary")


#copy()
stu={101:'rj',102:'rk',103:'rl'}
print("original Dict:")
print(stu)
print()

new_stu=stu.copy()
print("copied dict:")
print(new_stu)
print()

stu[102]='python'
print(stu)

#fromkeys()used to convert the list in keys
a=['name','class','rollno','add']
b={}
class10={}
class10=b.fromkeys(a)
#with value
class10['name']='shreya'
print("12...",class10)

#accessing dict
stu={101:'JJ',102:'Leo',103:'canal'}
fees={'JJ':20000,'Leo':50000,'canal':60000}
print(stu[101])
print(stu[102])
print(stu[103])

print(fees['JJ'])
print(fees['Leo'])
print(fees['canal'])

#Testing key(membership operator)
#check the value is exists in dictionary
stu={101:'JJ',102:'Leo',103:'canal'}
print(101 not in stu)
print(102  in stu)
print(102 and 101 not in stu)
