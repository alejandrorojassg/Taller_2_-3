def valores_repetidos(numeros: list) -> list:
    """
    Encuentra y retorna los valores que se repiten en una lista.

    Parámetros:
    numeros (list): Una lista de números.

    Retorna:
    list: Una lista de números que se repiten en la lista original.
    """
    repetidos = []  # Lista para almacenar los números repetidos

    # Itera sobre cada número en la lista original
    for i in numeros:
        # Verifica si el número aparece más de una vez en la lista
        if numeros.count(i) > 1:
            # Si el número no está ya en la lista de repetidos, lo agrega
            if i not in repetidos:
                repetidos.append(i)
                
    return repetidos  # Retorna la lista de números repetidos

if __name__ == "__main__":
    numeros = []  # Inicializa una lista vacía para almacenar los números ingresados por el usuario
    
    # Bucle infinito para ingresar números en la lista
    while True:
        entrada = input("Digite el número que quiere ingresar a la lista, para terminar, ingrese 'fin': ")
        if entrada.lower() == "fin":  # Verifica si el usuario desea finalizar la entrada de números
            break
        numeros.append(float(entrada))  # Convierte la entrada a float y la agrega a la lista
    
    # Llama a la función para obtener los números repetidos en la lista
    repetidos = valores_repetidos(numeros)

    # Itera sobre la lista de números repetidos e imprime cuántas veces se repite cada número
    for i in repetidos:
        print(f"El número {i} se repite {numeros.count(i)} veces.")
