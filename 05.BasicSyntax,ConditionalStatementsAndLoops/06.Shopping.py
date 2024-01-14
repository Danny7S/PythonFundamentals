budget=int(input())
total=0
while True:
    amount=input()
    if amount=='End':
        print("You bought everything needed.")
        break
    amount=int(amount)
    if total+amount>budget:
        print('You went in overdraft!')
        break
    total=total+amount
