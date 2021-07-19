def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x//y

print("calculate \1. Addition \2.Substraction \3.Multiplication \4.Division")

ch= input("Enter your choice : ")
n1 = float(input("First number : "))
n2 = float(input("Second number : "))
if ch=="1":
    print(n1+" + " +n2+" : "+add(n1, n2))
elif ch=="2":
    print(n1+" - " +n2+" : "+sub(n1, n2))
elif ch=="3":
    print(n1+" * " +n2+" : "+mul(n1,n2))
elif ch=="4":
    print(n1+" / " +n2+" : "+div(n1,n2))
else:
    exit()
