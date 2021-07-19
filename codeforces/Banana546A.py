k,n,w=[int(k) for k in input().split()]
price=0
for i in range(1,w+1):
    price=price+(i*k)
if price>n:
    print(price-n)
else:
    print("0")