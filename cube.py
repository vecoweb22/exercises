import random

k = 4
arr = []
total = 0
tr = 0
while k != 0:
    x = random.randint(1, 6)
    k -= 1
    tr = tr + 1
    arr.append(x)
    print('Бросок', tr, arr)
for i in arr:
    total += i
print('Сумма', total)