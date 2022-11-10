Guessed_Words = []
chances = 10
endthegame = 1
# Storing our words in the list
word1 = list('apple')
word2 = list('5000')
word3 = list('dreams')
word4 = list('confusion')
word5 = list('submarines')

# Using this function to take the input name of the user and share some details:
def username():

    print ("Welcome to the 'HANGMAN GAME DEVELOPED BY A Noob (Sofia)' ")
    print ("Before we continue, Kindly enter your Name (Format: Firstname LastName)")
    print ("\n" *7)
    name = input()
    print ("Alright,",name,"Glad to know you are interested in playing the game")
    print ("\n" *2)
    print ("Kindly reply with (Y / N), Do you wish to continue?")
    user_reply = input ()
    if user_reply == "N" or user_reply == "no":
        print ("Wrong Input maybe, Or you are not interested in playing the game?")
        return username()
    if user_reply == "y" or user_reply == "yes":
        print ("Starting the Game \n" *3)
    else:
         return username()

# Using this function to share some rules of the game
def rules():
    print ("Before we dive into the game, Let's read and understand some rules of the game: ")
    print ("\n")
    print ("1: You will be given a statement and you have to guess the matching letter forming the word")
    print ("\n")
    print ("2: You will be given 10 chances, Each wrong letter will decrement your chance by -1")
    print ("\n")
    print ("3: There will be 3 levels of the game, Each time a word is guess correctly, You will pass out: ")
    print ("\n")
    print ("4: You cannot quit the game in Middle")
    print ("\n")
    print ("Do you understand these rules (Yes/ No)?")
    rules_confirmation = input().casefold()
    if rules_confirmation == "no" or rules_confirmation == "n":
        print ("Invalid Input")
        return rules()
    elif rules_confirmation == "yes" or rules_confirmation == "y":
        print ("\n"*2)
        print ("Great work, Let's dive and Enjoy the water :P ")

# Using this function to return the words as a level:
def level(value):
    if value == 1:
        guess_word = ['_' for x in word1]
        return guess_word
    if value == 2:
        guess_word = ['_' for x in word2]
        return guess_word
    if value == 3:
        guess_word = ['_' for x in word3]
        return guess_word
    if value == 4:
        guess_word = ['_' for x in word4]
        return guess_word
    if value == 5:
        guess_word = ['_' for x in word5]
        return guess_word

# To count decrement the chance by 1 if wrong letter is inserted
def chance(yourvalue):
        global chances
        if  yourvalue == 1:
            chances = chances - 1
            return chances

# Using this small function to print the statement when game ends            
def endgame():
    global chances
    if chances == 0:
        print ("Uff you lost the game, Better Luck Next Time")
        print ("\n" *2)
        

# All good, We need to set this to run while chances are more than > 0 else end
def checkLetter(letter, word, guess_word):
    for c in word:
         if c == letter:
             guess_word[word.index(c)] = c
             word[word.index(c)] = '*'
    return guess_word

# The Result <3          
def begingame(var):
    global endthegame 
    if var == 1:

        guess_word = level(1)
        while '_' in guess_word and chances > 0:
            print ("\n"*2)
            print ("Sweetest Redish Fruit?")
            print (guess_word)
            guess = input('Letter: ')
            if not guess in word1:
                print ("This letter doesn't exists in the word, Kindly enter another one")
                print ("\n"*3)
                Guessed_Words.append(guess)
                chance(1)
                print ("You have",chances,"chances remaining")
                print ("\n"*4)
            if chances == 0:
                print ("You have",chances,"chances remaining")
                endthegame = 2
                endgame()
            
            else: 
                print(checkLetter(guess, word1, guess_word))
                if chances > 0 or endthegame < 2:
                    print ("Congrats, You have passed the level 1, Now comes the another level: ")
                    print ("\n" *10)
                    
    if var == 2:
        guess_word = level(2)
        while '_' in guess_word and chances > 0:
            print ("\n"*3)
            print ("How many rupees will a yeti-hunting permit set you back?")
            print ("\n"*2)
            print (guess_word)
            guess = input('Letter: ')
            if not guess in word2:
                print ("This letter doesn't exists in the word, Kindly enter another one")
                Guessed_Words.append(guess)
                chance(1)
                print ("You have",chances,"chances remaining")
            if chances == 0:
                endthegame = 2
                print ("You have",chances,"chances remaining")
                endgame()
            else: 
                print(checkLetter(guess, word2, guess_word))
            
                if chances > 1 or endthegame < 2:
                    print ("\n"*2)
                    print ("Congrats, You have passed the level 2, Now comes the another level: ")
                    print ("\n" *10)
                
    if var == 3:
        guess_word = level(3)
        while '_' in guess_word and chances > 0:
            print ("\n"*2)
            print ("What’s the oddest thing Antarctica recycles?")
            print (guess_word)
            guess = input('Letter: ')
            if not guess in word3:
                print ("This letter doesn't exists in the word, Kindly enter another one")
                Guessed_Words.append(guess)
                chance(1)
                print ("You have",chances,"chances remaining")
                if chances == 0:
                    endthegame = 2
                    print ("You have",chances,"chances remaining")
                    endgame()

            else: 
                print(checkLetter(guess, word3, guess_word))
                if chances > 1 or endthegame < 2:
                    print ("The word is",word5)
                    print ("\n"*2)
                    print ("Congrats, You have passed the level 3, Now comes the another level: ")
                    print ("\n" *10)
    if var == 4:
        guess_word = level(4)
        while '_' in guess_word and chances > 0:
            print ("\n"*2)
            print ("What happens when ants wear stilts?")
            print (guess_word)
            guess = input('Letter: ')
            if not guess in word4:
                print ("This letter doesn't exists in the word, Kindly enter another one")
                Guessed_Words.append(guess)
                chance(1)
                print ("You have",chances,"chances remaining")
                if chances == 0:
                    endthegame = 2
                    print ("You have",chances,"chances remaining")
                    endgame()
            else: 
                print(checkLetter(guess, word4, guess_word))
                if chances > 1 or endthegame < 2:
                    print ("The word is",word4)       
                    print ("\n"*2) 
                    print ("Congrats, You have passed the level4, Now comes the another level: ")
                    print ("\n" *10)
    if var == 5:
        guess_word = level(5)
        while '_' in guess_word and chances > 0:
            print ("\n"*2)
            print ("What’s the neatest thing you can buy for $600,000?")
            print (guess_word)
            guess = input('Letter: ')
            if not guess in word5:
                print ("This letter doesn't exists in the word, Kindly enter another one")
                Guessed_Words.append(guess)
                chance(1)
                print ("You have",chances,"chances remaining")
                if chances == 0:
                    endthegame = 2
                    print ("You have",chances,"chances remaining")
                    endgame()
            else: 
                print(checkLetter(guess, word5, guess_word))
                print ("\n" *10)
                print ("The word is",word5)
                if chances > 1 or endthegame < 2: 
                    print ("Congrats, You won the GAME, You have been given a (****** - Secret Gift) ")
                    print ("\n"*2)
                    print (" The secret will be revealed, Use your mind :) ")
                    endthegame = 2


                    
        
                    
if __name__ == "__main__":
    username()
    rules()
    if chances > 0 or endthegame < 2:
        begingame(1)
    if chances > 0 or endthegame < 2:
        begingame(2)
    if chances > 0 or endthegame < 2:
        begingame(3)
    if chances > 0 or endthegame < 2:
        begingame(4)
    if chances > 0 or endthegame < 2:
        begingame(5)
    
    
