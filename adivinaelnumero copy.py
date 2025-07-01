import random

print("¡Bienvenido al juego de Adivina el Número!")
numero_secreto = random.randint(1, 20)
intentos = 0

while True:
    intento = int(input("Adivina un número entre 1 y 20 "))
    intentos += 1

    if intento == numero_secreto:
        print(f"¡Correcto! Lo adivinaste en {intentos} intento(s).")
        break
    else:
        print("Incorrecto. Intenta de nuevo.")
