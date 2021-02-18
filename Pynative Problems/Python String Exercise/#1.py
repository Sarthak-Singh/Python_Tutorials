word = input('Enter a word of more than 7 and odd no. of characters:\n')
mid = int(len(word)/2)
if len(word) % 2 != 0:
    print(word[mid-1] + word[mid] + word[mid+1])
else:
    print(word[mid-1] + word[mid])
