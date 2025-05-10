def intercalar_varias_listas(listas):
    indices = [0] * len(listas)
    resultado = []

    while True:
        candidatos = []
        for idx, lista in enumerate(listas):
            if indices[idx] < len(lista):
                candidatos.append((lista[indices[idx]], idx))

        if not candidatos:
            break

        menor_valor, origen = min(candidatos)
        resultado.append(menor_valor)
        indices[origen] += 1

    return resultado


if __name__ == "__main__":
    num_listas = int(input("¿Cuántas listas ordenadas quieres intercalar? "))
    listas = []

    for i in range(num_listas):
        entrada = input(f"Ingrese los elementos de la lista #{i+1} separados por espacios (ya ordenados): ")
        lista = list(map(int, entrada.strip().split()))
        listas.append(lista)

    resultado = intercalar_varias_listas(listas)
    print("\nResultado de la intercalación:", resultado)


