from math import ceil
num_of_people=int(input())
el_capacity=int(input())
num_of_turns=ceil(num_of_people / el_capacity)

print(num_of_turns)

