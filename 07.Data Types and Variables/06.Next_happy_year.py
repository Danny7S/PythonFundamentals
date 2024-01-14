num=int(input())
happy=1
while happy>0:
    happy=0
    string_num=str(num)
    for digit in string_num:
        if string_num.count(digit)<=1:
            happy += 0
        else:
            happy+=1
    num+=1
string_num=num-1
print(f'{string_num}')

