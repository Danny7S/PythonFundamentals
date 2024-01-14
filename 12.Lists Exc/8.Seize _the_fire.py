# High = 89#Low = 28#Medium = 77#Low = 23
# 1250
fires=input().split('#')
water_supply=int(input())
effort=0
put_out_cells=[]

for cells in range(len(fires)):
    # type, amount_of_fire=fires[cells][0],int(fires[cells][1])
    current_fire=fires[cells].split(' = ')
    current_fire_scale=current_fire[0]
    current_fire_power=int(current_fire[1])
    if water_supply<current_fire_power:
        continue
    else:
        if current_fire_scale=='High' and 81<=current_fire_power<=125:
            water_supply-=current_fire_power
            effort+=1/4*current_fire_power
            put_out_cells.append(current_fire_power)
        elif current_fire_scale=='Medium' and 51<=current_fire_power<=80:
            water_supply-=current_fire_power
            effort+=1/4*current_fire_power
            put_out_cells.append(current_fire_power)
        elif current_fire_scale == 'Low' and 1 <= current_fire_power <= 50:
            water_supply -= current_fire_power
            effort += 1 / 4 * current_fire_power
            put_out_cells.append(current_fire_power)
print('Cells:')
for j in range(len(put_out_cells)):
    print(f' - {put_out_cells.pop(0)}')
print(f'Effort: {effort:.2f}')
print(f'Total Fire: {effort*4:.0f}')



