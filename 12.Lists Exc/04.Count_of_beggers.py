# money=input()
# kloshar_count=int(input())
# print(money)
# each_kloshars_money=[]
# for current_kloshar in range(kloshar_count):
#     current_kloshar_money=0
#     for i in range(current_kloshar,len(money),kloshar_count):
#         current_kloshar_money+=money[i]
#     each_kloshars_money.append(current_kloshar_money)
# print(each_kloshars_money)
money=input().split(', ')
kloshar_count=int(input())
monn=[]
for cur_kl in range(kloshar_count):
    mon_cur_klosh=0
    for i in range(cur_kl,len(money), kloshar_count):
        money[i]=int(money[i])
        mon_cur_klosh=mon_cur_klosh+money[i]
    monn.append(mon_cur_klosh)
print(monn)