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
while len(pin) != 4:
    num = randint(0, 9)
    if num not in pin:
        pin.append(num)

print(pin)

""" can't start with zero -_- """



