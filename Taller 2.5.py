def mcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo (MCM) de dos números enteros.

    Parámetros:
    a (int): El primer número entero.
    b (int): El segundo número entero.

    Retorna:
    int: El mínimo común múltiplo de a y b.
    """
    multiplo = a  # Inicializa el múltiplo en el valor de 'a'
    
    while True:
        # Verifica si el múltiplo actual es divisible por 'b'
        if multiplo % b == 0:
            return multiplo  # Si lo es, este es el MCM y se retorna
        multiplo += a  # Si no, incrementa el múltiplo en 'a' y repite el proceso

if __name__ == "__main__":
    # Solicita al usuario que ingrese dos números enteros
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    
    # Calcula el MCM de los dos números ingresados
    minimo_comun_multiplo = mcm(a, b)
    
    # Imprime el resultado
    print(f"El MCM de {a} y {b} es: {minimo_comun_multiplo}")