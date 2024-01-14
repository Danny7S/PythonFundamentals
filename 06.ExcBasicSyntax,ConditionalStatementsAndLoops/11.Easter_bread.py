budget = float(input())
flour_price = float(input())
eggs = 3/4*flour_price
liter_of_milk = 125/100*flour_price
milk = 0
flour = 0
packs_of_eggs = 0
bread = 0
colored_eggs_count = 0
while True:
    if milk == 0:
        if budget-liter_of_milk < 0:
            break
        else:
            budget=budget-liter_of_milk
            milk=4
    if packs_of_eggs==0:
        if budget-eggs<0:
            if  milk==4:
                budget+=liter_of_milk
            break
        else:
            budget=budget-eggs
            packs_of_eggs=1
    if flour==0:
        if budget-flour_price<0:
            budget+=liter_of_milk+eggs
            break
        else:
            budget=budget-flour_price
            flour=1
    bread+=1
    flour=flour-1
    packs_of_eggs=packs_of_eggs-1
    milk=milk-1
    if bread%3==0:
        colored_eggs_count+=3
        colored_eggs_count=colored_eggs_count-(bread-2)
    else:
        colored_eggs_count+=3
print(f'You made {bread} loaves of Easter bread! Now you have {colored_eggs_count} eggs and {budget:.2f}BGN left.')