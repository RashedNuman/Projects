
import turtle
import sys
import random
import time

#turtle = turtle.Turtle()
#screen = turtle.getscreen()

def get_word():


    words = dict()

    word_list = ["airplane", "monopoly", "jetski", "server", "computer", "friends", "money", "girlfriend", "banana"]
    desc_list = ["Flying object, carries people", "board game that teaches you capitalism", "motorcycle on water", "device that hosts content for you", "device that does everything", "people you hang out with", "paper that gets you anything", "something you can never get :)", "weird boneless yellow thing"]

    #cleaner implementation isntead of the pile of shit below it, uses tuples instead, this method reduces the code by about 6 lines
    length = len(word_list) -1 # word_list and desc_list have the same size so it doesnt matter
    random_num = random.randint(0, length)
    word_hint = (word_list[random_num], desc_list[random_num])
    return word_hint




def draw_hangman(lives):

    """
    draws the hangman with different missing limbs depending on failed attempts,
    not called in the called yet
    """

    turtle.speed(7)
    turtle.penup()
    turtle.clear()
    turtle.home()

    if lives == 6:
        
        turtle.pensize(7)
        turtle.penup()
        turtle.left(90)
        turtle.forward(250)
        turtle.pendown()
        turtle.dot(70)
        turtle.right(180)
        turtle.forward(40)
        turtle.pensize(5)
        turtle.right(45)
        turtle.forward(150)
        turtle.right(180)
        turtle.forward(150)
        turtle.right(45)
        turtle.right(45)
        turtle.forward(150)
        turtle.left(180)
        turtle.forward(150)
        turtle.left(135)
        turtle.pensize(6)
        turtle.forward(175)
        turtle.left(15)
        turtle.pensize(5)
        turtle.forward(140)
        turtle.right(180)
        turtle.forward(140)
        turtle.left(155)
        turtle.forward(140)

    if lives == 5:
        
        turtle.pensize(7)
        turtle.penup()
        turtle.left(90)
        turtle.forward(250)
        turtle.pendown()
        turtle.dot(70)
        turtle.right(180)
        turtle.forward(40)
        turtle.pensize(5)
        turtle.right(45)
        turtle.forward(150)
        turtle.right(180)
        turtle.forward(150)
        turtle.right(135)
        turtle.pensize(6)
        turtle.forward(175)
        turtle.left(15)
        turtle.pensize(5)
        turtle.forward(140)
        turtle.right(180)
        turtle.forward(140)
        turtle.left(155)
        turtle.forward(140)
        

def list_to_text(mylist):

    word = ''

    for i in mylist:

        word += " " + i

    return word

    

def game():

    print("-" * 100)
    print(" \t \t \t \t Welcome to hangman \n")

    #print("The objective is to guess the word given by the computer and you lose chances as you pick wrong letters.\n There are no hints cause thats pussy shit, but the words are simple so dont be a lil bitch"


    word_hint = get_word()
    word = word_hint[0]
    hint = word_hint[1]

    print("\n Generating a word for you :) \n")
    time.sleep(2)

    size = len(word)

    letters = list()


    for i in range(size):

        letters.append('__')
    

    hangman_word = ''

    for i in letters:

        hangman_word += " " + i

    lives = 6

    #draw_hangman(lives)

    print("Word Description: ", hint, "\n \n")

    print( list_to_text(letters) + "\n \n")
    
    used_letters = set()

    while True:

        counter = len(set(word))
        letter_counter = 0
        
        for i in used_letters:

            if i in word:
                letter_counter += 1

            if letter_counter == counter:
                print("\n \t You have figured out the word! \n")
                end_menu = (input("play again or exit? P/E :  "))

                if end_menu == "p" or end_menu == "P":
                    print("\n" * 10 )
                    game()

                else:
                    exit()

        if lives == 0:  #if player has no lvies left he loses the gmae, it exists
                print(" \t \t \t GAME OVER \n")
                print("You have no Lives left, git gud trash")
                print(" \n the word was", word,)

                end_menu = str(input("Retry or exit ? R/E :  "))

                if end_menu == "R" or end_menu == "r":
                    
                    print("\n" *10)
                    game()

                else:
                    print("Thanks for playing dipshit")
                    sys.exit()

                
        user_input = str(input("enter a letter:  "))

        if user_input in used_letters:
            print("You have allready used this letter... \n")
            continue

        if user_input in word:


            for index, letter in enumerate(word):
                   
                if user_input.lower() == letter:
                   
                    letters[index] = user_input.upper()
                    used_letters.add(user_input)
            
        else:

            if user_input in used_letters:
                
                print("You have allready used this letter... \n")
                continue
            
            used_letters.add(user_input)
            print("The Letter doesnt exist in this word, you just lost a limb :) ")
            lives -= 1
            print("\n You have ", lives, " left")
            
            #draw_hangman(lives) # if statment inside the lose_limb will determine based on lives the limb to take out
       

                        

        print( list_to_text(letters))
        print("\n \n ")
            


game()






