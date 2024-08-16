
opciones = {
    "izquierda" : "Te encontraste con un dragón",
    "derecha" : "Encontraste un tesoro",
    "adelante" : "Caíste en un pozo",
}

eleccion = input("Estás en un cruze. ¿Quieres ir a la derecha, izquierda o adelante?: ")

if eleccion in opciones:
    print("Respuesta: ", opciones[eleccion])
else:
    print("opción incorecta")
    