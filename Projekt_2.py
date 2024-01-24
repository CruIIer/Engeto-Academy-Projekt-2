"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

autor: Aleš Preclík
email: apreclik@centrum.cz
discord: alda_p
"""


from random import randint
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


###### USER'S PIN ######
def users_attempt_pin():
    while True:
        user_pin = input("Enter your number: ")
        if len(user_pin) != 4:
            print("Your number must contain 4 digits.")
        elif user_pin[0] == "0":
            print("Your number can't start with 0.")
        elif not user_pin.isnumeric():
            print("Your number must contian numbers only.")
        elif len(set(user_pin)) != len(user_pin):
            print("Your number can't contain duplicates.")
        else:
            return [int(num) for num in user_pin]
    

###### RESULTS OF A ROUND ######
result_pin = generate_pin()
def round_results(result_pin):
    user_pin = users_attempt_pin()
    bulls = 0
    cows = 0
    
    for num_pc, num_user in zip(result_pin, user_pin):
        if num_pc == num_user:
            bulls += 1
        elif num_user in result_pin:
            cows += 1
    return result_pin, user_pin, bulls, cows


###### SHOWING RESULTS ######
guess_count = 0
rating_ranges = [(1, 2, "awesome!"), (3, 5, "pretty good!"), (6, 8, "average!"), (9, float('inf'), "quite bad, try again!")]

def show_results(result_pin, user_pin, bulls, cows, guess_count):
    print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, {cows} {'cow' if cows == 1 else 'cows'} \n{separator}")
    if bulls == 4:
        rating_scale = next((rating for lower, upper, rating in rating_ranges if lower <= guess_count <= upper))
        print(f"Correct, you've guessed the right number in {guess_count} guesses. That's {rating_scale}")
        
while True:
    result_pin, user_pin, bulls, cows = round_results(result_pin)
    show_results(result_pin, user_pin, bulls, cows, guess_count)
    guess_count += 1
    if bulls == 4:
        break


