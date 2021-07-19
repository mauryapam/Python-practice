"""Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and 
last elements of the given list. For practice, write this code inside a function."""

def MoreLists():
    a = [5, 10, 15, 20, 25]
    # b=[el for el in a]
    b=[]
    b.append(a[0])
    b.append(a[len(a)-1])
    print(b)
MoreLists()

# def list_ends(a_list):
#     return [a_list[0], a_list[len(a_list)-1]]