s=input()
t=input()
if len(s)==len(t) and s[::-1]==t:
    print("YES")
else:
    print("NO")