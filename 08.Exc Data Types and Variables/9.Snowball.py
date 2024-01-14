number_of_snowballs=int(input())
best_snowball=0
weight_best_snowball=0
time_best_snowball=0
quality_best_snowball=0


for _ in range(number_of_snowballs):
    weight = int(input())
    time = int(input())
    quality = int(input())
    current_score=(weight/time)**quality
    if current_score>best_snowball:
        best_snowball=current_score
        weight_best_snowball=weight
        time_best_snowball=time
        quality_best_snowball=quality
print(f'{weight_best_snowball} : {time_best_snowball} = {best_snowball} ({quality_best_snowball})')