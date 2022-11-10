import random
import time
print ("Welcome to the Roll A Dice Game")
print ("This will roll a dice between 1 and 6")
n = ""
def dice():
    print (random.randint(1,6))
    n = input("Do you want to roll again? (y/n) : ")
    if (n == "y") or (n == "yes"):
        return dice()
    else:
         print ("Thanks for rolling")
         
dice()
time.sleep(7.0)