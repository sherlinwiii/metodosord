def insertion_sort_numbers(arr):
    num_comparaciones = 0 
    
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
    
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            num_comparaciones += 1
        
        arr[j + 1] = key


        if j >= 0:
            num_comparaciones += 1

    return num_comparaciones

numbers = [64, 34, 25, 12, 22, 11, 90]


print("Lista original:", numbers)
comparaciones = insertion_sort_numbers(numbers)
print("Lista ordenada:", numbers)
print(f"Número de comparaciones realizadas: {comparaciones}")
