sent = input('Type the sentence:\n')
wrd = input('Type the word to be counted:\n')
temp_sent = sent.lower()
temp_wrd = wrd.lower()
count = temp_sent.count(temp_wrd)
print('\nCount is : ' + str(count))