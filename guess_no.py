import random

print('Welcome to Guess The Number game!')
top_range = input('Enter the number for me to make the guess: ')
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print('Enter a valid number greater than 0 next time..')
        quit()
else:
    print('Enter a valid number next time')
    quit()

random_number = random.randint(0, top_range)
guesses = 0

while True: # to run infinitely
    guesses += 1
    user_guess = input('Enter your guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a valid number')
        continue # to move the control back to beginning while statement

    if user_guess == random_number:
        print('My Mahnn!')
        break
    else:
        if user_guess < random_number:
            print('You were below the number!')
        elif user_guess > random_number:
            print('You were above the number!')

print('You got it in', guesses, 'guesses')