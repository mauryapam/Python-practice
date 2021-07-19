"""Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that
 they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)"""

name=input('Enter your name : ')
age= int(input('Enter your age : '))
year= (2021-age)+100

#print(f"{name} will turn 100 years old in year {year} \n")
msg=f"{name} will turn 100 years old in year {year}"
print(msg)

no_of_copies=int(input('Enter how many copies you want of the msg : '))
print(msg*no_of_copies)
for i in range(no_of_copies):
    print(msg)

