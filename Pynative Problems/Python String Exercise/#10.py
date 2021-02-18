inputStr = "pynativepynvepynative"
countDict = dict()
for char in inputStr:
    count = inputStr.count(char)
    countDict[char] = count
print(countDict)
