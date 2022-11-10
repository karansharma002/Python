import time

#Founded Bugs
'''
Game doesn't ends when total chances reached 0
'''
file = open

# Global Variables
Store_Movements = []
Game_Won = 1
total_chances = 8

def game_instructions():

    print ("You slept last night, A Dream came and you have to find a way of coming out of the dream",
    "You have a candle in your hand, And the only way of exploring the area.")
    print ("\n")
    print ("\n")
    print ("Remember, Reaching the Main Spot isn't that easy, You have to think of every move you'll be going",
    "to take off. Mainly, There are 4 Doors, You have to choose, Once you stepped up by choosing the door",
    " You cannot return back. Each door has own way of reaching the Main Spot. 'Be Aware', There are 2 Wells",
    "inside. If you hear some water sounds, You should immediately find a way of going away. Else you will lose",
    "your live and will never be able to come out of the dream.")
    print ("\n")
    print ("\n")
    print ("Hints and Warnings will be given each time you are stucked, near, or going to spot something new",
    "Wish you best of luck." )
    print ("\n")
    print ("\n")
    time.sleep(1)
    print ("Hold your candle, We are going to move.. ")
    time.sleep(1)
    print ("Hold your candle, We are going to move..... ")
    time.sleep(1)
    print ("Hold your candle, We are going to move............... ")
    print ("\n")
    print ("\n")
    wanna_play = input(" Wanna come out of the dream? ('Play / Exit')").casefold()
    if wanna_play == "play":
        print ("Loading ..................")
        time.sleep(0.9)
        print ("Loading ..................")
        time.sleep(0.9)
        print ("Loading ..................")
        time.sleep(0.9)
        print ("Loading ..................")
        time.sleep(0.9)
    else:
        return empty_function()

# Game Information and Rules
def door1_one():
    global total_chances
    print ("\n")
    print ("You have chosen the 'Door One' , Good Decision we guess. ")
    print ("\n")
    print (" I can hear something, Uhmmm 'Where is this sound coming from? ")
    print ("\n")
    input_door1_1 = input("Where would you like to go?'Forward' 'Right' 'Left' 'Back' < (If you want to choose another door)").casefold()
    print ("\n")
    if input_door1_1 == "back":
        return user_window()
    elif input_door1_1 == 'right' or input_door1_1 == 'left':
        print ("\n")
        print (" Come on, Can't you see this wall?  ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door1_one()

    elif input_door1_1 == "forward":
        print ("Great Great, Keep Moving you will surely reach the destination")
        print ("\n")
        print ("You are Three Steps  Away!!")
        Store_Movements.append(input_door1_1)
        return Store_Movements,door1_two()

# DOOR 1 SECOND MOVEMENT 
def door1_two():
    global total_chances
    print ("\n")
    print ("mhmmm arghhhhhhh what's that? Is that a light? I guess so!! ")
    print ("\n")
    input_door1_2 = input("Where would you like to go?'Forward' 'Right' 'Left' 'Straight': ").casefold()
    print ("\n")
    if input_door1_2 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        print ("\n")
        return door1_two()

    elif input_door1_2 == 'Left':
        print ("\n")
        print (" Come on, Can't you see this wall?  ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door1_two(),total_chances

    elif input_door1_2 == "forward":
        print (" Man, Come on. Where you looking at??????? ")
        print ("\n")
        print ("Lost another live!")
        total_chances = total_chances - 1
        return door1_two()
    
    elif input_door1_2 == 'right':
        print ("\n")
        print (" Right is the best!!")
        print ("\n")
        Store_Movements.append(input_door1_2)
        print (" > You are Two Steps Away < ")
        print ("\n")
        return Store_Movements,door1_three()
    

#Door 1 Third Movement 
def door1_three():
    global total_chances
    print ("\n")
    print (" You should be happy, We are going to reach the Destination",
     " Hold that candle Tightly, In your Right Hand ")
    print ("\n")

    input_door1_3 = input("Where would you like to go?'Forward' 'Right' 'Left': ").casefold()
    print ("\n")
    if input_door1_3 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        print ("\n")
        return door1_three()

    elif input_door1_3 == 'Left':
        print (" You need more light, Take the candle in front of your EyES, Why can't you see the wall?? ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door1_three()

    elif input_door1_3 == "forward":
        print ("\n")
        print (" It's Enough now, Stop being Stupid! ")
        print ("\n")
        print ("Lost another live!")
        total_chances = total_chances - 1
        return door1_three()
    
    elif input_door1_3 == 'right':
        print ("\n")
        print (" Right is the best, I said Before ^_^ ")
        print ("\n")
        Store_Movements.append(input_door1_3)
        print (" > You are One Step Away < ")
        return Store_Movements,door1_four()
    

#Door 1 Fourth Movement
def door1_four():
    global Game_Won
    global total_chances
    print ("\n")
    print (" I can hear some sounds, Is that water? Come on Please, Let's drink  it .....")
    print ("\n")
    input_door1_4 = input("Where would you like to go?'Forward' 'Right' 'Left': ").casefold()
    print ("\n")
    if input_door1_4 == "back":
        print ("\n")
        print ("Told you many times, You cannot go back at this stage: ")
        print ("\n")
        return door1_four()
    elif input_door1_4 == "left":
        print ("\n")
        print ("Drink the water and Relax. You fell into Well")
        print ("\n")
        total_chances = total_chances - 1
        return door1_four(),total_chances
    elif input_door1_4 == "forward":
        print (" Wow Wow  I am soooooooooo happy, I finaly came out of the dream :) ")
        print ("\n")
        Game_Won += 5
        time.sleep(10)
        return Game_Won,empty_function()
    elif input_door1_4 == "right":
        print ("It's not always right, I was lying: ")
        print ("\n")
        total_chances = total_chances - 1
        return total_chances,input_door1_4

# Door 2 First Movement 
def door2_one():
    global total_chances

    print (" You have chosen the 'Door Two' , Perfect One ")
    print ("\n")
    print (" I can still see the Darkness here, Don't be lazy... Let's move... ")
    print ("\n")
    input_door2_1 = input("Where would you like to go? 'Forward' 'Right' 'Left' 'Back' < (If you want to choose another door)").casefold()
    print ("\n")
    if input_door2_1 == "back":
        return user_window()

    elif input_door2_1 == 'Right' or input_door2_1 == 'Left':
        print (" Hey, Are you drunk????????  ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_one(),total_chances

    elif input_door2_1 == "forward":
        print ("\n")
        print ("That's the perfect Decision")
        print ("\n")
        Store_Movements.append(input_door2_1)
        print ("You are tHREE Steps  Away!!")
        return Store_Movements,door2_two()

    else:
        print (" Hey, What you doing?? ")
        print ("\n")
        return  door2_one()
     

# DOOR 2 SECOND MOVEMENT 
def door2_two():
    global total_chances
    print (" i am actually excited to go out of this bastard dream!! ")
    print ("\n")
    input_door2_2 = input("Where would you like to go?'Forward' 'Right' 'Left': ").casefold()
    print ("\n")
    if input_door2_2 == "back":
        print ("You can't return back at this stage")
        print ("\n")
        return door2_two()

    elif input_door2_2 == 'Left':
        print (" Hey, Are you drunk? ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_one(),total_chances

    elif input_door2_2 == "forward":
        print (" Yes, Yes.... You are the Best ")
        print ("\n")
        Store_Movements.append(input_door2_2)
        print ("You are Two Steps  Away!!")
        return Store_Movements,door2_three()
    
    elif input_door2_2 == 'right':
        print("Hey, Where you looking at? Stupid!")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_two(),total_chances
     

#Door 1 Third Movement 
def door2_three():
    global total_chances
    print ("\n")
    print (" I can say, You are actually genius. We are going in the right way, That's the spirit! ")
    print ("\n")

    input_door2_3 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()
    print ("\n")
    if input_door2_3 == "back":
        print ("You can't return back at this stage")
        return door2_three()

    elif input_door2_3 == 'Left':
        print (" You should have taken a cup of water with you, You need it!! ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_three()

    elif input_door2_3 == "forward":
        print ("\n")
        print (" I really want to give you some flowers for these perfect decisions ")
        print ("\n")
        Store_Movements.append(input_door2_3)
        print ("You are One STEP aWAY, Don't be lazy. Let's moveeeeeeeeeeeeeeeeeeeeeeeee ")
        print ("\n")
        return Store_Movements,door2_four()

    elif input_door2_3 == 'right':
        print (" Why people choose Right?? ")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_three(),total_chances
     

#Door 1 Fourth Movement
def door2_four():
    global Game_Won
    global total_chances
    print (" Wanna drink some water?? I think it's somewhere near!! ")
    print ("\n")
    input_door2_4 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()
    print ("\n")
    
    if input_door2_4 == "back":
        print ("Told you many times, You cannot go back at this stage: ")
        print ("\n")
        return door2_four()

    elif input_door2_4 == "left":
        print (" Enjoy the water, It's smooooooth ")
        print ("\n")
        total_chances = total_chances - 1
        print ("Finally lost a chance, You deserves it!!")
        print ("\n")
        return door2_four(),total_chances

    elif input_door2_4 == "forward":
        print (" Hey, Hey are you there?????? Wake up, We are out of the Dream Now!! :) ")
        print ("\n")
        Game_Won += 5
        return Game_Won,empty_function()
    elif input_door2_4 == "right":
        print (" Delete Right word from your dictionary")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door2_three(),total_chances
   


# Door 3 First Movement 
def door3_one():
    global total_chances

    print (" You have chosen the 'Door Three' , TOTTALLLLLLY PERFECT!! ")
    print ("\n")
    print (" Why taking so long???? ")
    print ("\n")

    input_door3_1 = input("Where would you like to go? 'Forward' 'Right' 'Left' 'Back' < (If you want to choose another door)").casefold()
    if input_door3_1 == "back":
        return user_window()

    elif input_door3_1 == 'Right' or input_door3_1 == 'Left':
        print ("\n")
        print (" Please No Alcohal ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door3_one(),total_chances

    elif input_door3_1 == "forward":
        print ("\n")
        print (" I love FORWARD YES, I love it!! ")
        print ("\n")
        print ("You are Three Steps Away!!")
        Store_Movements.append(input_door3_1)
        return Store_Movements,door3_two()
        
    else:
        print ("\n")
        print (" Hey, What you doing?? ")
        print ("\n")
        return  door3_one()
 

# DOOR 3 SECOND MOVEMENT 
def door3_two():
    global total_chances
    print (" If you ask me where you should you go, I will say!! Stay in dream, Best Decision!! ")
    print ("\n")
    input_door3_2 = input("Where would you like to go?'Forward' 'Right' 'Left': ").casefold()
    if input_door3_2 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        print ("\n")
        return door3_two()

    elif input_door3_2 == 'Left':
        print (" Sometimes Alcohal is best :P ") 
        print ("\n")
        print ("You are two steps away!!")
        Store_Movements.append(input_door3_2)
        return Store_Movements,door3_three()

    elif input_door3_2 == "forward":
        print ("\n")
        print (" Please don't love too much, it's Injurious")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door3_two(),total_chances
    
    elif input_door3_2 == 'right':
        print(" You are the most stupid person I have seen, Open your eyes please ")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door3_two(),total_chances


#Door 1 Third Movement 
def door3_three():
    global total_chances
    print ("\n")
    print (" Please wake uppp ")
    print ("\n")
    input_door3_3 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()

    if input_door3_3 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        return door3_three()

    elif input_door3_3 == 'Left':
        print ("\n")
        print (" I wanna hug you <3") 
        print ("\n")
        print ("You are One Step Away!!")
        Store_Movements.append(input_door3_3)
        return Store_Movements,door3_four()

    elif input_door3_3 == "forward":
        print ("\n")
        print (" Look, Either You are drunk or This script is, Tell me where you looking at? ")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door3_three(),total_chances


    elif input_door3_3 == 'right':
        print (" Uhmm Uhmm Surprise!!!!! ")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door3_three(),total_chances


#Door 3 Fourth Movement
def door3_four():
    global Game_Won
    global total_chances
    print (" Sadly No well near :((, I really wanted to drink some water .... )) ")
    print ("\n")
    input_door3_4 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()
    
    if input_door3_4 == "back":
        print ("\n")
        print ("Told you many times, You cannot go back at this stage: ")
        return door3_four()

    elif input_door3_4 == "left":
        print ("\n")
        print (" Another Surprise <3 ")
        print ("\n")
        total_chances = total_chances - 1
        print ("You lost a chance !!")
        print ("\n")
        return door3_four(),total_chances

    elif input_door3_4 == "forward":
        print ("\n")
        print (" Time to come out of the Dream, And give me some redish flowers for waking you up :D :) ")
        print ("\n")
        Game_Won += 5
        return Game_Won,empty_function

    elif input_door3_4 == "right":
        print ("\n")
        print (" Told you before, Delete Right word from your dictionary")
        total_chances = total_chances - 1
        print ("\n")
        print ("You just lose one chance")
        print ("\n")
        return door3_four(),total_chances
  


# Door 4 First Movement 
def door4_one():
    global total_chances

    print (" You have chosen the 'Door Four', Aren't you hungry? ")
    print ("\n")
    input_door4_1 = input("Where would you like to go? 'Forward' 'Right' 'Left' 'Back' < (If you want to choose another door)").casefold()
    if input_door4_1 == "back":
        return user_window()

    elif input_door4_1 == 'Right' or input_door4_1 == 'Left':
        print ("\n")
        print (" Avoid Drugs, They are Injurious!! ") 
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door4_one(),total_chances

    elif input_door4_1 == "forward":
        print ("\n")
        print (" I can't express, How Happy I Am <3 ")
        print ("\n")
        Store_Movements.append(input_door4_1)
        print ("You are 3 steps away")
        print ("\n")
        return Store_Movements,door4_two()
        
    else:
        print (" Hey, What you doing?? ")
        print ("\n")
        return  door4_one()
 

# DOOR 4 SECOND MOVEMENT 
def door4_two():
    global total_chances
    print (" I love fruits, Do you? If yes, Believe me You should eat one there is something in front of you ")
    print ("\n")
    input_door4_2 = input("Where would you like to go?'Forward' 'Right' 'Left': ").casefold()
    if input_door4_2 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        return door4_two()

    elif input_door4_2 == 'Left' or input_door4_2 == "right":
        print ("\n")
        print (" I hate fruits, Sorry  :( ")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door4_two(),total_chances


    elif input_door4_2 == "forward":
        print ("\n")
        print (" Believe me You can do it ^^ ")
        print ("\n")
        print ("You are two steps away!! ")
        print ("\n")
        Store_Movements.append(input_door4_2)
        return Store_Movements,door4_three()
   

#Door 4 Third Movement 
def door4_three():
    global total_chances
    global Store_Movements
    print (" Hello <3 , Are you excited?? ")
    print ("\n")
    input_door4_3 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()

    if input_door4_3 == "back":
        print ("\n")
        print ("You can't return back at this stage")
        return door4_three()

    elif input_door4_3 == 'forward':
        print ("\n")
        print (" I love you <3") 
        print ("\n")
        print ("You are One Step Away!!")
        Store_Movements.append(input_door4_3)
        return Store_Movements,door4_four()
        

    elif input_door4_3 == "left" or input_door4_3 == "right":
        print ("\n")
        print (" Come on, That candle is about to expire!! ")
        total_chances = total_chances - 1
        print ("\n")
        print ("You just lose one chance")
        print ("\n")
        return door4_three(),total_chances
    

#Door 4 Fourth Movement
def door4_four():
    global Game_Won
    global total_chances
    global Store_Movements
    print (" Please helpppppppppp , We are one step away. Please please help !!!!!! )) ")
    print ("\n")
    input_door4_4 = input("Where would you like to go? 'Forward' 'Right' 'Left': ").casefold()
    
    if input_door4_4 == "back":
        print ("\n")
        print ("Told you many times, You cannot go back at this stage: ")
        return door4_four()

    elif input_door4_4 == "left":
        print ("\n")
        print (" I have a surprise for you!! ")
        time.sleep(2)
        print ("\n")
        print ("Excited to hear???????")
        time.sleep(4)
        print ("\n")
        print ("We are out of our dream, Congrulations <3")
        print ("\n")
        Store_Movements.append(input_door4_4)
        Game_Won += 5
        return Game_Won,empty_function

    elif input_door4_4 == "forward" or input_door4_4 == "right":
        print ("\n")
        print (" I hate this word 'forward', You should do same")
        print ("\n")
        total_chances = total_chances - 1
        print ("You just lose one chance")
        print ("\n")
        return door4_four(),total_chances


def user_window():
    global door1_one
    global door2_one
    global door3_one
    global door4_one
    print ("Which door would you like to Go? >> Door 1 << >> DOOR2 >> DOOR3 << DOOR4 >>")
    start_input = input()
    if start_input == "door1":
        return door1_one()
    elif start_input == "door2":
        return door2_one()
    elif start_input == "door3":
        return door3_one()
    elif start_input == "door4":
        return door4_one()
    else:
        print ("Oh My God, That doesn't exists. Please open your eyes < ")
        return user_window()

def empty_function():
    print (" WCC Out of the game Window.")
    return None
    

if __name__ == "__main__":
    while Game_Won <= 5 or total_chances <= 0:
        game_instructions()
        user_window()
