def mcd(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números enteros utilizando el algoritmo de Euclides.

    Parámetros:
    a (int): Primer número entero.
    b (int): Segundo número entero.

    Retorna:
    int: El máximo común divisor de a y b.
    """
    while b != 0:  # Mientras b no sea 0
        a, b = b, a % b  # Actualiza a con b y b con el residuo de a dividido por b
    return abs(a)  # Retorna el valor absoluto de a (el MCD siempre es positivo)

def mcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo (MCM) de dos números enteros utilizando el MCD.

    Parámetros:
    a (int): Primer número entero.
    b (int): Segundo número entero.

    Retorna:
    int: El mínimo común múltiplo de a y b.
    """
    return abs(a * b) // mcd(a, b)  # Usa la relación MCM(a, b) = abs(a * b) // MCD(a, b)

if __name__ == "__main__":
    # Solicita al usuario que ingrese dos números enteros
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    # Calcula el MCD y MCM de los dos números ingresados
    maximo_comun_divisor_resultado = mcd(num1, num2)
    minimo_comun_multiplo_resultado = mcm(num1, num2)

    # Imprime los resultados
    print(f"El MCM de {num1} y {num2} es: {minimo_comun_multiplo_resultado}")
