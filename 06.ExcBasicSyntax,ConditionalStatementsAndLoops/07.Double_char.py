while True:
    new=''
    repeat=input()
    if repeat=='End':
        break
    elif repeat=='SoftUni':
        continue
    for i in range(len(repeat)):
        new+=2*repeat[i]
    print(new)

