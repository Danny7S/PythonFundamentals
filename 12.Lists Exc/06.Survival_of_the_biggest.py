# from sys import maxsize
# num = input().split()
# counter=-maxsize
# big=int(input())
# big_league=[]
# mmm=num.pop()
# for i in range(big):
#     num=num.sort()
#     mmm=num.pop()
#     big_league.append(mmm)
# print(big_league)
number_line = input().split()
number_line=number_line.sort(reverse=True)
n=int(input())
big_league=[]
for i in range(n):
    big_league.append(number_line[i])
print(big_league)
