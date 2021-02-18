def max_of_three(x, y, z):
    if z > x and z > y:
        print(z)
    elif y > x and y > z:
        print(y)
    elif x > z and x > y:
        print(x)
    elif z == y > x or z == x > y:
        print(z)
    elif z == y > x or y == x > z:
        print(y)
    elif x == y > z or z == x > y:
        print(x)
    else:
        print(x)


max_of_three(4, -1, 0)
