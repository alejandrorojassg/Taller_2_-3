def promedio(lista: list) -> float:
    """
    Calcula el promedio de una lista de números.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float: El promedio de los números en la lista.
    """
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def mediana(lista: list) -> float:
    """
    Calcula la mediana de una lista de números.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float: La mediana de los números en la lista.
    """
    lista.sort()
    n = len(lista)
    if n % 2 == 0:
        # Si la longitud es par, retorna el promedio de los dos valores centrales
        return (lista[n // 2 - 1] + lista[n // 2]) / 2
    else:
        # Si la longitud es impar, retorna el valor central
        return lista[n // 2]

def promedio_multiplicativo(lista: list) -> float:
    """
    Calcula el promedio multiplicativo de una lista de números.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float: El promedio multiplicativo de los números en la lista.
    """
    multiplicacion = 1
    for i in lista:
        multiplicacion *= i
    return multiplicacion ** (1 / len(lista))

def orden_ascendente(lista: list) -> list:
    """
    Ordena una lista de números en orden ascendente.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    list: La lista ordenada de forma ascendente.
    """
    lista.sort()
    return lista

def orden_descendente(lista: list) -> list:
    """
    Ordena una lista de números en orden descendente.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    list: La lista ordenada de forma descendente.
    """
    lista.sort(reverse=True)
    return lista

def mayor_elevado_menor(lista: list) -> float:
    """
    Calcula el valor del mayor número elevado a la potencia del menor número de la lista.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float: El mayor número elevado al menor número.
    """
    lista.sort()
    return lista[-1] ** lista[0]

def raiz_cubica_menor_numero(lista: list) -> float:
    """
    Calcula la raíz cúbica del menor número en la lista.

    Parámetros:
    lista (list): Una lista de números.

    Retorna:
    float: La raíz cúbica del menor número en la lista.
    """
    lista.sort()
    return lista[0] ** (1 / 3)

if __name__ == "__main__":
    # Solicita al usuario que ingrese números para formar una lista
    print("Ingrese los números de la lista. Para terminar, ingrese 'fin'.")
    lista = []
    while True:
        entrada = input("Ingresar número: ")
        if entrada.lower() == "fin":  # Verifica si el usuario desea finalizar la entrada
            break
        lista.append(float(entrada))  # Convierte la entrada a float y la agrega a la lista

    # Calcula y almacena los resultados de varias funciones estadísticas y de manipulación de listas
    resultado_promedio = promedio(lista)
    resultado_mediana = mediana(lista)
    resultado_promedio_multiplicativo = promedio_multiplicativo(lista)
    resultado_orden_ascendente = orden_ascendente(lista)
    resultado_orden_descendente = orden_descendente(lista)
    resultado_mayor_elevado_menor = mayor_elevado_menor(lista)
    resultado_raiz_cubica_menor_numero = raiz_cubica_menor_numero(lista)
    
    # Imprime los resultados obtenidos
    print(f"El promedio es {resultado_promedio}")
    print(f"La mediana es {resultado_mediana}")
    print(f"El promedio multiplicativo es {resultado_promedio_multiplicativo}")
    print(f"La lista ordenada de forma ascendente es {resultado_orden_ascendente}")
    print(f"La lista ordenada de forma descendente es {resultado_orden_descendente}")
    print(f"El mayor elevado al menor es {resultado_mayor_elevado_menor}")
    print(f"La raíz cúbica del menor número es {resultado_raiz_cubica_menor_numero}")
