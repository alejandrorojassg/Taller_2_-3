def mcd(a: int, b: int) -> int:
    """
    Calcula el máximo común divisor (MCD) de dos números enteros usando recursión y el algoritmo de Euclides.

    Parámetros:
    a (int): El primer número entero.
    b (int): El segundo número entero.

    Retorna:
    int: El máximo común divisor de a y b.
    """
    if b == 0:
        return a  # Caso base: si b es 0, el MCD es a
    else:
        # Llamada recursiva intercambiando los parámetros
        return mcd(b, a % b)

def mcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo (MCM) de dos números enteros.

    Parámetros:
    a (int): El primer número entero.
    b (int): El segundo número entero.

    Retorna:
    int: El mínimo común múltiplo de a y b.
    """
    return (a * b) // mcd(a, b)  # Usa la fórmula MCM(a, b) = (a * b) / MCD(a, b)

if __name__ == "__main__":
    # Solicita al usuario que ingrese dos números enteros
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    
    # Calcula el MCD y el MCM de los dos números ingresados
    maximo_comun_divisor_resultado = mcd(a, b)
    minimo_comun_multiplo_resultado = mcm(a, b)
    
    # Imprime el resultado del MCM
    print(f"El MCM de {a} y {b} es: {minimo_comun_multiplo_resultado}")