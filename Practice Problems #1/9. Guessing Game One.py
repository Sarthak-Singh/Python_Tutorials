import random

a = random.randint(1, 9)

x = 0
response = 'r'
while response != 'exit':
    guess = int(input('Guess a number between 1 and 9 and test your luck! ...\n'))
    if guess < a:
        print('You guessed too low!\n')
    elif guess == a:
        print('You guessed exactly right!\n')
    elif guess > a:
        print('You guessed too high!\n')

    print("Press any key to continue guessing or type 'exit' to exit")
    response = input()
    x = x + 1
    if response == 'exit':
        break

print("No. of guesses taken : " + str(x))
