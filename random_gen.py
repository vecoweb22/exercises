
import random
x = random.randint(0, 100)
print(f'Моё число: {x} - {type(x)}')

arr = [1, 2, 3, 4, 5, 6, 12, 34, 56, 76, 87, 99, 'a', 's', 'd', 'f']
k = 3
arr2 = []
while k != 0:
    k -= 1
    print('Моё число/строка', random.choice(arr))
    arr2.append(random.choice(arr))
print(arr2)

