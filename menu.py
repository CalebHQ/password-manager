from encryption import encrypt, master_pin, decrypt
from database_manager import store_password, find_app, find_users, display_all_data, change_info, delete_data
from texttable import Texttable
from getpass import getpass


def menu():
    print('')
    print('='*23 + 'MENU' + '='*23)
    print('')
    print('1. Create new password')
    print('2. Find all accounts connected to an app name')
    print('3. Find all sites and apps connected to an email')
    print('4. Display all accounts')
    print('5. Change details')
    print('6. Delete account')
    print('Q. Exit')
    print('')
    print('='*50)
    print('')
    return input('> ')


def enter_pin():
    pin = getpass('Enter pin: ').encode('utf-8')
    if not master_pin(pin):
        print('Wrong')
        exit()
    print('Successful')


def create():
    enter_pin()
    print('')
    print('Enter name of the website or app: ')
    app_name = input('> ')
    print('Enter password: ')
    plain_text_password = input('> ')
    password = encrypt(plain_text_password)
    print('Enter your user email for this app or site: ')
    email = input('> ')
    print('Enter your username for this app or site (if applicable): ')
    username = input('> ')
    if username == None:
        username = ''
    print('Enter the url to the site that you are creating the password for: ')
    url = input('> ')
    try:
        store_password(username, email, password, url, app_name)
        print('Successfully Created')
    except:
        print('Error')


def find():
    enter_pin()
    print('Enter the name of the site or app that you want to find accounts for')
    app_name = input('> ')

    t = Texttable()
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    t.set_cols_width([2, 15, 30, 15, 30, 15])
    data = find_app(app_name)
    for i in range(len(data)):
        username, email, password, url, app_name, id = data[i]
        if username == '':
            username = 'Null'
        t.add_rows([['ID', 'Username', 'Email', 'Password', 'URL', 'App Name'], [
                   id, username, email, decrypt(password), url, app_name]])
    print(t.draw())


def find_accounts():
    enter_pin()
    print('Enter the email that you want to find accounts for')
    email = input('> ')

    t = Texttable()
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    t.set_cols_width([2, 15, 30, 15, 30, 15])
    data = find_users(email)
    for i in range(len(data)):
        username, email, password, url, app_name, id = data[i]
        if username == '':
            username = 'Null'
        t.add_rows([['ID', 'Username', 'Email', 'Password', 'URL', 'App Name'], [
                   id, username, email, decrypt(password), url, app_name]])
    print(t.draw())


def display_all():
    enter_pin()
    t = Texttable()
    t.set_cols_align(["c", "c", "c", "c", "c", "c"])
    t.set_cols_width([2, 15, 30, 15, 30, 15])
    data = display_all_data()
    for i in range(len(data)):
        username, email, password, url, app_name, id = data[i]
        if username == '':
            username = 'Null'
        t.add_rows([['ID', 'Username', 'Email', 'Password', 'URL', 'App Name'], [
                   id, username, email, password, url, app_name]])
    print(t.draw())


def change():
    enter_pin()
    print('Which account id do you want to change?: ')
    id = input('> ')
    print('Which attribute do you want to change?: ')
    attribute = input('> ')
    print('Replace with: ')
    value = input('> ')
    if attribute == 'password':
        value = encrypt(value)
    change_info(id, attribute, value)


def delete():
    enter_pin()
    print('Enter the attribute which you want to remove fields by: ')
    attribute = input('> ')
    print('Remove fields with which value?: ')
    value = input('> ')
    delete_data(attribute, value)
