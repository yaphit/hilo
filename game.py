from random import randint


def is_valid(user_guess):
    try:
        temp = int(user_guess)
        if temp > 100 or temp < 1:
            return "Please enter a number between 1 and 100!!!"
        return guess_a_number(temp)
    except ValueError:
        return "Please enter a number!"


def guess_a_number(int_guess):
    if int_guess > number:
        return "Too High - try again!"
    elif int_guess < number:
        return "Too Low - try again!"
    else:
        return f"Got it!: The number is {number}"


print('Welcome to the Hi - Lo game')
number = randint(1, 100)

while True:
    guess = is_valid((input('Guess a number between 1 and 100 :')))
    print(guess)
    if "Got it" in guess:
        break
