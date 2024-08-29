# Бінарний пошук

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
result = binary_search(arr, target)

if result != -1:
    print(f"Шуканий елемент: {target} \n"
          f"Елемент знайдено на індексі: {result}")
else:
    print("Елемент не знайденo")


# Сортування вставкою

def insertion_sort(array):
    # Пройтись по всіх ел масиву починаючи з другого
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        # Перемістити елементи масиву, які більші ключа, на одну позицію вперед
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        # Вставити ключ на правильне місце
        array[j + 1] = key

    return array


array = [5, 2, 9, 1, 13, 10, 6]
sorted_array = insertion_sort(array)
print(sorted_array)


# Сортування вибором — Selection sort —
# пошук найменшого або найбільшого елемента
# і переміщення його в початок або кінець впорядкованого списку.

def selection_sort(array):
    n = len(array)

    for i in range(n):
        min_idx = i

        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array


array = [64, 25, 12, 22, 11]
sorted_array = selection_sort(array)
print(sorted_array)


# Швидке сортування

def quicksort(array):
    # Масив з 1 або 0 елементів уже відсортований
    if len(array) <= 1:
        return array

    # Вибрати опорний елемент (pivot)
    pivot = array[len(array) // 2]

    # Розділити масив на три частини: менше, рівно і більше опорного елемента
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # Рекурсивно застосувати quicksort до лівого і правого підмасивів і об'єднати результат
    return quicksort(left) + middle + quicksort(right)


array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = quicksort(array)
print(sorted_array)
