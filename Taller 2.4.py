import math  # Importamos la librería math para usar la función coseno y otras utilidades matemáticas

def aproximar_coseno(x, n):
    """
    Calcula la aproximación del coseno de x usando la serie de Taylor.
    
    Parámetros:
    x (float): El ángulo en radianes para el cual se quiere calcular el coseno.
    n (int): El número de términos de la serie de Taylor a utilizar en la aproximación.
    
    Retorna:
    float: La aproximación del coseno de x.
    """
    suma = 0  # Inicializa la suma que acumulará los términos de la serie
    for i in range(n):
        # Calcula cada término de la serie de Taylor para el coseno
        termino = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        suma += termino  # Suma el término calculado a la acumulada
    return suma  # Devuelve la suma como la aproximación final del coseno

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero n.
    
    Parámetros:
    n (int): Número entero no negativo cuyo factorial se desea calcular.
    
    Retorna:
    int: El factorial de n.
    """
    resultado = 1  # Inicializa el resultado del factorial
    for i in range(1, n + 1):
        resultado *= i  # Multiplica el acumulado por el valor actual de i
    return resultado  # Devuelve el factorial de n

if __name__ == "__main__":
    # Solicita al usuario que ingrese el valor de x y el número de términos n para la aproximación
    x = float(input("Ingrese el valor de x para calcular Cos(x): "))
    n = int(input("Ingrese el numero de terminos de la serie: "))
    
    # Calcula la aproximación del coseno usando la serie de Taylor con los valores ingresados
    aproximacion = aproximar_coseno(x, n)
    
    # Calcula el valor real del coseno utilizando la función de la librería math
    valor_real = math.cos(x)
    
    # Muestra la aproximación calculada, el valor real y el porcentaje de error
    print(f"Aproximacion de Cos({x}) usando {n} terminos: {aproximacion}")
    print(f"Valor real de Cos({x}): {valor_real}")
    print(f"Porcentaje de error: {((abs(valor_real - aproximacion) / valor_real) * 100):.2f} %")
