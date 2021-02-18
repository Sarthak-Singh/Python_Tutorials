row1 = row2 = row3 = [0, 0, 0]
board = [row1,
         row2,
         row3]
p1 = 'X'
p2 = 'O'
chance = 0
print(board)
while 0 in (row1 or row2 or row3):
    print('Player ' + str(chance % 2 + 1) + "'s chance")
    co_ord = input().strip().split(',')
    co_ord = list(map(int, co_ord))
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
