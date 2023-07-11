from cryptography.fernet import Fernet

import base64
import sys


def generate_key(mstr_pwd):
    key_fernet = Fernet.generate_key()
    key = key_fernet + mstr_pwd.encode()
    key = base64.b64encode(key)
    # Return the key and the generated Fernet part only
    return key, key_fernet


def write_key(key):
    with open("key.key", "wb") as kf:
        kf.write(key)


def load_key():
    f = open("key.key", "rb")
    key = f.read()
    f.close()
    return key


def view_passwords(fernet):
    try:
        with open("./passwords.txt", 'r') as f:
            for line in f.readlines():
                text = line.rstrip()
                user, passw = text.split('|')
                print("User/context:", user)
                print("Password:", fernet.decrypt(passw.encode()).decode() + '\n')
    except:
        print("\nThe file does not exist yet!")
        print("Add a new password.\n")


def add_password(fernet):
    user = input("Username/context: ")
    pwd = input("Password: ")
    print("add pwd", fernet)
    # Will automatically close the file 
    # without having to user open() and close()
    with open("./passwords.txt", 'a') as f:
        f.write(user + '|' + fernet.encrypt(pwd.encode()).decode() + '\n')


if __name__ == "__main__":
    mstr_pwd = input("Enter your master password for encrypting/decrypting: ")
    key = ""

    try:
        # Try to open and load the key.key file if it exists.
        key = load_key()
        #print("hello", base64.b64decode(fernet.decode()))
    except:
        pass
        
    if key != "":
        # Now, check if the mstr_pwd inserted is the same as the key in the file
        mstr_key = base64.b64decode(key.decode())
        mstr_key = mstr_key.decode()

        #print("try key:", try_key)
        #print("try key:", try_key[44:])

        if mstr_key[44:] != mstr_pwd:
            print("\nInvalid master password. Exiting...")
            exit(1)
        else:
            print("\nMaster password accepted!")
            # Get the 32 url-safe part from the key,
            # that can be used by the Fernet import
            fernet = Fernet(mstr_key[:44])
    else:
        # If the key.key file doesn't exist, generate a new key a create + write to file.
        # Get the whole key and just the Fernet generated key
        key, key_fernet = generate_key(mstr_pwd)

        #print("key:", key, "| fernet_key:", key_fernet)

        # Write the key to the file, and use the Fernet generated key
        # to create the Fernet object to use later
        write_key(key)
        fernet = Fernet(key_fernet)

    while 1:
        print("\nChoose one of the following options:")
        print("\t1 - View existing passwords")
        print("\t2 - Add a new password")
        print("\tQ - Exit")
        menu = input("> ")
        if menu not in ['1', '2', 'Q', 'q']:
            print("\nPlease choose a valid option.")
            continue
        if menu in ['Q', 'q']: break

        print("")
        if menu == '1': view_passwords(fernet)
        if menu == '2': add_password(fernet)
