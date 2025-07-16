import time

# Actualiza y muestra los resultados del usuario
def actualizar_resultados(nombre, jugadores):
    jugadores[nombre]["Partidas ganadas"] = jugadores[nombre]["Partidas ganadas"] + 1

    print(f"📍 Estadísticas de {nombre}:\n")
    for p, v in jugadores[nombre].items():
        print("▪ ", p, ': ', v, sep='')

# Itera un máximo de tres veces la pregunta de cuál es el número secreto
def minijuego(num1, num2, num_secreto):
    intentos = []
    n = 3
    for i in range(3):
        while True:
            try:
                intento = int(input("¿Podrás adivinar cuál es el número secreto?\n"))
                break
            except ValueError:
                print("¿Y eso que es? ¿Se come? No, solo se aceptan números.\n")
        
        intentos.append(intento)

        print()
        time.sleep(1)

        validacion = verificar_num(i, intento, num_secreto)
        if validacion:
            return True

        if i < 2:
            pistas(i, num_secreto, intentos) # Pistas para hacer la experiencia del jugador más divertida
        
    print(f"\nEl número era: {num_secreto}. ¡Pero estuviste cerca! Vuelve a intentarlo cuando quieras ^^.\n")

# Mostrar todos los resultados cuanto se cierra el programa
def mostrar_todos_los_resultados(jugadores):
    for j in jugadores:
        print("👤", j)
        for p, v in jugadores[j].items():
            print("▪ ", p, ': ', v, sep='')
        print()

# Agrega un nuevo jugador o actualiza su ficha
def nueva_partida(nombre, jugadores):
    if nombre not in jugadores:
        jugadores[nombre] = {"Partidas jugadas": 1, "Partidas ganadas": 0}
    else:
        jugadores[nombre]["Partidas jugadas"] = jugadores[nombre]["Partidas jugadas"] + 1

# Entrega pistas según la cantidad de intentos
def pistas(i, num_secreto, intentos):
    # Cuenta los intentos restantes
    print("¡Ese no era el número! ¡Recórcholis!")
    if i == 0:
        print("Dos intentos restantes")

    else:
        print("Un intento restante")

    comparacion = "mayor" if intentos[i] > num_secreto else "menor"
    print(f"Pista: El número ingresado es {comparacion} que el número secreto.\n")

    # Si es el segundo intento, entrega una pista extra
    if i == 1:
        time.sleep(2)
        if abs(num_secreto - intentos[0]) > abs(num_secreto - intentos[1]):
            print(f"Pista extra: El número está más cerca de {intentos[1]} que de {intentos[0]}...\n")
        elif abs(num_secreto - intentos[0]) < abs(num_secreto - intentos[1]):
            print(f"Pista extra: El número está más cerca de {intentos[0]} que de {intentos[1]}...\n")
        else:
            print(f"Pista extra: El número secreto está a la misma distancia de {intentos[0]} que de {intentos[1]}...\n")

# Verifica si el jugador quiere o no seguir jugando
def validar_continuar():
    while True:
        continuar = input("\n¿Deseas seguir jugando? (s/n): ").strip().lower()
        if continuar in ['s', 'n']:
            return continuar
        print("Debes ingresar s (sí) o n (no).\n")

# Verifica que es un nombre válido
def validar_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ").strip().title()
        print()
        if any(l.isalpha() for l in nombre):
            return nombre
        print("El nombre debe tener al menos una letra.\n")


# Verifica que el número ingresado sea el número secreto
def verificar_num(i, intento, num_secreto):
    correcto = "✔\n"
    incorrecto = "❌\n"
    if intento == num_secreto:
        print(correcto)
        print("No puede ser... Has adivinado el número secreto.")
        print("¡Felicitaciones, pudiste adivinar! ¡El tesoro es tuyo!\n")
        return True
    elif i == 0:
        print(incorrecto)
        print("Nunca adivinarás. JAJAJA\n")
        return False
    elif i == 1:
        print(incorrecto)
        print("Nunca podrás obtenerlo. JAJAJA\n")
        return False
    else:
        print(incorrecto)
        print("¡No era ese!")
        print("Ahora puedes irte, JAJAJA. ¡No te molestes en volver!\n")
        return False