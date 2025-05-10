
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        menores = [x for x in arr[1:] if x <= pivot]
        mayores = [x for x in arr[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(mayores)

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1 
    r = 2 * i + 2 
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
    return arr

def main():
    while True:
        print("\n--- Menú de Ordenamiento ---")
        print("1. Shell Sort")
        print("2. Quicksort")
        print("3. Heapsort")
        print("4. Radix Sort")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '5':
            print("Saliendo del programa.")
            break

        try:
            cantidad = int(input("¿Cuántos números vas a ingresar? "))
            numeros = []
            for i in range(cantidad):
                num = int(input(f"Ingresa el número {i+1}: "))
                numeros.append(num)
        except ValueError:
            print("Entrada inválida. Intenta de nuevo.")
            continue

        if opcion == '1':
            resultado = shell_sort(numeros.copy())
        elif opcion == '2':
            resultado = quicksort(numeros.copy())
        elif opcion == '3':
            resultado = heapsort(numeros.copy())
        elif opcion == '4':
            resultado = radix_sort(numeros.copy())
        else:
            print("Opción no válida.")
            continue

        print("Lista ordenada:", resultado)

if __name__ == "__main__":
    main()
