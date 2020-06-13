"""
 Generates encryption key and stores it in a file. ileformat can be changed to own version (Made: Jauaries).
"""

# Python Packets
from cryptography.fernet import Fernet


def encryptionKey():
    

    key = Fernet.generate_key()
    f = Fernet(key)
    print(f)

    filename = 'key.key' # Change the filename and format for own specific

    file = open(filename, 'wb')
    file.write(key)
    file.close()

encryptionKey()
