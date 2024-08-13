import random

def ahorcado():
    palabras = ["python", "programacion", "ahorcado", "desarrollo", "juego"]
    palabra_secreta = random.choice(palabras)
    letras_adivinadas = []
    intentos = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print("_ " * len(palabra_secreta))

    while intentos > 0:
        letra = input("Adivina una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya adivinaste esa letra. Intenta otra vez.")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra_secreta:
            print("¡Bien hecho! Esa letra está en la palabra.")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        palabra_mostrada = [letra if letra in letras_adivinadas else "_" for letra in palabra_secreta]
        print(" ".join(palabra_mostrada))

        if "_" not in palabra_mostrada:
            print("¡Felicidades! Adivinaste la palabra.")
            break
    else:
        print(f"Lo siento, te quedaste sin intentos. La palabra era '{palabra_secreta}'.")

ahorcado()
