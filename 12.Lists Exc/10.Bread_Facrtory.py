initial_energy=100
initial_coins=100
working_day=input().split('|')
closed=False
for current_work in range(len(working_day)):
    work=working_day[current_work].split('-')
    thing=work[0]
    value=int(work[1])
    if thing=='rest':
        if initial_energy+value>100:
            initial_energy=100
            value=100-initial_energy
            print(f'You gained {value} energy.')
        else:
            initial_energy+=value
            print(f'You gained {value} energy.')
        print(f'Current energy: {initial_energy}.')
    elif thing=='order':
        if initial_energy>=30:
            initial_coins+=value
            initial_energy-=30
            print(f"You earned {value} coins.")
        else:
            initial_energy+=50
            print(f"You had to rest!")
    else:
        if initial_coins>=value:
            initial_coins-=value
            print(f"You bought {thing}.")
        else:
            print(f"Closed! Cannot afford {thing}.")
            closed=True
            break
if closed==False:
    print(f"Day completed!")
    print(f"Coins: {initial_coins}")
    print(f"Energy: {initial_energy}")

