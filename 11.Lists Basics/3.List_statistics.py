num_count=int(input())
p_numbers=[]
n_numbers=[]
for i in range(num_count):
    current_num=int(input())
    if current_num<0:
        n_numbers.append(current_num)
    else:
        p_numbers.append(current_num)
print(p_numbers)
print(n_numbers)
print(f'Count of positives:', len(p_numbers))
print(f'Sum of negatives:', sum(n_numbers))

