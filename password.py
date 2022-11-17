import random
chars = '+-/*!&$#?=@<>abcdefghklmnopqrstuvwxyzABCDEFGHKLMNOPQRDTUVWXYZ1234567890'
length = input('Длина пароля' + '\n')
password = ''
try:
    length = int(length)
    for n in range(length):
        password += random.choice(chars)
    print(password)
except ValueError:
    print('Вы ввели буквы, введите цифры')
