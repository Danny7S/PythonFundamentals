coffee_count=0
while True:
    activity=input()
    if activity=='END':
        break
    elif activity.lower()=='coding' \
        or activity.lower()=='cat' \
        or activity.lower()=='dog' \
        or activity.lower()=='movie':
        if activity.islower():
            coffee_count+=1
        elif activity.isupper():
            coffee_count+=2
if coffee_count<=5:
    print(coffee_count)
else:
    print('You need extra sleep')


