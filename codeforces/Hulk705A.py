n=int(input())
s=''
for i in range(1,n+1):
    if i==1:
        s+='I hate '
    elif i%2==0:
        s+='that I love '
    else:
        s+='that I hate '
print(s+'it')