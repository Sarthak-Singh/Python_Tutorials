w1 = input('Enter the first word:\n')
w2 = input('Enter the second word:\n')
w3 = ''
mid = int(len(w1)/2)
w3 = w3 + w1[:mid] + w2 + w1[mid:]
print(w3)
