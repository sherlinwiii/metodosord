def dividir_en_secuencias(arr):
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

def mezclar_sec(a, b):
    resultado = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            resultado.append(a[i])
            i += 1
        else:
            resultado.append(b[j])
            j += 1
    resultado.extend(a[i:])
    resultado.extend(b[j:])
    return resultado

def mezcla_equilibrada(arr):
    while True:
        secuencias = dividir_en_secuencias(arr)
        if len(secuencias) <= 1:
            return arr

    
        F1, F2 = [], []
        for i, sec in enumerate(secuencias):
            if i % 2 == 0:
                F1.append(sec)
            else:
                F2.append(sec)

        arr = []
        for i in range(max(len(F1), len(F2))):
            s1 = F1[i] if i < len(F1) else []
            s2 = F2[i] if i < len(F2) else []
            mezclado = mezclar_sec(s1, s2)
            arr.extend(mezclado)


if __name__ == "__main__":
    entrada = input("Ingresa los números a ordenar (mezcla equilibrada), separados por espacios: ")
    lista = list(map(int, entrada.strip().split()))
    ordenada = mezcla_equilibrada(lista)
    print("Lista ordenada:", ordenada)

