deck=input().split()
num_of_shufles=int(input())

for _ in range(num_of_shufles):
    mid=len(deck)//2
    right_part=deck[0:mid]
    left_part=deck[mid:]
    deck.clear()
    for i in range(len(left_part)):
        deck.append(right_part.pop(0))
        deck.append(left_part.pop(0))
print(deck)