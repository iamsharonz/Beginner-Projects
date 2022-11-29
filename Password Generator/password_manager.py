from cryptography
master_pass = input('What is your master password? ')



def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split(':')
            print('User:', user, '| Password:', passw)


def add():
    name = input('Please enter the account name: ')
    pwd = input('Enter the password: ')

    with open('passwords.txt', 'a') as file:
        file.write(name + ':' + pwd + '\n')



while True:
    mode = input('Would you like to enter a new password or to view an existing password (view/add) or q to quit: ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()