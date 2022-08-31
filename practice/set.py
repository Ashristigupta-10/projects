#creating a set
from ast import Set
from this import s


set1=set()
print("initial set:")
print ("1...",set1)

#create a set with string
set1=set("mysetfuncode")
print("\n using string:")
print("2...",set1)

#avoid dublicate value
set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print("3...",set1)
  
#using add method
set1.add(8)
set1.add(9)
set1.add((6,7))
print("\n add new element:")
print("4...",set1)


#add element using update func
set1=set({4,5,(6,7)})
set1.update({10,11})
print("\n set after adding ele:")
print("5...",set1)


#update
set={"abc","cba","cid"}
tropical={"pine","mango","papaya"}
set.update(tropical)
print("6...",set)

a={'a','b','c','d','e','f'}
b={'a','c','e','g','h'}
print("9...","A:",a)
print("B:",b)
print()#set output as it is
 
#intersection method
ism=a.intersection(b)
print("8...",ism)

i=a.union(b)
print("9...",i)

i= a.difference(b)
print("10...",i)

#set comprehension 
set1={0,1,2,3,4,5,6,7,8,9,10,11,12}
new_set1={i+1 for i in set1}
print("11...",new_set1)

#adding single and multiple set element
a={10,20,'python',40}
print("12...","before adding:",a)
print(id(a))  

a.update([101,102,104,108])
print("13...","after adding:",a)
print(id(a))

#remove and discard method
a={10,20,'gh',50}
print("original set",a)
print(id(a))
print()

a.remove('gh')
print("after removing",a)
print("14...",id(a))

#passing set to function
def show(s):
    print("15...",s)
    print("16...",type(s))
    for i in s:
        print("17...",i)
st={10,20,30,40}
show(st)

#copying elements
a = {10,20,'ghk'}
print("before copy",a)
print(id(a))
print()

new_a =a.copy()
print("after copy",new_a)
print(id(new_a))

#set input from user
a = Set()
print(id(a))

n=int(input("enter number of elements:"))

for i in range(n):
    el=input("enter element:")
    a.add(el)
for i in a:
    print(i)


