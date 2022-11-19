# ===============for Сортировка выбором - Выборка случвйнвя
from random import randint
n = 10
arr = []
for i in range (n):
    arr.append(randint(1, 99))
print (arr)
#  ============== while Сортировка выбором - Сортировка по ыозрастанию
i = 0
while i < n - 1:
    m = i
    j = i + 1
    while j < n:
        if arr[j] < arr[m]:
            m = j
        j += 1
    arr[i], arr[m] = arr[m], arr[i]
    i += 1
print(arr)

# ++++++++++++++++++ Sample

a = 15
arr1 = []
for e in range(a):
    arr1.append(randint(10, 150))
print(arr1)

e = 0
while e < a - 1:
    b = e # индекс ячейки с минимальным значением
    k = e + 1 # значение следующее за e
    while k < a:
        if arr1[k] < arr1[b]:
            b = k
        k += 1
    arr1[e], arr1[b] = arr1[b], arr1[e]
    e += 1 # проход по следующей ячейке
print(arr1)
