"""

Description: Rock Paper GUI Non-GUI based game

Author: Me

Language: Python3.8

"""

import random

print("\t Welcome to Rock Paper Scissors \n")





def menu():

    while True:
        
        mode = int(input("Enter 1 to play with the computer or 2 to play against another player:  "))

        if mode == 1:
            computer()

        elif mode == 2:
            print("Game mode not available, work in progress... \n")
            continue




def computer():

    ai_score = 0
    player_score = 0

    limit = int(input("Enter winning score:  "))
    print("\n")

    while True:

        if ai_score >= limit or player_score >= limit:

            if ai_score == 3:
                print("\n Computer wins this game... \n")
                break
            elif player_score == 3:
                print("\n Player wins this game... \n")
                break
        
        choice = int(input("Enter 1 for rock, 2 for paper, 3 for scissors:  "))
        ai = random.randint(1,3)

        if choice < 1 or choice > 3:
            print("Invalid input... \n")
            continue
        
        if ai == 1:

            if choice == 1:
                print("Computer: Rock")
                print("Player: Rock \n")
                print("Draw... \n")
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 2:
                print("Computer: Rock")
                print("Player: Paper \n")
                print("Player wins... \n")
                player_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 3:
                print("Computer: Rock")
                print("Player: Scissors \n")
                print("Computer wins... \n")
                ai_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

           
        elif ai == 2:

            if choice == 1:
                print("Computer: Paper")
                print("Player: Rock \n")
                print("Computer wins... \n")
                ai_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 2:
                print("Computer: Paper")
                print("Player: Paper \n")
                print("Draw... \n")
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 3:
                print("Computer: Paper")
                print("Player: Scissors \n")
                print("Player wins... \n")
                player_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

        elif ai == 3:
            
            if choice == 1:
                print("Computer: Scissors")
                print("Player: Rock \n")
                print("Player wins... \n")
                player_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 2:
                print("Computer: Scissors")
                print("Player: Paper \n")
                print("Computer wins... \n")
                ai_score += 1
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

            elif choice == 3:
                print("Computer: Scissors")
                print("Player: Scissors \n")
                print("Draw... \n")
                print("Ai Score: ", ai_score)
                print("Player Score: ", player_score)
                print("---------------------------------------------")
                print("\n")

    menu()

#---------------------------------------------------------
menu()
