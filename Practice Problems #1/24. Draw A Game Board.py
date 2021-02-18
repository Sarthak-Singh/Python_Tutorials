def draw_board(size):
    size = int(size)
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


size_b = int(input('Enter the size of required board :\n'))
draw_board(size_b)
