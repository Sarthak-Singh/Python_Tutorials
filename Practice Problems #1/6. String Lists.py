word = input("Enter a word :\n")

letters = list(word)
count = len(letters)

x = 0
while x < count:
    if letters[x] is letters[count - x - 1]:
        x = x + 1
    else:
        print("This word is NOT a palindrome !")
        break

if x is count:
    print("This word is a palindrome !")
