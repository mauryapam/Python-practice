"""Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of 
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock"""


p1=input('Player 1 : Enter your name: ')
p2=input('Player 2 : Enter your name: ')

gameon=input('Are you ready for Rock, Paper, Scissors game ?(y/n) : ')

p1_wins=0
p2_wins=0
draw=0


def game(p1_choice,p2_choice):
    global p1_wins,p2_wins,draw
    if p1_choice==p2_choice:
        print("Match draws")
        draw+=0

    elif p1_choice=="Rock":
        if p2_choice=="Scissors":
            print(f"{p1} wins")
            p1_wins+=1
        else:
            print(f"{p2} wins")
            p2_wins+=1

    elif p1_choice=="Scissors":
        if p2_choice=="Paper":
            print(f"{p1} wins")
            p1_wins+=1
        else:
            print(f"{p2} wins")
            p2_wins+=1

    elif p1_choice=="Paper":
        if p2_choice=="Rock":
            print(f"{p1} wins")
            p1_wins+=1
        else:
            print(f"{p2} wins")
            p2_wins+=1

    else:
        print("Invalid choice")

while gameon=='y':
    
    p1_choice=input(f'{p1}: Enter your choice : ')
    p2_choice=input(f'{p2}: Enter your choice : ')

    game(p1_choice,p2_choice)

    another_game=input('Want to play again?(y/n) : ')
    gameon=another_game

if gameon=='n':
    print('player 1 wins : ',p1_wins,'\tplayer 2 wins : ',p2_wins,'\tdraw matches : ',draw)
