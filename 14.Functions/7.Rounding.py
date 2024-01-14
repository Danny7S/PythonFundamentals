from math import floor
def rounding(a):
    return round(a)

a=input().split()
b=[]
for i in range(len(a)):
    b.append(rounding(float(a[i])))

print(b)