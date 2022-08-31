# 1.without list comprehension
lst1=[0,1,2,3,4,5,6,7,8,9]
new_lst1=[]
for i in lst1:
    new_lst1.append(i+1)
print("1..",new_lst1)

#2.range 
new_lst1=[]
for i in range(20):
    new_lst1.append(i+1)
print("2...",new_lst1)

#3.print list and append the list which is divisible by 2
lst=[]
for i in range(20):
    if(i%2==0):
        lst.append(i)
print("3...",lst)

#4. nested if
lst=[]
for i in range(20):
    if(i%2==0):
        if(i%3==0):
            lst.append(i)
print("4...",lst)

#5.if else
lst=[]
for i in range(10):
    if(i%2==0):
        lst.append(i)
    else:
        lst.append("invalid")
print("5...",lst)




#############################################
#1.with list comprehension making new list
lst2=[0,1,2,3,4,5,6,7,8,9]
new_lst2=[i+1 for i in lst2]
print("1...",new_lst2)

#2.using list comprehension print list using rage
new_lst2=[i+1 for i in range(20)]
print("2...",new_lst2)

#3 code same question but using list comprehension
lst2=[i for i in range(20) if i%2==0 ]
print("3...","new list:",lst2)

#4. nested if with list compre..
lst2=[i for i in range(20) if i%2!=0 if i%3!=0]
print("4...","new list:",lst2)

#5. if else
lst2=[i if i%2==0 else "invalid" for i in range(10)]
print("5...",lst2)

#accept number less than 5
lst=[x for x in range(10)if x <5]


print("7...")
lst=[]
n=int(input("Enter number of elements:"))
for i in range(10):
    b=int(input("Enter element:"))
    lst.append(b)
lst.sort()
print("Second largest element is:",lst[n-2])
print(lst)

