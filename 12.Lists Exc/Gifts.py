gifts=input().split()
command = input()
while command !='No Money':
    if 'OutOfStock' in command:
        command=command.split()
        com, attribute=command[0], command[1]
        if len(command)>2:
            for k in range(1,len(command)):
                attribute=command[k]
                if attribute in gifts:
                    for i in range(len(gifts)):
                        if attribute == gifts[i]:
                            gifts[i]=None
        else:
            for i in range(len(gifts)):
                if attribute == gifts[i]:
                    gifts[i]=None

    if 'Required' in command:
        req=command.split()
        value=int(req[2])
        if value<0:
            command = input()
            continue
        if value>len(gifts)-1:
            command = input()
            continue
        gifts[value] = req[1]

    if 'JustInCase' in command:
        command=command.split()
        com, attribute = command[0], command[1]
        guz=gifts.pop()
        gifts.append(attribute)
    command=input()
while True:
    if None in gifts:
        gifts.remove(None)
    else:
        break
while len(gifts)>0:
    print(gifts.pop(0), end=' ')

