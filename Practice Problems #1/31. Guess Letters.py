print('Welcome to Hangman!')
print('Guess The Word!')
wrd = 'EVAPORATE'
word = list(wrd)
length = len(word)
disp = '_ ' * length
while '_' in disp:
    print(disp)
    guess = input("Enter any alphabet :\n")
    disp = list(disp)
    if guess in word:
        print('You Got A Right Alphabet!')
        x = 0
        while x < length-1:
            if word[x] == guess:
                disp[(x*2)] = guess
            else:
                pass
        x = x + 1
    else:
        print('Incorrect Alphabet!')
    new = ''
    new = new.join(disp)
    disp = new

print('The Word is :' + wrd)
