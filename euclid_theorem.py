a = int(input('Введите число A больше 0:'))
b = int(input('Введите число B больше 0:'))


def calc_hcf(x, y):
    while x != 0 and y != 0:
        if x > y:
            x = x % y
        else:
            y = y % x
    return x + y


hcf = calc_hcf(a, b)
lcm = a * b / hcf
print(f'Наибольший общий делитель (НОД) = {hcf}')
print(f'Наименьшее общее кратное (НОК) = {lcm}')
