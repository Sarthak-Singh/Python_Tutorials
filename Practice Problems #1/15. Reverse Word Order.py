def reverse(x):
    words = x.split()
    length = len(words)
    rev_words = []
    y = 0
    while y < length:
        rev_words.append(words[length-1-y])
        y = y + 1

    new_sentence = " ".join(rev_words)
    print(new_sentence)


original_sentence = input("Enter any sentence to reverse it! : \n")
reverse(original_sentence)
