n=int(input())
s=input()
# countA=0
# countD=0
# for i in range(len(s)):
#     if s[i]=="A":
#         countA+=1
#     else:
#         countD+=1
# if countA>countD:
#     print("Anton")
# elif countA<countD:
#     print("Danik")
# else:
#     print("Friendship")

d=n-s.count('A')
if d<s.count('A'):
    print("Anton")
elif d>s.count('A'):
    print("Danik")
else :
    print("Friendship")