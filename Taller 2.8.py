def elementos_ausentes(lista1: list, lista2: list) -> list:
    """
    Encuentra y retorna los elementos que están en la primera lista pero no en la segunda.

    Parámetros:
    lista1 (list): La primera lista de elementos.
    lista2 (list): La segunda lista de elementos.

    Retorna:
    list: Una lista con los elementos que están en lista1 pero no en lista2.
    """
    lista_resultante = []  # Lista para almacenar los elementos ausentes en lista2

    # Itera sobre cada elemento en lista1
    for i in lista1:
        # Verifica si el elemento no está en lista2
        if i not in lista2:
            # Si el elemento no está en lista2, se agrega a lista_resultante
            lista_resultante.append(i)
    
    return lista_resultante  # Retorna la lista de elementos ausentes

if __name__ == "__main__":
    # Inicializa listas vacías para almacenar los elementos ingresados por el usuario
    lista1 = []
    lista2 = []

    # Bucle para ingresar elementos en la primera lista
    while True:
        entrada = input("Ingresar elemento (escriba 'fin' para terminar): ")
        if entrada.lower() == "fin":  # Verifica si el usuario desea finalizar la entrada
            break
        lista1.append(entrada)  # Agrega el elemento a la primera lista
    
    # Bucle para ingresar elementos en la segunda lista
    while True:
        entrada2 = input("Ingresar elemento (escriba 'fin' para terminar): ")
        if entrada2.lower() == "fin":  # Verifica si el usuario desea finalizar la entrada
            break
        lista2.append(entrada2)  # Agrega el elemento a la segunda lista

    # Llama a la función para encontrar elementos ausentes y almacena el resultado
    lista_resultante = elementos_ausentes(lista1, lista2)
    
    # Imprime los elementos que están en lista1 pero no en lista2
    print(f"Los elementos que tiene la primera lista que no tiene la segunda son: {lista_resultante}")
