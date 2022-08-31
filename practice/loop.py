#print code one by one
languages=["eng","french","german"]
for language in languages:
    print("1...",language)

#print individual letter of string using loop
word="zechoslovakia"
for letter in word:
    print("2...",letter)

#loop over the element of tuples here
nums=(1,2,4,5,6)
sum_nums=0
for num in nums:
    sums_nums=sum_nums+num
print(f'sum of number is{sum_nums}')




#factorial 
print("3...") 
num=int(input("enter the number:"))
factorial=1

#iterate through a list using indexing
genre=['pop','rock','jazz']
for i in range(len(genre)):
    print("4...","I like",genre[i])

print("5...")
if num<0:
    print("sorry, factorial for negative number does not exist:")
elif num==0:
    print("the factorial for number 0 is 1")
else:
    for i in range(1, num+1):
          factorial=factorial*i
    print("the factorial of ", num, "is", factorial)


#loop using while loop 
# number guessing game

print("6...",'this is a guessing game')
import random  #it's func r package which generate random num
random_number=random.randrange(1,10)#generate the num b/w 1 to 10
guess=int(input("what could be the number?")) 
correct= False #bydefault assign the value false
print(random_number)

while not correct:
    if guess==random_number:
        print("congrats you got it")
        correct=True
    elif guess>random_number:
        print("too high")
        break
    elif guess<random_number:
        print("too low")
        break
    else:
        print("try something else")
        break


#nested loop 
words=["xyz","abc","roc","jump"]
for word in words:#fetching word from the list
    print("the following lines will print each letters of"+word)
    for letter in word:#fetching letter for word
        print (letter)
    print("")#this print is used to blank line    


# atm bank
print("7...",'welcome to xyz bank')
restart=('y') #key value assign
chances=3
balance=900
while chances>=0:
    pin=int(input("please enter your 4 digits pin:"))
    if pin==(1234):
        print('you entered your pin correctly\n')
        while restart not in('n','NO','no','N'):
            print('please press 1 for your balance\n')
            print('please press 2 for your withdrawl\n')
            print('please press 3 for your pay in\n')
            print('please press 4 for your return card\n')
            option=int(input('choose your option...') )
            if option==1:
                print('your balance is $',balance,'\n')
                restart=input('want to go back?')
                if restart in ('n','NO','no','N'):
                    print('thank you for using xyz')
                    break

            elif option==2:
                option2=('y')
                withdrawl=float(input('how much you want to withdraw? \n $10/$20/$40/$60/$80/$100 for other Amount press 1'))
                if withdrawl in [10,20,40,60,80,100]:#passing the list
                    balance=balance-withdrawl #substract the balance
                    print('\n your balance is $ ',balance)
                    restart=input('choose your option:')
                    if restart in ('n','NO','no','N'):
                        print('Thankyou for using xyz banking')
                        break
                elif withdrawl !=[10,20,40,60,80,100]:
                    print('Invalid amount,please try again\n')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl= float(input('please enter the desired amount:'))
                elif option==3:
                    pay_in=float(input('what amount you like to pay in?'))
                    balance=balance+pay_in
                    print('\nyour balance is $',balance)
                    restart=input('would you like to go back?')
                    if restart in ('n','NO','no','N'):
                        print('thankyou for using xyz banking')
                        break
                elif option==4:
                    print('please wait while your card is returned...\n')
                    print('thankyou for using xyz banking')
                    break
                else:
                    print('please enter a correct number.\n')
                    restart=('y')
            elif pin!=('1234'):
                print('Incorrect password')
                chances=chances-1
                if chances==0:
                    print('\n no more tries, contact support@xyz.co')
                    break
def xzy():
    print("HI Happy birthday")

xyz
