tp=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
print("1...",tp)

#print opposite string/numbers
a='Amish tripathi(shiva triology)','The immortals of Mehula','the story of the nagas','The Oth of vayuputras'
b='sita','the secret of karn'
temp=a
a=b
b=temp
print("2...",a,b)

#tuple len
tp=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
print("3...",len(tp))

#tp -data types
tp1=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
tp2=(4,6,7,1,5,6)
tp3=(True,False,False)
print(tp1)
print(tp2)
print("4...",tp3)

#type()
tp1=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
print("5...",type(tp1))

#delete tp
tp1 = ("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
del (tp1)
print ("6...","After deleting tup : ")

#slicing in tp
tp2=(22,33,44,55,88,77,99,1)
print("7...",tp2[1:5])

#dont menstion the start value the range bydefault start from the first term
tp1=(22,55,33,66,8,2.7,9,0)
print("8...",tp1[:5])
print("9...",tp1[4:])
print("10...",tp1[:])
print("11...",tp1[::2])
print("12...",tp1[-4:-1])#8,2,7.9
print("13...",tp1[-1::-3])#0,8,55


#iteration use 
a=(2,4,5,7,9)
for x in range(4):
    print("14...",a[x])


#print all item accept water
tp=("air","soil","water","fire","sky")
print("16...",tp[:2])


#convert tp into list to able to change it:
x=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
y=list(x)
y[1]="the perfect murder"
x=tuple(y)
print("17...",x)

#check if item exists
#if specified item is present in a tuple use the 'in'keywords
tp1=("Amish tripathi(shiva triology)","The immortals of Mehula","the story of the nagas","The Oth of vayuputras","sita","the secret of karn")
if "sita" in tp1:
    print("17...","yes element is present.")
else:
    print("18...","no")

#using astrik
#add list value the "tropic" variable
fruits=("apple","mango","orange","pine","cherry")
(tropic,*yellow,red)=fruits
print("19...",*yellow)
print("20...",tropic)
print("21...",red)
# print("22...",*yellow)
# print("23...",type(yellow))
# print("24...",yellow[0])
# print("25...",yellow[1])
# print("26...",yellow[2])
print("27...",type(*tropic[0]))



#find greatest number in tuple
print("22...","enter number separated by comma ")
t1=tuple([int(e) for e in input().split(',')])
print("greatest number in the tuple is",max(t1))


#print tuple through count
tp1=(10,20,30,40,50,60,70)
print(tp1)
count=0
for i in tp1:
    print("tp1[%d]=%d"%(count,i))
    count=count+1

