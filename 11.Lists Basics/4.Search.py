total_searches=int(input())
k_word=input()
searches=[]
matches=[]
for _ in range(total_searches):
    new_search=input()
    searches.append(new_search)
print(searches)

for i in range(0,len(searches)):
    if k_word in searches[i]:
        matches.append(searches[i])
print(matches)