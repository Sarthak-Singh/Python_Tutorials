def restoreString(s, indices):
    new = ['']*len(s)
    for x in range(len(indices)):
        new[indices[x]] = s[x]
    return ''.join(new)


print(restoreString("aaiougrt", [4,0,2,6,7,3,1,5]))
