word=input()
reverse=''
for i in range(len(word)):
    reverse=word[i]+reverse
print(reverse)