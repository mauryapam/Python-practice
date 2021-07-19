n =int(input())
count=0
for i in range(n):
    sum=0
    a,b,c=[int(a) for a in input().split()]
    
    sum=a+b+c
    if sum>=2:
        count+=1
print(count)




