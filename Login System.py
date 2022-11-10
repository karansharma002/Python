import time
import random
import json

def login():
	with open('data.json','r') as f:
		users = json.load(f)

	username = input("Enter Your Username: ")

	if username in users:
		password = input("Enter Your Password: ")
		if password == users[username]['password']:
			print('Successfully Logged into the system, Welcome',username)
			time.sleep(10)
			return
		elif not password == users[username]['password']:
			print ("Dear",username,"The Password Is Incorrect: ")
			time.sleep(10)
			return login()
			
	else:
		print ("Account Doesn't exists, Kindly Create a New Account: ")
		return register()

def register():
	with open('data.json','r') as f:
		users = json.load(f)

	print (" :You can either create an account with your Email ID, or Username which should be only alphabets: ")
	user_choice1 = input("Enter your Username you would like to use as: ")
	if not user_choice1 in users:
		print("Please enter your PASSWORD you would like to use: ")
		password = input("Enter your Password: ")
		users[user_choice1] = {}
		users[user_choice1]['password'] = password
		with open('data.json','w') as f:
			json.dump(users,f)

	elif user_choice1 in users:
		print('Account already exists, Kindly LOGIN with your username.')
		return login()

def userwindow():
    print (" Welcome to the Panel, Are you an existing user or Would like to create an account?")
    print (" Kindly Reply with, ('login') or ('register'): ")
    user_choice = input()
    if  user_choice == "login":
        return login()
    elif user_choice == "register":
        return register()
    else:
        print ("Invalid Choice, Kindly Re Enter :> ")
        return userwindow()

if __name__ == "__main__":
    userwindow()
    