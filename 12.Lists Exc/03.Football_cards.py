team_a_ejected=[]
team_b_ejected=[]

cards=input().split()
for i in range(len(cards)):
    if 'A' in cards[i]:
        team, number=cards[i].split('-')
        number=int(number)
        if  number<1 or number>11:
            continue
        if number not in team_a_ejected:
            team_a_ejected.append(number)
    if 'B' in cards[i]:
        team, number=cards[i].split('-')
        number=int(number)
        if  number<1 or number>11:
            continue
        if number not in team_b_ejected:
            team_b_ejected.append(number)

print(f"Team A - {11-len(team_a_ejected)}; Team B - {11-len(team_b_ejected)}")
if len(team_a_ejected)>4 or len(team_b_ejected)>4:
    print('Game was terminated')
