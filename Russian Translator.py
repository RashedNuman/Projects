"""
                    Russian Translator

                    Written in Python 3.8.1

                    requires words.txt document

"""

import io
import sys
import time
import os as system

def examples():

    print("\n \n \n")
    print('=' *25)
    print("\n")

    with open("words.txt", "r") as file:

        for line in file:

            word = line.split()[0]

            print(word + "\n")

    print('=' *25)

    return None

def translator():

    if system.path.isfile("./words.txt") == True:
        print("\n \n Dictionary file found... Continuing... \n \n")
    else:
        print("\n \n Dictionary File not found, please place words.txt in the same directory as the code then run again")
        sys.exit()

    english_phrase = str(input("Translate : "))

    english_word_list = english_phrase.split()


    russian_phrase = ''
    

    for en_word in english_word_list:

        with open("words.txt", "r") as file:

            for line in file:

                x = line.split()

                if x[0] == en_word:

                    translated = x[2]
                    russian_phrase += translated + " "
            file.close()

    print(russian_phrase)

    return None
    

print("Welcome to the russian translator \n")
print("it can only translate very few phrases / words due to the insane manual work needed \n")

while True:

  

    menu = str(input(" \n Enter 1 to continue or 2 to display translation dictionary or 0 to exit :  "))
    
    if menu == '1':

        translator()

    elif menu == '2':

        examples()

    elif menu == '0':

        sys.exit()
    
