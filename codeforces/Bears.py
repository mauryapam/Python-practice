a,b=[int(a) for a in input().split()]
county=0
while a<=b:
    a=a*3
    b=b*2
    county+=1
print(county)