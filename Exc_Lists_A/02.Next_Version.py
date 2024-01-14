next_version=input().split('.')
version=0
new=[]
for n in range(len(next_version)):
    version+=10**(2-n)*int(next_version[n])
version+=1
new=[i for i in str(version)]
print('.'.join(new))

