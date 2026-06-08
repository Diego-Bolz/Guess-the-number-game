import random
attempts = []
guesses = 0
chances = 0
divider = '------------------------------'
difficulty = int(input('\tChoose a difficulty level!\n[1] Easy (1-10)\n[2] Medium (1-50)\n[3] Hard (1-100)\n'))
if difficulty == 1:
     random_number = random.randint(1,10)
elif difficulty == 2:
     random_number = random.randint(1,50)
elif difficulty == 3:
    random_number = random.randint(1, 100)
while guesses != random_number and chances < 5:
    guesses = int(input(f'{divider}\nGuess a number: '))
    attempts.append(guesses)
    chances += 1
    if guesses > random_number:
        print(f'Lower!')
    elif guesses < random_number:
        print(f'Higher!')
if guesses == random_number:
    print(f'{divider}\nCorrect! the random number was {random_number}!')
    print(f'It took you {guesses} attempts!')
else:
    print(f'{divider}\nSorry, but you have reached the maximum of attempts! :(')
print(f'Attempts: {attempts}')
