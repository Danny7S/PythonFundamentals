first_char=int(input())
last_char=int(input())

for i in range(first_char,last_char+1):
    if i!=last_char:
        print(f'{chr(i)}' , end=' ')
    else:
        print(f'{chr(i)}')