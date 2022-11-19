def binary_search(arr, low, high, x):
    # Проыерка середины
    if high >= low:
        mid = (high + low) // 2
        #  Если элемент находится в середине
        if arr[mid] == x:
            return mid
        # Если элемент находится с левой стороны
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        # Если элемент находится с правой стороны
        else:
            return binary_search(arr, mid + 1, high, x)
    # Если элемент не в массиве
    else:
        return -1

# Объявление массива
arr = [3, 5, 7, 10, 15, 17]
x = int(input('Введите число '))

# Вызов функции
result = binary_search(arr, 0, len(arr) - 1, x)

if result != -1:
	print('Элемент присутствует в массиве ')
else:
	print('Элемент не присутствует в массиве ')
