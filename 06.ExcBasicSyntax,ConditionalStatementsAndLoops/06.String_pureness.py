num_of_str=int(input())
for i in range(num_of_str):
    string_check=input()
    if ',' in string_check or'.' in string_check or '_' in string_check:
        print(f'{string_check} is not pure!')
    else:
        print(f'{string_check} is pure.')