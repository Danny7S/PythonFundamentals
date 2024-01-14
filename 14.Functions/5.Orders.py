def order(type,quantity):
  price=0
  if type=='coffee':
   price=1.50
  elif type=='water':
   price=1.00
  elif type == 'coke':
   price = 1.40
  elif type=='snacks':
   price=2.00
  return quantity*price

order_o=input()
times=int(input())
print(f'{order(order_o,times):.2f}')