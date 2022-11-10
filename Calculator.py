import time
print (" **** --- Just a simple Calculator, You can specifiy the values and Your option --- *** ")

# A Function to calculate two values:
def calc_two_num(num1,num2):
    addition = num1 + num2
    multiplication = num1 * num2
    subtraction = num1 - num2
    division = num1 / num2
    user_choice = input("What would you like, >> 'Addition ' or 'Multiplication' or 'subtraction' or 'division' ")
    if user_choice == "Addition" or "addition":
        return addition
    elif user_choice == "Multiplication" or "multiplication":
        return multiplication
    elif user_choice == "subtraction" or "Subtraction":
        return subtraction
    elif user_choice == "division" or "Division":
        return division
    else:
        print ("Wrong Choice, Please read carefully and enter it")
        return calc_two_num
    
# A Function to calculate three values:
def calc_three_num(num1,num2,num3):
    addition = num1 + num2 + num3
    multiplication = num1 * num2 * num3
    subtraction = num1 - num2 -  num3
    division = num1 / num2 / num3
    user_choice = input("What would you like, >> 'Addition ' or 'Multiplication' or 'subtraction' or 'division' ")
    if user_choice == "Addition" or "addition":
        return addition
    elif user_choice == "Multiplication" or "multiplication":
        return multiplication
    elif user_choice == "subtraction" or "Subtraction":
        return subtraction
    elif user_choice == "division" or "Division":
        return division
    else:
        print ("Wrong Choice, Please read carefully and enter it")
        return calc_three_num()

# A Function to calculate four values:
def calc_four_num(num1,num2,num3,num4):
    addition = (num1 + num2) + (num3 + num4)
    multiplication = (num1 * num2) * (num3 * num4)
    subtraction = (num1 - num2) -  (num3 - num4)
    division = (num1 / num2) / (num3 / num4)
    user_choice = input("What would you like, >> 'Addition ' or 'Multiplication' or 'subtraction' or 'division' ")
    if user_choice == "Addition" or "addition":
        return addition
    elif user_choice == "Multiplication" or "multiplication":
        return multiplication
    elif user_choice == "subtraction" or "Subtraction":
        return subtraction
    elif user_choice == "division" or "Division":
        return division
    else:
        print ("Wrong Choice, Please read carefully and enter it")
        return calc_four_num()



decision = input ("How many numbers would you like to calculate? \n Please, Choose one option and reply: >>>Two or Three or Four ?<<<:")
if decision == "two" or decision == "Two":
    sl1 = int(input("Enter the Num1: "))
    sl2 = int(input("Enter the Num2: "))
    print (calc_two_num(sl1,sl2))

elif decision == "three" or decision == "Three":
    sl1 = int(input("Enter the Number1: "))
    sl2 = int(input("Enter the Number2: "))
    sl3 = int(input("Enter the Number3: "))
    print (calc_three_num(sl1,sl2,sl3))

elif decision == "four" or decision == "Four":
    sl1 = int(input("Enter the Number1: "))
    sl2 = int(input("Enter the Number2: "))
    sl3 = int(input("Enter the Number3: "))
    sl4 = int(input("Enter the Number4: "))
    print (calc_four_num(sl1,sl2,sl3,sl4))
else:
    print ("Invalid Option, Kindly Re Run the Program")

print (" ------- >> Thanks for Using it, Take care and Have a nice day ------ - ")

time.sleep(10.0)