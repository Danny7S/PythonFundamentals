num=int(input())
sum=0
for _ in range(num):
    char=input()
    sum+=ord(char)
print(f"The sum equals: {sum}")