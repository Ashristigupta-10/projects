import time

true = ["T", "t", "True"]
false = ["F", "f", "False"]
correct = 0 #Storing the correct answers

name = input ("What's your name?") #Storing the user's name

print ("\nokk " +  name +", let's get started. Remember, the following answers are only True or False.")
time.sleep(2)

print ("\nPython is a case sensitive language true or false?")
choice = input(">>> ")
if choice in true:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print ("\npython is ool true or false?")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0  

print ("\npython is open source language true or false?")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 
  
print ("\n python django liberary is used for game development true or false?")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  
  
print ("\n the letter h is between letters g and j on keyboard.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\nSpaghetto is the singular form of the word spaghetti.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\ncamel have 3 sets of eyelashes.")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\n there are 5 zeros in one hundres thousand")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\n there are stars and zigzags on the flag of America")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\nif you add the two numbers on the opposite sides of dice together,the answer is always 7")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0 

print ("\n Newyork is nicknamed 'the big orange'")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\n Apes can't laugh")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0
    
print ("\nYou're finished, " + name +". You got", correct, "out of 11 correct.")