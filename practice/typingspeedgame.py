from time import time # to record the time

# to calculate the accuaracy of input prompt
def tperror(prompt):
    global inwords
    words= prompt.split()
    errors=0

    for i in range(len(inwords)):
        if i in (0,len(inwords)-1):
            if inwords[i]==words[i]:
                continue
            else:
                if inwords[i]==words[i]:
                    if(inwords[i+1]== words[i+1])&(inwords[i-1]== words[i-1]):
                        continue
                    else:
                        errors+=1
                else:
                    errors +=1
        return errors


#now to calculate the speed of typing words per min
def speed(inprompt,stime,etime):
    global time
    global inwords

    inwords= inprompt.split()
    twords=len(inwords)
    speed=twords / time

    return speed

# calculate the total elapsed time
def elapsedtime(stime,etime):
    time= etime-stime
    return time

if __name__=='__main__':
    prompt= " Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
    #paragraph to check your typing speed
    print("Type this:-",prompt," ")

    #checking to input enter basically it will see
    input("press enter when you are ready to check your speed!!!")

    #recording  time for input
    stime=time()
    inprompt=input()
    etime=time()

    #collect all the information returned by the functions
    time=round(elapsedtime(stime,etime),2) #round off the time
    speed = speed(inprompt,stime,etime)
    errors=tperror(prompt)

    #printing all the requiredf data to see result
    print("Total time elapsed:",time,"seconds")
    print("your Average typing speed was", speed,"words per min(w/m)")
    print("with the total of",errors,"errors")
   