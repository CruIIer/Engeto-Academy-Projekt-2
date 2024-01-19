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
    
    
###### CREATING 4 DIGITS result_pin CODE ######
def generate_pin():
    result_pin = []
    result_pin.append(randint(1,9))
    while len(result_pin) != 4:
        num = randint(0, 9)
        if num not in result_pin:
            result_pin.append(num)
    return result_pin


###### USER'S result_pin ######
def users_attempt_pin():
    while True:
        user_pin = input("Enter your number: ")
        if len(user_pin) != 4:
            print("Your result_pin must contain 4 digits.")
        if user_pin[0] == "0":
            print("Your result_pin can't start with 0.")
        if not user_pin.isnumeric():
            print("Your result_pin must contian numbers only.")
        if len(set(user_pin)) != len(user_pin):
            print("Your result_pin can't contain duplicates.")
        else:
            return user_pin
    
print(separator)

###### RESULTS OF A ROUND ######
def round_results():
    result_pin = generate_pin()
    user_pin = [int(num) for num in user_pin]
    bulls = 0
    cows = 0
    
    for num_pc, num_user in zip(result_pin, user_pin):
        if num_pc in user_pin:
            if num_pc == num_user:
                bulls += 1
            else:
                cows += 1
    return result_pin, user_pin, bulls, cows



 









 








