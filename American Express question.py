import random


def solution(riddle):
    L = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
         'n','o','p','q','r','s','t','u','v','w','x','y','z']

    for x in riddle:
        if x == '?':
            a = random.randint(0, 25)
            letter = L[a]
            riddle = riddle.replace('?', letter, 1)
    print(riddle)


solution('?????')
