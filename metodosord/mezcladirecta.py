
def mezcla_directa(arr):
    def dividir_secuencias(arr):
        secuencias = []
        i = 0
        while i < len(arr):
            sec = [arr[i]]
            i += 1
            while i < len(arr) and arr[i] >= arr[i - 1]:
                sec.append(arr[i])
                i += 1
            secuencias.append(sec)
        return secuencias

    def mezclar(secuencias):
        resultado = []
        while len(secuencias) > 1:
            nueva_sec = []
            for i in range(0, len(secuencias), 2):
                if i + 1 < len(secuencias):
                    nueva_sec.append(fusionar(secuencias[i], secuencias[i + 1]))
                else:
                    nueva_sec.append(secuencias[i])
            secuencias = nueva_sec
        return secuencias[0] if secuencias else []

    def fusionar(a, b):
        resultado = []
        i = j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                resultado.append(a[i])
                i += 1
            else:
                resultado.append(b[j])
                j += 1
        resultado.extend(a[i:])
        resultado.extend(b[j:])
        return resultado

    while True:
        secuencias = dividir_secuencias(arr)
        if len(secuencias) <= 1:
            break
        arr = mezclar(secuencias)
    return arr

if __name__ == "__main__":
    entrada = input("Ingresa los números a ordenar separados por espacios: ")
    lista = list(map(int, entrada.strip().split()))
    ordenada = mezcla_directa(lista)
    print("Lista ordenada:", ordenada)
