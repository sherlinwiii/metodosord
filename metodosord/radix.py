def counting_sort(arr, exp):
    n = len(arr)
    salida = [0] * n
    cuenta = [0] * 10

    for i in range(n):
        index = int(arr[i] // exp) % 10
        cuenta[index] += 1

    for i in range(1, 10):
        cuenta[i] += cuenta[i - 1]

    i = n - 1
    while i >= 0:
        index = int(arr[i] // exp) % 10
        salida[cuenta[index] - 1] = arr[i]
        cuenta[index] -= 1
        i -= 1
    for i in range(n):
        arr[i] = salida[i]

def radix_sort(arr):
    if not arr:
        return arr

    if any(n < 0 or int(n) != n for n in arr):
        raise ValueError("Radix Sort solo funciona con números enteros no negativos.")

    max_num = int(max(arr))
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10
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
                num = float(input(f"Ingrese el número {i + 1} (entero no negativo): "))
                if num < 0 or int(num) != num:
                    print("Radix Sort solo permite números enteros no negativos.")
                    continue
                numeros.append(int(num))
                break
            except ValueError:
                print("Por favor, ingrese un número válido.")
    return numeros

def menu():
    while True:
        print("\n--- Menú Radix Sort ---")
        print("1. Ingresar números y ordenar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeros = pedir_numeros()
            print("Lista original:", numeros)
            try:
                ordenada = radix_sort(numeros.copy())
                print("Lista ordenada:", ordenada)
            except ValueError as e:
                print("Error:", e)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
