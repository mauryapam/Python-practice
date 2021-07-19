n=int(input('Enter a number : '))
# a = [x for x in range(2, num) if num % x == 0]
for i in range(2,n):
    if n%i==0:
        print("Number is not prime")
        break
else:
    print("Number is prime")
    



