n=int(input())
numbers= [int(input()) for _ in range(n)]
command=input()
filtered_nums=[]
for i in range(0,len(numbers)):
    if command=='even' and numbers[i]%2==0:
        filtered_nums.append(numbers[i])

    if command=='odd' and numbers[i]%2==1:
        filtered_nums.append(numbers[i])

    if command=='negative' and numbers[i]<0:
        filtered_nums.append(numbers[i])

    if command == 'positive' and numbers[i] >= 0:
        filtered_nums.append(numbers[i])
print(filtered_nums)