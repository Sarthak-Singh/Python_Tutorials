response = str
x = 0
y = 100
guess = x+y/2
counter = 1
while response != 'e':
    print('Is your number ' + str(int(guess)) + ' ?')
    print('If your number is:\nEqual to the guess, type e\n'
          'Smaller than the guess, type s\nGreater than the guess, type g')
    response = input()
    if response == 'e':
        break
    elif response == 's':
        y = guess
        guess = (x + guess) / 2
    elif response == 'g':
        x = guess
        guess = (y + guess) / 2
    else:
        print("Enter a valid response !")
    counter = counter + 1
print('So your number is ' + str(guess) + '.')
print('No. of guesses taken = ' + str(counter) + ' !')
