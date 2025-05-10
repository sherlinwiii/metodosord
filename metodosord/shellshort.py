from tkinter import Menu
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
if __name__ == "__main__":  
    Menu()

    numeros = []
    while True:
        print("\n--- MENÚ SHELL SORT ---")
        print("1. Ingresar números")
        print("2. Ordenar con Shell Sort")
        print("3. Mostrar lista actual")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            try:
                cantidad = int(input("¿Cuántos números desea ingresar? "))
                numeros = []
                for i in range(cantidad):
                    num = float(input(f"Ingrese el número #{i + 1}: "))
                    numeros.append(num)
            except ValueError:
                print("Entrada inválida. Intente de nuevo.")
        elif opcion == '2':
            if numeros:
                print("Lista original:", numeros)
                shell_sort(numeros)
                print("Lista ordenada:", numeros)
            else:
                print("Primero debe ingresar números.")
        elif opcion == '3':
            print("Lista actual:", numeros if numeros else "vacía")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

Menu()
