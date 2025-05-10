def selection_sort_numbers(arr):
    num_intercambios = 0  
    
    for i in range(len(arr)):

        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
    
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            num_intercambios += 1

    return num_intercambios

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Lista original:", numbers)
intercambios = selection_sort_numbers(numbers)

print("Lista ordenada:", numbers)
print(f"Número de intercambios realizados: {intercambios}")
