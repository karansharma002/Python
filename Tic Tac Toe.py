import random
# Global Variables
game_won  = 0
game_lost = 0
entered_words = []
row1 = ['1','2','3']
row2 = ['4','5','6']
row3 = ['7','8','9']

# This will be our game layout
def game_map():
    global row1
    global row2
    global row3
    print ("                    ",row1)
    print ("\n")
    print ("                    ",row2)
    print ("\n")
    print ("                    ",row3)

#Game Instructions
def instructions():
    print ("Below is the layout where both of the players will draw either"
    " 0 or 1 in the place prefered")
    print ("\n"*2)
    game_map()
    print ("\n"*2)
    print ("You will have to enter your choice, Choose from one of the letter and enter it.")
    print ("That place will be re written by your character, Either x or y depends on the role")
    print ("The First player whos characters will form a line either", 
    "Horizontly or Vertically or By Side will win")
    print ("\n" * 4)
    print ("Imporant Thing: You will be playing as a X and Computer will be playing as Y: ")    
    print ("\n" * 4)


# Changing the value entered by the Player 1 to X
def player_one(num):
    
    global row1
    global row2
    global row3

# ROW 1 Value Changing
    if num == "1":
        row1[row1.index('1')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)


    elif num == '2':
        row1[row1.index('2')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '3':
        row1[row1.index('3')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    
#Row 2 Value Changing
    if num == '4':
        row2[row2.index('4')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)
    elif num == '5':
        row2[row2.index('5')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '6':
        row2[row2.index('6')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    
#Row 3 Value Changing
    if num == '7':
        row3[row3.index('7')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '8':
        row3[row3.index('8')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '9':
        row3[row3.index('9')] = 'x'
        print ("\n"*2)
        game_map()
        print ("\n"*2)
    return row1, row2,row3

# Changing the value entered by the Player 2 to  "Y"
def player_two(num):
    global row1
    global row2
    global row3
    # ROW 1 Value Changing
    if num == "1":
        row1[row1.index('1')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '2':
        row1[row1.index('2')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '3':
        row1[row1.index('3')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)
   
    #Row 2 Value Changing
    if num == '4':
        row2[row2.index('4')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
    elif num == '5':
        row2[row2.index('5')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '6':
        row2[row2.index('6')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)
    
    #Row 3 Value Changing
    if num == '7':
        row3[row3.index('7')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '8':
        row3[row3.index('8')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    elif num == '9':
        row3[row3.index('9')] = 'y'
        entered_words.append(num)
        print ("\n"*2)
        game_map()
        print ("\n"*2)

    return row1,row2,row3


# Taking out the input from user and the computer, Returning it to the change value function
def playerturns(value):
    global entered_words
    if value == 1:
        print (game_map())
        print ("Enter the number you would like to move on: ")
        playerchoice1 = input()
        if (playerchoice1 in row1) or (playerchoice1 in row2) or (playerchoice1 in row3):
            if not playerchoice1 in entered_words:
                return player_one(playerchoice1)

            elif playerchoice1 in entered_words:
                print ("This position has been already occupied")
                return playerturns(1)
        else:
            print ("Invalid Slot, Kindly checkout the layout and Re Enter the Word! ") 
            return playerturns(1)
          
    if value == 2:
        # Like if we want it o be a realistic move to trigger when user moves we set it to on based on the user MOVE. SIMPLE
        # Now, How will we do it/?
        # We can do it teasily, Ofc simple <3
        # IF ROW 1 COLUM 1 AND ROW 2 COULM 1 IS OCCUPIED BY USER, MOVE AT THE 3 ELSE RANDOM . RANDINT
        actual_value = random.randint(1,9)
        player_choice2 = str(actual_value)
        if (player_choice2 in row1) or (player_choice2 in row2) or (player_choice2 in row3):
            if not player_choice2 in entered_words:
                return player_two(player_choice2)
            elif player_choice2 in entered_words:
                print ("This position has been already occupied")
                return playerturns(2)
        else:
            print ("Invalid Slot, Kindly checkout the layout and Re Enter the Word! ") 
            return playerturns(2)


# Will end the game immediately when positions matches
def verify_lines():
    global game_won
    global game_lost
# Hz Checkout

    if row1[0] == row1[1] and row1[1] == row3[2]:
        game_won = game_won + 2
        return game_won 
    elif row2[0] == row2[1] and row2[1] == row3[2]:
        game_won = game_won + 2
        return game_won 
    elif row3[0] == row3[1] and row3[1] == row3[2]:
        game_won = game_won + 2
        return game_won 
      
# Vert Checkout
    if row1[0] == row2[0] and row2[0] == row3[0]:
        game_won = game_won + 2
        return game_won 
    elif row1[1] == row2[1] and row2[1] == row3[1]:
        game_won = game_won + 2
        return game_won 
    elif row1[2] == row2[2] and row2[2] == row3[2]:
        game_won = game_won + 2
        return game_won 
    
# Cross Checkout
    if row1[0] == row2[1] and row2[1] == row3[2]:
        game_won = game_won + 2
        return game_won 
    elif row1[2] == row2[1] and row2[1] == row3[0]:
        game_won = game_won + 2
        return game_won
    else:
        game_lost = game_lost + 2
        return game_lost


# All bugs fixed, Except the Infite Run and game not ending when drawn.

while game_won <= 2:
    verify_lines()
    print("Your Turn")  
    playerturns(1)
    verify_lines()
    print("PC Turn to move ")
    playerturns(2)
    verify_lines()
      


