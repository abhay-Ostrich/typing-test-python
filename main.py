from time import *
import random as rm

#function to calculate errors
def countingerrors (a,b):
    error=0
    for i in range(len(a)):
        try:
            if a[i]!=b[i]:
                error= error + 1
        except:
            error=error + 1
    return error

# function to calculate time
def time_fuc(tstart,tend,usrinput):
    time_delay=tend-tstart
    time_delay_in_min= time_delay/60
    speed= (len(usrinput)/5)/time_delay_in_min
    return round(speed)

# function for error to accuracy
def accuracy_fuc(total_cheracter,errors):
    # if total_cheracter == 0:
    #     return 0
    a=((total_cheracter-errors)/total_cheracter)*100
    return round(a)



test= ["hello its me this side",
"here is your typing speed test created by using python",
"once upon a time there was a king who did nothing and died",
"if there was some one there ",
"there is no one named this lives here"]

while True:   #while loop to continue game
    am= input('Press "s" to start and "q" to quit: ')
    if am == "s":
        tt=rm.choice(test)
        print('')
        print("                      TYPING TEST        ")
        print()
        print("")
        print("Type This:     ",tt)
        print()
        tme=time()
        usrninput= input("ENTER: ")
        tme2=time()

        # Calling functions
        print(f"Speed : {time_fuc(tme,tme2,usrninput)} w/m")
        qw=countingerrors (tt,usrninput)
        print("Errors : ",qw)
        at=len(tt)
        print(f"Accuracy  : {accuracy_fuc(len(tt), qw)}%")
    elif am== "q":
        print("you exited the game")
        break
    else:
        print('wrong input')
