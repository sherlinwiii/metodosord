def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[0]
        menores = [x for x in arr[1:] if x <= pivote]
        mayores = [x for x in arr[1:] if x > pivote]
        return quicksort(menores) + [pivote] + quicksort(mayores)

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
        print("\n--- Menú Quicksort ---")
        print("1. Ingresar números y ordenar")
        print("2. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numeros = pedir_numeros()
            print("Lista original:", numeros)
            ordenada = quicksort(numeros)
            print("Lista ordenada:", ordenada)
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()
