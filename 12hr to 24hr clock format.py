a = input()
time = ''
if 'PM' in a:
    if int(a[0:2]) != 12:
        time += str(int(a[0:2])+12)
    else:
        time += str(int(a[0:2]))
    for x in range(2, 8):
        time += a[x]
elif 'AM' in a:
    if int(a[0:2]) == 12:
        time += '00'
    elif int(a[0:2]) < 10:
        time += '0' + str(int(a[0:2]))
    else:
        time += str(int(a[0:2]))
    for x in range(2, 8):
        time += a[x]
print(time)
