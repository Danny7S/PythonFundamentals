"Not enough money."
items=input().split('|')
budget=float(input())
profits=[]
total_price=0
for i in range(len(items)):
    current_item=items[i].split('->')
    item=current_item[0]
    price=float(current_item[1])
    if price>budget:
        continue
    if item=='Clothes' and 0<price<=50.00:
        total_price+=price
        budget-=price
        profits.append(round(price*1.4,2))
    elif item=='Shoes' and 0<price<=35.00:
        total_price += price
        budget-=price
        profits.append(round(price*1.4,2))
    elif item=='Accessories' and 0<price<=20.50:
        total_price += price
        budget-=price
        profits.append(round(price*1.4,2))
profit=sum(profits)-total_price
while len(profits)>1:
    print(profits.pop(0), end=' ')
print(profits.pop(0))
print(f"Profit: {profit:.2f}")
if profit+budget+total_price>=120:
    print("Hello, France!" )
else:
    print("Not enough money.")
