import this
from xml.dom.expatbuilder import theDOMImplementation

mylist = ["apple", "banana", "cherry"]
print("1...",mylist)


#to determine how many items a list has, use the len() function:
#Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print("2...",len(thislist))

#change list
thislist=["apple","banana","cherry"]
thislist[1:2]=["z","q"]
print("3...",thislist)

#add list item
thislist.append("orange")
print("4...",thislist)

Novels=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
Novels.append("the secret of Mahabharat")
Novels.append("Sita")
Novels.append("the secret of karn")
print("5...",Novels)

#insert item
thislist.insert(1,"grapes")
print("6...",thislist)

#list length
thislist=["app","data","merge"]
print("7...",len(thislist))

#type()
mylist=["apple","banana","cherry"]
print("8...",type(mylist))



#Access listitem
#print the 2nd item in list
thislist=["computer","cpu","mouse","speaker"]
print("9...",thislist[1])
print("10...",thislist[3])

#negative list indexing
#print the last item of list
thislist=["computer","cpu","mouse","speaker","keyboard"]
print("11...",thislist[-1])
print("12...",thislist[-3])

#list range of indexing
thislist=["computer","cpu","mouse","speaker","keyboard"]
print("13...",thislist[2:4])
print("14...",thislist[1:5])
print("15...",thislist[2:])

#check item in list
thislist=["computer","cpu","mouse","speaker","keyboard"]
if "apple" in thislist:
    print("16...","yes,'apple' is on the list")
else:
    print("17...","no, there is no apple in the list")

#remove list item
#pop()
#remove the second item
thislist=["computer","cpu","mouse","speaker","keyboard"]
thislist.pop(2)
print("18...",thislist)

#del
thislist=["computer","cpu","mouse","speaker","keyboard"]
del thislist[2]
print("19...",thislist)

#delete entire item
thislist=["computer","cpu","mouse","speaker","keyboard"]
del thislist

#clear()
thislist=["computer","cpu","mouse","speaker","keyboard"]
thislist.clear()
print("20...",thislist)

#loop list
#loop through list
#print all item ,one by one:
thislist=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
for x in thislist:
    print("21...",x)



#condition that only accept item that valuate to True
#only accept item that are not"the immortals of mehula"
Novels=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
newlist=[x for x in Novels if x != "The immortals of Mehula"]
print("22...",newlist)

#with no if statement
Novels=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
newlist=[x for x in Novels]
print("23...",newlist)

#Expression#
#upper case in newlist
Novels=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
newlist=[x.upper()for x in Novels]
print("24...",newlist)

#set all values in newlist is print error
Novels=["Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras"]
newlist=['Error' for x in Novels]
print("25...",newlist)

#slicing index
thislist=["computer","cpu","mouse","speaker","keyboard","harddisk"]
print("26...","xyz",thislist[-1:-2])
#because the start is ahead of the stop for traversal

thislist=["computer","cpu","mouse","speaker","keyboard","harddisk"]
print("27...","xyz",thislist[-1::-2])


#sum thislist
thislist=[4,6,8,9,6,3,2]
print("28...",sum(thislist))


#print one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print("29...",x)

#join two list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print("30...",list3)


#print number only lower than 5
newlist=[x for x in range(10) if x<5] 
print("31...",newlist)

#.copy()
lst1=[1,2,3,4,5,6,7,8,9,10]
lst1.copy()
print("32...",lst1)

#clear()
lst1.clear()
print("33...",lst1)

#given list is in Ascending order or not
lst1=[1,9,3,4,5,6,7,8,9]
temp_lst1=lst1[:]
lst1.sort()
if temp_lst1==lst1:
    print("give list is an ascending order")
else:
    print("given list is not")


lst1=[]
temp_lst1=lst1[:]
lst1.sort()
if temp_lst1==lst1:
    print("give list is an ascending order")
else:
    print("given list is not")


#interchange the value first ele to last
lst1=[1,2,3,4,5,6,7,8,9]
lst1[1],lst1[5]=lst1[5],lst1[1]
print(lst1)