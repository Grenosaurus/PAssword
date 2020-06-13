"""
 Program has two different options: 
  Option 1. Generates new password and stores it in a text file as binary with the account name.  
  Option 2. Copies existing password for use
 For accessing both option user must give a master password of their own choise (Made: Jauaries Loyala -- 
 12.06.2020).
"""


# Python packets
import time

from pyperclip import copy
from pickle import dump, load, HIGHEST_PROTOCOL
from random import sample
from cryptography.fernet import Fernet


"""
 When program is operated the first time close lines 33-35, because the file must consists binary input for 
 this section of the program tp work.
"""


# Reads the encryption key from another file
def encryptionKey(filename):

    # Opens the file and reads the key
    file = open(filename, 'rb')
    key = file.read()
    file.close()

    f = Fernet(key)    

    return f


# Generates a new password and stores it in file
def generatePassword(filename, f):

    # Creating a storage distionary for accounts and passwords
    storage = {}

    # Reads the binary file and used for appending the next set of passwords | Read file must exist and have binary inputs in it
    with open(filename, 'rb') as fileread:
        storage = load(fileread)
    
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#%&/()=?' # List of letters

    input_number = input('Number of letter in password: ') # Letter number
    len_password = int(input_number) # Length of the letter number

    list_char = sample(characters, len_password) # Generates randomly a password from the list of letters

    password = ''.join(list_char) # Joins the characters together
    encrypted_password = password.encode() # Encrypting the password
    print(encrypted_password)

    pw = f.encrypt(encrypted_password) # Encypts encoded password

    keep_password = input('Keep pasword (yes or no): ')

    # Keeping the password or not
    if('yes' in keep_password):
        site_name = input('Enter site name: ') # Account name

        storage[site_name] = pw # Storing the password with the object into the distionary
        
        # Creates a text file as a binary file
        with open(filename, 'wb') as filewrite:
            dump(storage, filewrite, protocol = HIGHEST_PROTOCOL)
        
    else:
        print('OK!')



# Reads the existing file and copies the password
def readPassword(filename, f):

    site_name = input('Enter site name: ')

    with open(filename, 'br') as readfile:
        storage = load(readfile)

    if(site_name in storage):
        decryted_password = f.decrypt(storage[site_name]).decode() # Decodes encoded password
        copy(decryted_password)
        print('Password copied!')

    else:
        print('Account not found!')




def main():

    password_file = 'textfile/test.txt' # File where the passwords and account site name will be stored | Change the name and format
    encryption_file = 'textfile/key.key' # File which consists encryption key

    master_password = input('Master password: ') # Master password for accesing the passwords

    f = encryptionKey(encryption_file) # Encryption key

    # Evaluates the Master password | Change the master password
    if(master_password == 'GRENO'):
        input_password = str(input('New password (new) or Copy Password (copy): ')) # Wanted option

        if('new' in input_password):
            generatePassword(password_file, f) # Generates a new password for wanted account

        elif('copy' in input_password):
            readPassword(password_file, f) # Copies password for wanted account (if the account is found from the read file)

        else:
            print('Option not found!')

    else:
        print('Master password INCORRECT!')


# Calculates the how much the program took to finnish
if __name__ == "__main__":

    # Time of main function
    start_time = time.time() # Start time of the main function
    main()
    end_time = time.time() # End time of the main function

    # Delta time
    Delta_time_seconds = end_time - start_time # Difference between start and end time (defined in seconds)
    Delta_time_minutes = Delta_time_seconds/60 # Difference between start and end time (defined in minutes) | 1 min = 60 s

    # Round value of delta time
    Delta_time_seconds_round = round(Delta_time_seconds, 2)
    Delta_time_minutes_round = round(Delta_time_minutes, 2)

    # Prints the time took for the program to run
    print("\nProgram took %s seconds (~ %s minutes)." % (Delta_time_seconds_round, Delta_time_minutes_round))


