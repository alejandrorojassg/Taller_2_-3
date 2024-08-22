# Definimos una función llamada "digitos" que toma un número entero como parámetro y devuelve una lista.
def digitos(num: int) -> list:
    # Creamos una lista vacía llamada "digitos_separados" que almacenará los dígitos del número.
    digitos_separados = []
    # Iniciamos un bucle while que se ejecutará mientras el número sea mayor que 0.
    while num > 0:
        # Calculamos el resto de la división del número entre 10, lo que nos da el último dígito del número.
        digito = num % 10
        # Agregamos el dígito a la lista "digitos_separados".
        digitos_separados.append(digito)
        # Dividimos el número entre 10, lo que nos permite avanzar al siguiente dígito en la próxima iteración.
        num //= 10
    # Devolvemos la lista "digitos_separados" que contiene los dígitos del número original.
    return digitos_separados

# Si el script se ejecuta directamente (no se importa como módulo), se ejecutará el siguiente código.
if __name__ == "__main__":
    # Pedimos al usuario que ingrese un número entero.
    num = int(input("digite un numero entero: "))
    # Llamamos a la función "digitos" con el número ingresado y almacenamos el resultado en la variable "digitos_separados".
    digitos_separados = digitos(num)
    # Invertimos la lista "digitos_separados" para que los dígitos estén en el orden correcto (de izquierda a derecha).
    digitos_separados.reverse()
    # Imprimimos los dígitos separados del número original.
    print(f"los digitos separados de {num} son \n {digitos_separados}")