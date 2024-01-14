number = list(map(int, input().split()))
# number_w = number.copy()
# number_w.sort(reverse=True)
# big_league = []
n = int(input())
# for i in range(n):
#     number_w.pop()
# for j in range(len(number)):
#     if number[j] in number_w:
#         number.remove(number[j])
# while len(number) > 0:
#     print(number.pop(0), end=', ')
# print(number.pop())
for _ in range(n):
    number.remove(min(number))
while len(number) > 1:
     print(number.pop(0), end=', ')
print(number.pop())