n=int(input())
count=0
magnet='00'
for i in range(n):
    a=input()
    if magnet!= a:
        count+=1
        magnet=a

print(count)
