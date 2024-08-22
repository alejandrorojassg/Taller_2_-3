if __name__ == "__main__":
    # Solicita al usuario que ingrese palabras separadas por espacios y las almacena en una lista
    palabras = input("Ingrese palabras separadas por espacio: ").split()

    # Lista para almacenar las palabras que contienen dos o más vocales
    palabras_con_vocales = []

    # Itera sobre cada palabra en la lista ingresada
    for palabra in palabras:
        # Cuenta las vocales en la palabra utilizando una comprensión de listas dentro de la función sum()
        if sum(1 for letra in palabra if letra in "aeiou") >= 2:
            # Si la palabra contiene dos o más vocales, se agrega a la lista palabras_con_vocales
            palabras_con_vocales.append(palabra)

    # Verifica si hay palabras con dos o más vocales en la lista
    if palabras_con_vocales:
        # Itera sobre la lista de palabras que cumplen con el criterio y las imprime
        for palabra in palabras_con_vocales:
            print(f"La palabra '{palabra}' tiene dos o más vocales.")
    else:
        # Si no hay palabras con dos o más vocales, imprime un mensaje indicando eso
        print("No existe una palabra con dos o más vocales.")
