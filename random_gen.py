
import random
x = random.randint(0, 100)
print(f'Моё число: {x} - {type(x)}')

arr = [1, 2, 3, 4, 5, 6, 12, 34, 56, 76, 87, 99, 'a', 's', 'd', 'f']
k = 3
arr2 = []
while k != 0:
    k -= 1
    num = random.choice(arr)
    print('Моё число/строка', num)
    arr2.append(num)
print(arr2)

y = random.random()
print(f'Случайное число от 0.0 до 1.0 - {y} {type(y)}')

z = random.uniform(0.2, 7.5)
print(f'Случайное число от 0.2 до 7.5 - {z} {type(z)}')
