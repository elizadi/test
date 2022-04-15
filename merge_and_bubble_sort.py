# two types of sorting algorithms: Merge sort and bubble sort

def merge_sort(arr):
    if len(arr) > 1:
        middle = len(arr) // 2
        left = arr[:middle]
        right = arr[middle:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
    
        if swapped == False:
            break

    return arr
    

def string_to_list(arr):
    arr = arr.split(' ')
    i = 0
    a = []
    while i < len(arr):
        a.append(int(arr[i]))
        i += 1
    arr = a 
    return arr


array = input('Print array. Use space to separate elements: ')
array = string_to_list(array)
# print(array)
print('Merge sorted array: ', merge_sort(array))
print('Bubble sorted array: ', bubble_sort(array))