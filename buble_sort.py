from random import randint

a = [7, 13, 5, 3, 9]
n = len(a)
print(a)
for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print(a)

# ====================== Сортировка пузырьком for

m = 15
arr = []
for i in range(m):
    arr.append(randint(10, 150))
print(arr)

for k in range(n - 1):
    for j in range(n - k - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
print(arr)

# ====================== Сортировка пузырьком while

n1 = 15
arr1 = []
for i in range(n1):
    arr1.append(randint(10, 150))
print(arr1)

k1 = 0
while k1 < n1 - 1:
    j1 = 0
    while j1 < n1 - 1 - k1:
        if arr1[j1] > arr1[j1 + 1]:
            arr1[j1], arr1[j1 + 1] = arr1[j1 + 1], arr1[j1]
        j1 += 1
    k1 += 1
print(arr1)
