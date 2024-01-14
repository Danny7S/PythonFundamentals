values=input().split()

new_values=[]

for num in range(len(values)):
    values[num]=-int(values[num])
print(values)