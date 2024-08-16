
opciones = {
    "izquierda" : "Te encontraste con un dragón",
    "derecha" : "Encontraste un tesoro",
    "adelante" : "Caíste en un pozo",
}

eleccion = input("Estás en un cruze. ¿Quieres ir a la derecha, izquierda o adelante?: ").lower()

if eleccion in opciones:
    print("Respuesta: ", opciones[eleccion])
    if eleccion == "derecha":
        print("Felicidades, gracias por jugar")
    elif eleccion == "izquierda":
        print("Te ha hecho cenizas, intenta de nuevo")
    elif eleccion == "adelante":
        print("Has caído, intenta de nuevo")
else:
    print("Opción incorrecta, digite una opción válida")