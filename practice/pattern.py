#print pyramid
print("1...")
row=5
for i in range(1,row+1):
    for j in range(1, i+1):
        print(j,end='')
    print('')


#Inverted pyramid of numbers
row=5
b=0
#reverse
for i in range(row,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end='')
    print('\r')

#same digit pyramid 
row=5
num=row
#reverse
for i in range(row,0,-1):
    for j in range(0,i):
        print(num,end='')
    print('\r')

#alternate number print using while loop
row=5
i=1
while i<=row:
    j=1
    while j<=i:
        print((i*2-1),end=" ")
        j=j+1
    i=i+1
    print('')
