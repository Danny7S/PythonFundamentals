positive=[]
negative=[]
even=[]
odd=[]
numbers=[int(i) for i in input().split(', ')]
for i in range(len(numbers)):
    if numbers[i]>=0:
        positive.append(numbers[i])
    if numbers[i]<0:
        negative.append(numbers[i])
    if numbers[i]%2==0:
        even.append(numbers[i])
    else:
        odd.append(numbers[i])
print(f'Positive: '+', '.join([str(i) for i in positive]))
print(f'Negative: '+', '.join([str(i) for i in negative]))
print(f'Even: '+', '.join([str(i) for i in even]))
print(f'Odd: '+', '.join([str(i) for i in odd]))