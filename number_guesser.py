
import random
import sys


def main():

    enter = input("Enter any key once you think of a number remember the number has to be between 1 and 100")
    guess()
    
        




def guess():

    """
    Picks a initial random number then uses binary algorithm to pick the next possible number
    """
    
    
    max_limit = 100
    min_limit = 1
    counter = 0

    while True:

        counter += 1
        num = random.randint(min_limit, max_limit)

        print("Is ", num, " The number you're thinking off?")
        check = input("Y/N:  ")

        if check == 'y' or check == 'Y':
            print("It took the computer ", counter, " attempt to guess your number")
            sys.exit()

        else:
            while True:
                
                resize = input("Is your number greater or smaller than the guessed number?:  ")

                if resize == "greater":
                    min_limit = num +1
                    break

                elif resize == "smaller":
                    max_limit = num -1
                    break

                else:
                    print("invalid input enter either greater or smaller \n")
                    continue
                    
                    
        

    

    
    
print("\t Welcome to the number guesser \n \n")

print(" think of a number between 1 and 100 and i will try to guess it \n")

main()

