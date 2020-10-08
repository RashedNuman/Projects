"""
                           Ceaser Cipher Encryptor





Description: Python script that runs ceaser cipher on a txt document, encrypts
                decrypts files, can also encrypt based on date

Language: python 3.8.1

Author : Rashed Alnuman


"""

# importing libraries at the start to use

import sys
import errno
import time
from datetime import datetime



def main():

    """
    void function
    no parameters
    
    Main function, displays a interactive selection menu that prompts the user to enter a valid
    input to choose the service they wish to use, in case of invalid input loops back to prompt
    for valid input. Surrounded by try-catch block which either restarts the main function to
    handle an exception. upon user choice to exit, exits with exit code 0
    """

    try:
    
        print(" \t Hello to the Ceaser Cipher \n \n")
        choice = int(input("Enter 1 to encrypt, Enter 2 to decrypt, Enter 3 to Exit:  "))

    except EOFError:
        main()


    if choice == 1:

        while True:
        
            choice2 = int(input("Enter 1 to encrypt manually by key, Enter 2 to encrypt by date:  "))

            if choice2 == 1:

                manual_encrypt()
                break

            elif choice2 == 2:

                encrypt_date()
                break

            else:

                print("Invalid input, please pick a correct option")
                continue
                      


    elif choice == 2:

        decrypt()

    elif choice == 3:

        sys.exit(0)

    else:
        print("Invalid choice, please enter a valid choice")
        main()



def encrypt_date():

    """
    void function
    no parameters
    
    Encrypts based on the current day of the month, uses daytime and the now() method
    to extract the current date and then extract the day of the month to place it as
    the key. For the sake of simplicity theres no point in the key being greater than
    25 which loops back and causes potential errors, key value is altered to be less
    than 25 if the day of month is more than 25. callst he encrypt function to continue
    """

    try:

        current_date = str(datetime.date(datetime.now()))

        date_split = current_date.split("-")

        key = int(date_split[2])

        while key > 25:

            key = key //2 +5
 

        file = str(input("Enter file name: "))
        filename = open(file, "r+")
        string = filename.read()
        encrypt(string, key, 1)

    except IOError as ioe:
        
        if ioe.errno == errno.EACCES:
            print("Unreadable File, please enter a readable file... \n \n")
            encrypt_date()

        elif ioe.errno == errno.ENOENT:
            print("File does not exist, enter a existing file... \n \n")
            encrypt_date()

    except Exception:
        print("An error has occured \n \n")
        main()
        
  

###########
    
def manual_encrypt():

    """
    void function
    no parameters
    
    manual encryption prompts the user to manually enter an encryption key.
    The value of the key cannot be less than 1 nor greater than 25. User is
    prompted to enter a new value everytime the key is an invalid value.
    calls the encrypt function to continue the encryption process
    """
    

    try:

        key = int(input("Enter the left shift value key:  "))

        if key < 1 or key > 25:

            print("Key value cannot exceed 25 or go below 1, enter a new value")
            encrypt()


        file = str(input("Enter file name: "))
        filename = open(file, "r+")
        string = filename.read()

        
        encrypt(string, key, 0)

    except IOError as ioe:
        
        if ioe.errno == errno.EACCES:
            print("Unreadable File, please enter a readable file... \n \n")
            manual_encrypt()

        elif ioe.errno == errno.ENOENT:
            print("File does not exist, enter a existing file... \n \n")
            manual_encrypt()

    except Exception:
        print("An error has occured \n \n")
        main()


    


#######################

def encrypt(string, key, stat):

    """
    void function
    parameters: str() String, int() key, int() stat
    
    Encrypts the string provided based on the key, and removes hidden key in the file
    in case the file was automatically encrypted by date. encrypts the string by
    altering the ascii value to change it to another letter, cannot translate to non
    letters, will revolve back to the end of the alphabet if it goes out of letter range.
    Does not encrypt blank spaces or non letters.
    writes the encrypted data on a new file.
    """
    

    try:

        text = ""

        for i in string:

            for k in i:
        
                    
                if ord(k) >= 97 and ord(k) <= 122:

                    if ord(k) - key < 97:


                        letter = chr( ord(k) +26 -key)
                        text += letter
                    

                    else:
                        
                        letter = chr( ord(k) - key)

                        text += letter

                
                        
           
                elif ord(k) >= 65 and ord(k) <= 90: # if its a capital
                        

                    if ord(k) - key < 65:  

                        letter = chr( ord(i) +26 -key)
                        text += letter


                    else:

                        letter = chr( ord(k) - key)

                        text += letter


                else:
                    text += k

                    
    
        encrFile = str(input("Encrypted file name:  "))
        newfile = open(encrFile +".txt", "w+")
        
        if stat == 0:
            newfile.write(text)
        else:
            x = 'k'+str(key)
            newfile.write(text+x)
            
        newfile.close()
        print("encryption successfull")
        print("Your encrypted text has been saved as " + encrFile + ".txt")
        print("returning to main menu... \n \n")
        time.sleep(2)
        main() # Calls the main function again

    except IOError:
        print("Error occured during encryption, possibly unreadable data or corrupt file, return to menu... \n \n")
        main()

    except Exception:
        print("An unknown error has occured, returning to menu... \n \n")
        main()
        
        


def decrypt():

    """
    void function
    no parameters
    
    reverses the algorithm of the encrypt function. in case file was
    automatically encyrpted by date, extracts the key from the file
    decrypts it automatically also.
    writes the decrypted data on a new file
    """


    try:

        try:
        
            file = input("Enter the txt file you wish to decrypt:  ")
            myfile = open(file, "r+")
            file_text = myfile.read()
                

            method = int(input("Enter 1 to decrypt manually or 2 for auto detection decryption:  "))

            if method == 1:
            
                key = int(input("Enter the key:  "))
                file_text2 = file_text
              
                
            elif method == 2:
                

                # Extracts the key from the file
                file_key = ""
                
                for i in range(len(file_text) -1, 0, -1):

                    x = file_text[i]
                    if x == "k":
                        file_key += x
                        break

                    file_key += x

                    old = file_key.replace('k',"")
                    key = int(old[::-1])
                    
                    
                    remove =  'k'+str(key)
                    file_text2 = file_text.replace(remove,"")


        except EOFError:
            print("Stop messing with the space bar  please, \n \n")
            decrypt()

        except ValueError:
            print("Invalid input type, enter the apporpiate data type in inputs... \n \n")
            decrypt()

        
        text = ""

        for i in file_text2:

            for k in i:


                if ord(k) >= 97 and ord(k) <= 122:

                
                    if ord(k) + key > 122:


                        letter = chr( ord(k) - 26 + key)
                        text += letter

                
                    else:

                        letter = chr(ord(k) + key)
                        text += letter
                    

                        

        
                elif ord(k) >= 65 and ord(k) <= 90:


                    if ord(k) + key > 90:

                        letter = chr( ord(k) -26 +key)
                        text += letter

                
                    else:

                        letter = chr(ord(k) + key)
                        text += letter


                else:

                    text += k

        print(text)
        print("decryption successfull")

        name = str(input("Decryption file name:  "))
        
        newfile = open(name+".txt", "w+")
        newfile.write(text)
        newfile.close()
        time.sleep(2)   
        main()

    except IOError as ioe:
        
        if ioe.errno == errno.EACCES:
            print("Unreadable File, please enter a readable file... \n \n")
            decrypt()

        elif ioe.errno == errno.ENOENT:
            print("File does not exist, enter a existing file... \n \n")
            decrypt()

    except IndexError:
        print("Could not process key in the data file, may be altered or corrupt... \n \n")
        decrypt()

    except ValueError:
        print("Could not identify file key in the data file, enter the key manually... \n \n")
        decrypt()

    except Exception:
        print("Unknown problem has occured, Either UTF error or something else, returning to menu... \n \n")
        main()

#---------------------------------------------------------------------------------------------------#   

main() # calling the main function to start the code
