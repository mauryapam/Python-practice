"""Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message
 to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides
 evenly into num, tell that to the user. If not, print a different appropriate message."""

num=int(input('Enter a number :'))
if num%2==0 and num%4==0:
    print('Its a even number and Number is divisible by 4')

# elif num%4==0:
#     print('Number is divisible by 4')

else:
    print('Its a odd number')

check=int(input('Enter a check number : '))

if num%check==0:
    print(f'{num} is completely divisble by {check}')
else:
    print(f'{num} is not divisble by {check}')