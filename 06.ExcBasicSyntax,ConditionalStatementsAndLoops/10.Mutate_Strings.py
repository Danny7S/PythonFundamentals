string_one=input()
string_two=input()
new=string_one
char1=''
char2=''
for i in range(len(string_one)):
    if new[i] != string_two[i]:
        new=string_two[:i+1]+new[i+1:]
        print(new)
    else:
        continue


