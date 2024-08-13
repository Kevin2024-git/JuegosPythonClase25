def laberinto():
    laberinto = {
        "entrada": {"norte": "pasillo", "sur": None, "este": None, "oeste": None},
        "pasillo": {"norte": "salida", "sur": "entrada", "este": "cuarto oscuro", "oeste": None},
        "cuarto oscuro": {"norte": None, "sur": None, "este": None, "oeste": "pasillo"},
        "salida": {"norte": None, "sur": "pasillo", "este": None, "oeste": None}
    }
    posicion_actual = "entrada"

    print("¡Bienvenido al Laberinto!")
    print("Tu objetivo es llegar a la salida.")

    while True:
        print(f"Estás en el {posicion_actual}.")
        direccion = input("¿A dónde te gustaría ir? (norte/sur/este/oeste): ").lower()

        if direccion in laberinto[posicion_actual]:
            nueva_posicion = laberinto[posicion_actual][direccion]
            if nueva_posicion is not None:
                posicion_actual = nueva_posicion
                if posicion_actual == "salida":
                    print("¡Felicidades! Has escapado del laberinto.")
                    break
            else:
                print("No puedes ir en esa dirección.")
        else:
            print("Dirección no válida. Intenta de nuevo.")

laberinto()
