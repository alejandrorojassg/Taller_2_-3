def matriz_magica(matriz: list) -> bool:
    """
    Verifica si una matriz cuadrada es mágica. Una matriz es mágica si la suma de los números
    en cada fila, cada columna y ambas diagonales principales es la misma.

    Parámetros:
    matriz (list): Una lista de listas que representa una matriz cuadrada.

    Retorna:
    bool: True si la matriz es mágica, False en caso contrario.
    """
    dimensiones = len(matriz)  # Obtiene el tamaño de la matriz
    suma_diagonal_principal = 0  # Inicializa la suma de la diagonal principal
    suma_diagonal_secundaria = 0  # Inicializa la suma de la diagonal secundaria

    # Itera sobre cada fila
    for i in range(dimensiones):
        suma_filas = 0  # Inicializa la suma de la fila actual
        suma_columnas = 0  # Inicializa la suma de la columna actual

        # Itera sobre cada columna
        for j in range(dimensiones):
            suma_filas += matriz[i][j]  # Suma el valor de la fila actual
            suma_columnas += matriz[j][i]  # Suma el valor de la columna actual

            # Verifica si el elemento está en la diagonal principal
            if i == j:
                suma_diagonal_principal += matriz[i][j]
            # Verifica si el elemento está en la diagonal secundaria
            if i + j == dimensiones - 1:
                suma_diagonal_secundaria += matriz[i][j]

    # Tomamos la suma de la primera fila como referencia
    suma_esperada = suma_filas  

    # Verifica si todas las sumas son iguales
    if (suma_filas != suma_columnas or
        suma_filas != suma_diagonal_principal or
        suma_filas != suma_diagonal_secundaria or
        suma_columnas != suma_diagonal_principal or
        suma_columnas != suma_diagonal_secundaria or
        suma_diagonal_principal != suma_diagonal_secundaria):
        return False

    return True

if __name__ == "__main__":
    print("¿Su matriz es mágica?")
    dimensiones = int(input("Ingrese el número de filas y columnas de la matriz: "))
    matriz = []

    # Lee la matriz del usuario
    for j in range(dimensiones):
        fila = []
        for k in range(dimensiones):
            valor = int(input(f"Ingrese el valor para [{j+1}], [{k+1}] de la matriz: "))
            fila.append(valor)
        matriz.append(fila)

    # Verifica si la matriz es mágica
    resultado_matriz_magica = matriz_magica(matriz)

    if resultado_matriz_magica:
        # Calcula la suma esperada basada en la primera fila
        print(f"La matriz es mágica pues la suma de todas sus filas, columnas y diagonales es {sum(matriz[0])}")
    else:
        print("La matriz no es mágica")
