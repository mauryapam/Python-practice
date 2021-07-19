"""Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in 
the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” 

Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. 
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end."""

# import random
# gameon=True
# def CowsBulls(num,guess):
#     for i,j in zip(range(len(num)),range(len(guess))):
#         cows=bulls=0
#         if num[i]==guess[j]:
#             cows+=1
#         elif num[i]!=guess[j] and num[i] in guess:
#             bulls+=1
#         else:
#             pass
#     return str(cows)+' cows,'+str(bulls)+' bulls'


# if __name__=="__main__":
#     random_num=random.randint(1000,9999)

#     while gameon:
        
#         user_guess = input("Give me a number: ")
#         if user_guess=='exit':
#             break
#         else:
#             print(CowsBulls(str(random_num),user_guess))
#             print(random_num)
        
import random

n = str(random.randint(1000,9999))
nlist = []
cow = 0
for i in n:
    nlist.append(i)

while cow < 4 and exit !="x":
    x = str(input("Choose a 4 digit number, x to exit: "))
    xlist = []
    cow = 0
    bull = 0
    if x!= "x":
        for i in x:
            xlist.append(i)
        for i in nlist:
            if i in xlist and nlist.index(i) == xlist.index(i):
                cow +=1
            if i in xlist and nlist.index(i) != xlist.index(i):
                bull +=1
        print(cow, "cow(s)", bull, "bull(s)")
    else:
        exit = "x"

print(nlist, xlist)