def interpret(command):
    ans = ''
    x = 0
    while x < len(command):
        if command[x] == '(':
            if command[x+1] == ')':
                ans += 'o'
                x += 2
            else:
                ans += 'al'
                x += 4
        else:
            ans += command[x]
            x += 1
    return ans


print(interpret("(al)G(al)()()G"))
