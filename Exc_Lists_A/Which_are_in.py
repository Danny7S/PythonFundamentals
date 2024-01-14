words=input().split(', ')
squence=input().split(', ')
new_words=[]
for n in range(len(words)):
    for i in range(len(squence)):
        if words[n] in squence[i]:
            new_words.append(words[n])
            break
print(new_words)