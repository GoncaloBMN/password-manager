
def view_passwords():
    pass


def add_password():
    pass


if __name__ == "__main__":
    pwd = input("Enter your master password for encrypting/decrypting: ")
    while 1:
        print("\nChoose one of the following options:")
        print("\t1 - View existing passwords")
        print("\t2 - Add a new password")
        print("\tQ - Exit")
        menu = input("> ")
        if menu not in ["1", "2", "Q"]:
            print("\nPlease choose a valid option.")
            continue
        if menu == 'Q': break

