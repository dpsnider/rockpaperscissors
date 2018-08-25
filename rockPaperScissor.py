#Rock Paper Scissors
import random
import time

player_score = 0
computer_score = 0

def winner():
    if computer_score == 3:
        print ("You lost best of three...")
    elif player_score == 3:
        print("You won best of three...")
    return;

while player_score < 3 and computer_score < 3:
        #player's choice
    p = input("Enter rock, paper, or scissors:")
    if p == "rock":
        print ("you played rock")
        p = 1
    elif p == "paper":
        print ("you played paper")
        p = 2
    elif p == "scissors":
        print ("you played scissors")
        p = 3
    time.sleep(0)

    #computer's choice
    c = random.randint(1, 3)
    if c ==1:
        print ("computer played rock")
    elif c ==2:
        print ("computer played paper")
    else:
        print ("computer played scissors")
    time.sleep(0)

        #Determine winner of round
    if p == c:
        print ("Tie!")
    elif p == c+1 or p == c-2:
        print ("You Win!")
        player_score += 1
    else:
        print ("You Lose!")
        computer_score +=1
    time.sleep(0)

    #print scores
    print ("computer score = " + str(computer_score))
    print ("player score = " + str(player_score))

    winner()
