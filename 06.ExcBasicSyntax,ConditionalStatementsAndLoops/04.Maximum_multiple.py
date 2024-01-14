devisor=int(input())
boundary=int(input())
for current_num in range(boundary, devisor, -1):
    if current_num%devisor==0:
        print(current_num)
        break