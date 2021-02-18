row1 = row2 = row3 = [0, 0, 0]
board = [row1,
         row2,
         row3]
p1 = 'X'
p2 = 'O'
chance = 0
print(board)
while 0 in (row1 and row2 and row3):
    print('Player ' + str(chance % 2 + 1) + "'s chance")
    co_ord = str(input())
    co_ord = list(co_ord.split(','))
    co_ord = [int(co_ord[0]), int(co_ord[1])]
    if board[co_ord[0]][co_ord[1]] == 0:
        if chance % 2 + 1 is 1:
            board[co_ord[0]][co_ord[1]] = p1
        elif chance % 2 + 1 is 2:
            board[co_ord[0]][co_ord[1]] = p2
        chance = chance + 1
    else:
        print("Choose another co-ordinate!")
    print(board)

print('\n Game Over!')


#------------------------------------------------------------------------------------

row1 = [0, 0, 2]
row2 = [0, 2, 0]
row3 = [2, 0, 0]
game = [row1, row2, row3]
win = 0
x = 0
while x < 3:
    if row1[x] == row2[x] == row3[x] == 1:
        win = 1
    elif row1[x] == row2[x] == row3[x] == 2:
        win = 2
    elif game[x] == [1, 1, 1]:
        win = 1
    elif game[x] == [2, 2, 2]:
        win = 2
    x = x + 1
if row1[0] == row2[1] == row3[2] == 1:
    win = 1
elif row1[0] == row2[1] == row3[2] == 2:
    win = 2
elif row1[2] == row2[1] == row3[0] == 1:
    win = 1
elif row1[2] == row2[1] == row3[0] == 2:
    win = 2

if win != 0:
    print("The winner is Player " + str(win) + '. Congratulations!')
else:
    print("Its a Draw!")

#-------------------------------------------------------------------------------


size = 3
i = 0
ho = " ---"
ve = "|   "
ho = ho * size
ve = ve * (size + 1)
while i < size + 1:
    print(ho)
    if not (i == size):
        print(ve)
    i += 1
