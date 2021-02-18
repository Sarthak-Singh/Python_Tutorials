w1 = input('Enter the first word:\n')
w2 = input('Enter the second word:\n')
w3 = ''
mid1 = int(len(w1)/2)
mid2 = int(len(w2)/2)
w3 = w3 + w1[0] + w2[0] + w1[mid1] + w2[mid2] + w1[-1] + w2[-1]
print(w3)
