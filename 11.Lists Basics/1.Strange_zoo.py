animal=[]
for _ in range(3):
    part=input()
    animal.append(part)
animal[0], animal[2]=animal[2],animal[0]

print(animal)
