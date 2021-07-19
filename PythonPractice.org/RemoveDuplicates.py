"""Write a program (function!) that takes a list and returns a new list that contains all the elements of the first 
list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets."""

lst=[]
# newlst=[]

for i in range(10):

    a=int(input())
    lst.append(a)
# def RemoveDupli(lst):
#     for i in lst:
#         if i not in newlst:
#             newlst.append(i)
# RemoveDupli(lst)
# print(newlst)


newset=set()
def UsingSets(lst):
    for i in lst:
        newset.add(i)

UsingSets(lst)
print(list(newset))
