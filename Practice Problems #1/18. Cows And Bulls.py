import random


rand_gen_num = []
for x in range(4):
    rand_gen_num.append(random.randint(0, 9))
count = 1
print('Choose a 4-digit number :')
guess = input()
guess = list(map(int, str(guess)))
while guess != rand_gen_num:
    cows = 0
    bulls = 0
    for x in range(4):
        if guess[x] in rand_gen_num:
            if guess[x] == rand_gen_num[x]:
                cows = cows + 1
            else:
                bulls = bulls + 1
    count = count + 1
    print("You guessed the number wrong.\nNo. of cows = " + str(cows) + '.\n' 'No. of bulls = ' + str(bulls) + '.\n')
    guess = input('Change your number :\n')
    guess = list(map(int, str(guess)))

print('You guessed the correct number in ' + str(count) + ' guesses!')
