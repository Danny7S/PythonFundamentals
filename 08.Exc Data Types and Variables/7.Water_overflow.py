number_of_tries=int(input())
capacity=255
for _ in range(number_of_tries):
    water_amount=int(input())
    if water_amount>capacity:
        print('Insufficient capacity!')
    else:
        capacity-=water_amount
print(255-capacity)