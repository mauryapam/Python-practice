n,h=[int(n) for n in input().split()]
a=[int(a) for a in input().split()]
width=0
for i in a:
    w=i
    if w<=h:
        width+=1
    else:
        width+=2
print(width)