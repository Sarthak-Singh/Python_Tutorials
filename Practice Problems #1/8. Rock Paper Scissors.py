print("Welcome to Rock , Paper & Scissor !")
print("Choose your weapon.")
print("r = rock , p = paper , s = scissor")

response = 'y'
result = 3


def rule(x, y):
    global result
    if (x == 'r' and y == 'p'):
        result = 2
    elif (x == 'p' and y == 'r'):
        result = 1
    elif (x == 'r' and y == 's'):
        result = 1
    elif (x == 's' and y == 'r'):
        result = 2
    elif (x == 's' and y == 'p'):
        result = 1
    elif (x == 'p' and y == 's'):
        result = 2
    elif (x == y):
        result = 0
    else:
        print("Enter valid responses!")


while response == 'y':
    p1 = input("Player 1, Enter your Choice :\n")
    p2 = input("Player 2, Enter your Choice :\n")

    rule(p1, p2)
    if result is 0:
        print('Its a draw!\n')
    elif result is 1:
        print('Player 1 WINS!\n')
    elif result is 2:
        print('Player 2 WINS!\n')

    print("Press 'y' to play again and 'n' to stop playing.")
    response = input()

    while response != ('y' or 'n'):
        if response == 'n':
            break
        elif response != 'y':
            print('Enter a valid command!')
            print("Press 'y' to play again and 'n' to stop playing.")
            response = input()
