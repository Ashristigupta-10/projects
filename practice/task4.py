# #print table
# #multiplication table of 2 to 50

for i in range(2,50):
     print("\n\nmultiplication table for %d\n" %(i))
     for j in range(2,50):
        print("%-5d X %5d = %5d" % (i,j, i*j))


#calling function inside the function
def xzy():
    wishes = "HI Happy birthday"
    return wishes

def abc():
    x = xzy()
    print(">>>>>>>", x)

obj = abc()

#program
#create digital clock
import time

while True:
    localtime=time.localtime()
    result=time.strftime("%I:%M:%S:%P",localtime)
    print(result)
    time.sleep(1)




