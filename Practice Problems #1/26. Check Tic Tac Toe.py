row1 = [1, 0, 0]
row2 = [0, 1, 0]
row3 = [0, 0, 1]
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
