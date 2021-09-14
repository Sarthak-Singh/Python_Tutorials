def decode(encoded, first):
    arr = [first]*(len(encoded) + 1)
    for x in range(len(encoded)):
        arr[x+1] = encoded[x] ^ arr[x]
    return arr


print(decode([6,2,7,3], 4))
