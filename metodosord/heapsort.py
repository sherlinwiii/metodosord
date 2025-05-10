def heapsort(arr):
    def heapify(arr, n, i):
        mayor = i
        izq = 2 * i + 1
        der = 2 * i + 2

        if izq < n and arr[izq] > arr[mayor]:
            mayor = izq
        if der < n and arr[der] > arr[mayor]:
            mayor = der
        if mayor != i:
            arr[i], arr[mayor] = arr[mayor], arr[i]
            heapify(arr, n, mayor)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)

    return arr

def pedir_numeros():
    while True:
        try:
            cantidad = int(input("¿Cuántos números vas a ingresar? "))
            if cantidad <= 0:
                print("Debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingresa un número válido.")
    
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i + 1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return numeros

def menu():
    while True:
        print("\n--- Menú Heapsort ---")
        print("1. Ingresar números y ordenar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeros = pedir_numeros()
            print("Lista original:", numeros)
            ordenada = heapsort(numeros.copy())
            print("Lista ordenada:", ordenada)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
