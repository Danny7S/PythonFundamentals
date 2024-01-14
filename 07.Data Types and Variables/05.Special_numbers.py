num=int(input())

calc=0
new_i=0
for i in range(1,num+1):
    new_i=i
    while new_i /10>=1:
      calc=calc+i%10
      new_i=int(new_i/10)
    calc=calc+new_i%10

    if calc==5 or calc==7 or calc==11:
        print(f'{i} -> True')
    else:
        print(f'{i} -> False')
    calc=0






















# num=int(input())
# for i in range(1,num+1):
#     string_num=str(i)
#     for digit in string_num:
#         if string_num.count(digit)>1:
#             continue:
#         else:
#             print(f'{i} ')
