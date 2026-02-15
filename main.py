import time as tm
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



sentences = [
    "the orange cat slept peacefully on the warm windowsill",
    "a sudden gust of wind scattered the papers across the room",
    "she found a mysterious key hidden inside the old book",
    "the city lights shimmered beautifully against the night sky",
    "he brewed a fresh cup of coffee before starting his work",
    "a colorful kite soared high above the sandy beach",
    "the mountain trail was quiet except for chirping birds",
    "they laughed loudly at the unexpected joke",
    "rain tapped gently on the roof throughout the evening",
    "the ancient clock chimed exactly at midnight"
]

while True:   #while loop to continue game
    am= input('Press "s" to start and "q" to quit: ')
    if am == "s":
        tt=rm.choice(sentences)
        print('')
        print("                      TYPING TEST        ")
        print()
        print("")
        print("Type This:     ",tt)
        print()
        tme=tm.time()
        usrninput= input("ENTER: ")
        tme2=tm.time()

        # Calling functionsq
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

