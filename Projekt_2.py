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

###### GAME ######
user = input("Enter a number: ")
attempt = list(user)

print(separator)
print(attempt)
bulls = []
cows = []
for num in attempt:
    if num in pin:
        bulls += 1

print(f"{bulls} bulls") 
        
# i gotta compare user's pin with programm's pin 
# 
if pin[1] is attempt[1]:
    cows += 1


