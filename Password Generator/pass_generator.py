# python password generator

import random

password_no = int(input('Enter the no of passwords: '))
password_len = int(input('Enter the length of the password: '))

char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!@#$%^&*(),_'
for i in range(password_no):
    password = ''
    for j in range(password_len):
        password += random.choice(char)
    print(password)