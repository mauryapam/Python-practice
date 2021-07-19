a=input()
b=input()
res=""
for i,j in zip(a,b):
    if i == j:
        res+=str('0')
    else:
        res+=str('1')

print(res)

