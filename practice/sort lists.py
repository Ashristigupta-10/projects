#sortlist by alphabetically
thislist=["Novels","Ebooks","Pdf reader","Amazon reader","Kindle"]
thislist.sort()
print(thislist)

#numerically
thislist=[100,900,875,650,480,500,780,300,250]
thislist.sort()
print(thislist)

#sort decending
thislist=[100,900,875,650,480,500,780,300,250]
thislist.sort()
print(thislist)

#acending
thislist=[100,900,875,650,480,500,780,300,250]
thislist.sort(reverse=True)
print(thislist)


#reverse
thislist=[100,900,875,650,480,500,780,300,250]
thislist.reverse()
print(thislist)


#customize sort function
list=['A','B','a','Y','a','b','Z','c']
list.sort()
print(list)

#case sensitive sort
list=['A','B','a','Y','a','b','Z','c']
list.sort(key=str.lower)
print(list)

#abs()-return absolute number
def myfunc(n):
    return abs(n-50)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print(thislist)

#case insensitive sort
thislist=["Novels","Ebooks","Pdf reader","Amazon reader","Kindle"]
thislist.sort()
print(thislist)

##str.lower in case insensitive
thislist=["Novels","Ebooks","Pdf reader","Amazon reader","Kindle"]
thislist.sort(key=str.lower)
print(thislist)


#extended sortlist(slicing)
thislist=["Novels","Ebooks","Pdf reader","Amazon reader","Kindle"]
print(thislist[::2])
print(thislist[::3])
print(thislist[::-2])
print(thislist[::-3])
print(min(thislist))


