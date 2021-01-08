from menu import menu, create, find, find_accounts, display_all, change, delete
from encryption import master_key
from getpass import getpass


def access():
    print('')
    print('Enter the master key to start: ')
    print('')
    master = getpass('> ').encode('utf-8')
    print('')
    if master_key(master):
        print("You're in!")
    else:
        print('No luck')
        exit()


def start():
    choice = menu()
    while choice != 'Q':
        if choice == '1':
            create()
        if choice == '2':
            find()
        if choice == '3':
            find_accounts()
        if choice == '4':
            display_all()
        if choice == '5':
            change()
        if choice == '6':
            delete()
        choice = menu()
    exit()


if __name__ == '__main__':
    access()
    start()
