# Función para convertir un número racional a un número entero
def convertir_a_entero(num: float) -> int:
    """
    Convierte un número racional (con decimales) a un número entero al eliminar el punto decimal.
    
    Parámetros:
    num (float): El número racional que se desea convertir a entero.

    Retorna:
    int: El número convertido a entero, sin parte decimal.
    """
    factor = 1  # Inicializa el factor que se usará para multiplicar y eliminar la parte decimal
    while num % 1 != 0:
        # Multiplica el número por 10 hasta que no tenga parte decimal
        num *= 10
        factor *= 10  # Actualiza el factor de multiplicación
    return int(num)  # Convierte y retorna el número como un entero

def digitos(num: int) -> list:
    """
    Separa los dígitos de un número entero y los devuelve como una lista.

    Parámetros:
    num (int): El número entero del cual se quiere separar los dígitos.

    Retorna:
    list: Una lista de los dígitos separados del número.
    """
    digitos_separados = []  # Lista para almacenar los dígitos separados
    while num > 0:
        # Obtiene el dígito más a la derecha usando el operador módulo
        digito = num % 10
        # Añade el dígito a la lista
        digitos_separados.append(digito)
        # Elimina el dígito más a la derecha del número
        num //= 10
    return digitos_separados  # Devuelve la lista de dígitos separados

if __name__ == "__main__":
    # Solicita al usuario que ingrese un número racional (con decimales)
    num = float(input("Digite un número racional: "))
    
    # Convierte el número racional a un número entero (eliminando los decimales)
    num_entero = convertir_a_entero(num)
    
    # Separa los dígitos del número entero obtenido
    digitos_separados = digitos(num_entero)
    
    # Invierte el orden de los dígitos para mostrarlos en el orden correcto
    digitos_separados.reverse()
    
    # Imprime los dígitos separados en el orden original
    print(f"Los dígitos separados de {num_entero} son \n{digitos_separados}")
