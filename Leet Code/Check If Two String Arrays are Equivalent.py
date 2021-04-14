def arrayStringsAreEqual(word1, word2):
    return ''.join(word1) == ''.join(word2)


print(arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
