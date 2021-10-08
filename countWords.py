intro = input('Enter Your Introduction : ')
charecterCount = 0
wordCount = 1

for i in intro :
    charecterCount += 1
    if (i == ' '):
        wordCount += 1

print(charecterCount)
print(wordCount)