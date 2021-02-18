sent = 'Emma is a good developer. Emma is also a writer.'
count = 0
for i in range(len(sent)-1):
    if sent[i:i+4] == 'Emma':
        count = count + 1

print(count)
