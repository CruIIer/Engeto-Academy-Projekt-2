"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""


from random import randint
###### INTRODUCTION ######
separator = 47 * "-"
print(separator)
print("Hi there!")
print(separator)
print("""I've generated a random 4 digit number for you.
Let's play a bulls and cows game.""")
print(separator)
    
    
###### CREATING 4 DIGITS PIN CODE ######
pin = []
pin.append(randint(1,9))
while len(pin) != 4:
    num = randint(0, 9)
    if num not in pin:
        pin.append(num)

print(pin)

###### USER'S PIN ######
while True:
    user_attempt = input("Enter your number: ")
    if len(user_attempt) != 4:
        print("Your pin must contain 4 digits.")
    if user_attempt[0] == "0":
        print("Your pin can't start with 0.")
    if not user_attempt.isnumeric():
        print("Your pin must contian numbers only.")
    if len(set(user_attempt)) != len(user_attempt):
        print("Your pin can't contain duplicates.")

print(separator)

###### RESULTS OF A ROUND ######
print(user_attempt)
bulls = []
cows = []
for num in user_attempt:
    if num in pin:
        bulls += 1

print(f"{bulls} bulls") 
        
# i gotta compare user's pin with programm's pin 
# 
if pin[1] is user_attempt[1]:
    cows += 1


