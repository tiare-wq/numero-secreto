import json
import os
import time

# Actualiza y muestra los resultados del usuario
def actualizar_resultados(jugador, resultado):
    if resultado:
        # Actualiza las partidas ganadas
        jugador["Partidas ganadas"] += 1

    jugador["Partidas jugadas"] += 1

    # Muestra los resultados
    print(f"📍 Estadísticas de {jugador["Nombre"]}:\n")
    for p, v in jugador.items():
        print("▪ ", p, ': ', v, sep='')
    print()

# Actualiza el TOP si el ganador está dentro de los 5 mejores puntajes
def actualizar_top(jugador, top):
    entro_al_top = False
    p_max = next((n["Puesto"] for n in top if n["Nombre"] == jugador["Nombre"]), 6) # Establece índice mínimo de 'cambiar_lugar_ranking'

    # Comparar puesto por puesto de mayor a menor cantidad de victorias.
    for i in sorted(top, key=lambda x: x["Puesto"], reverse=True):
        # Si es mayor guardar el puesto del ranking del jugador que reemplaza
        if jugador["Partidas ganadas"] > i["Partidas ganadas"]:
            jugador["Puesto"] = i["Puesto"]
            entro_al_top = cambiar_lugar_ranking(i["Puesto"], p_max, top)
            break
        # Si tiene la misma cantidad de ganadas, ubicar primero al que tenga menos partidas jugadas
        elif jugador["Partidas ganadas"] == i["Partidas ganadas"]:
            if jugador["Partidas jugadas"] < i["Partidas jugadas"]:
                jugador["Puesto"] = i["Puesto"]
                entro_al_top = cambiar_lugar_ranking(i["Puesto"], p_max, top)
                break       
            # Si tienen la misma cantidad en ambas partidas, ubicar primero a la victoria más reciente
            elif jugador["Partidas jugadas"] == i["Partidas jugadas"]:
                jugador["Puesto"] = i["Puesto"]
                entro_al_top = cambiar_lugar_ranking(i["Puesto"], p_max, top)
                break
        
    # Agregar al nuevo jugador
    if entro_al_top:
        top.append(jugador)
        if p_max == 6:
            print("Jugador entró en el TOP")

    # Eliminar al último jugador
    borrado = next((t for t in top if t["Puesto"] == 6), None)
    if borrado:
        top.remove(borrado)

# Actualiza el ranking de los demás jugadores
def cambiar_lugar_ranking(p_min, p_max, top):
    for j in sorted(top, key=lambda x: x["Puesto"], reverse=True):
        if p_min <= j["Puesto"] < p_max:
            j["Puesto"] += 1

    return True

# Carga listas de 'jugadores' y 'top', sin lanzar error si no existe
def cargar_archivos(ruta):
    if os.path.exists(ruta):
        try:
            with open(ruta, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print(f"Advertencia: El archivo {ruta} está dañado. Se usará una lista vacía.")
            return []
    else:
        return []

# Elimina los datos de las listas de 'jugadores' y 'top'
def eliminar_datos(jugadores, top):
    del jugadores[:]
    del top[:]
    print("Estadísticas reiniciadas correctamente.\n")

# Garantiza que la listas 'jugadores' y 'top' siempre se guarden en la subcarpeta correcta
def garantizar_ruta():
    CARPETA_BASE = os.path.dirname(__file__)  # Carpeta donde está el script actual
    RUTA_DATOS = os.path.join(CARPETA_BASE, "datos")
    os.makedirs(RUTA_DATOS, exist_ok=True) # Crea '/datos' si no existe, sin lanzar error si ya existe
    return RUTA_DATOS


# Guarda listas 'jugadores' y 'top' en minijuego/datos/nombre_del_archivo
def guardar_archivos(jugadores, top, ruta_j, ruta_t):
    top.sort(key=lambda x: x["Puesto"]) # Ordena la lista de 'top' por su puesto en el ranking
    with open(ruta_j, 'w', encoding='utf-8') as f:
        json.dump(jugadores, f, indent=4, ensure_ascii=False) # 'ensure_ascii=False' para caracteres especiales
    with open(ruta_t, 'w', encoding='utf-8') as f:
        json.dump(top, f, indent=4, ensure_ascii=False)

# Agrega un nuevo jugador o actualiza su ficha
def ingresar_jugador(nombre, jugadores):
    # Verifica si el nombre del jugador está ingresado, de lo contrario guarda 'None'
    jugador = next((j for j in jugadores if j["Nombre"] == nombre), None)
    if jugador:
        # Mostrar que el nombre ya está registrado
        respuesta = f"El jugador '{nombre}' ya ha sido registrado. ¿Deseas continuar de todos modos? (s/n): "
        reusar_nombre = validar_continuar(respuesta)

        # Solicitar nuevo nombre
        if reusar_nombre == 'n':
            nombre = validar_nombre()
            return ingresar_jugador(nombre, jugadores)
        
        return jugador

    jugador = {"Nombre": nombre, "Partidas jugadas": 0, "Partidas ganadas": 0}
    jugadores.append(jugador)
    print("Nuevo jugador registrado.\n")
    return jugador

# Menú
def menu():
    print("\n⚔ MENÚ DE JUEGO")
    print("1. Nueva partida")
    print("2. Ver TOP 5")
    print("3. Reiniciar archivos")
    print("4. Salir\n")

# Itera un máximo de tres veces la pregunta de cuál es el número secreto
def minijuego(num_secreto):
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
    
    time.sleep(1)    
    print(f"El número secreto era: {num_secreto}. ¡Pero estuviste cerca! Vuelve a intentarlo cuando quieras ^^.\n")

    time.sleep(1)

# Mostrar todos los resultados cuanto se cierra el programa
def mostrar_todos_los_resultados(jugadores):
    for j in jugadores:
        for p, v in j.items():
            if p == "Nombre":
                print("👤", v)
            elif p == "Puesto":
                print(f"Jugador se ubica en puesto {v} del ranking.")
            else:
                print("▪ ", p, ': ', v, sep='')
        print()

# Mostrar top
def mostrar_top(top):
    for t in sorted(top, key=lambda x: x["Puesto"]):
        print(f"{t["Puesto"]}: {t["Nombre"]}")
        print("▪ Partidas ganadas:", t["Partidas ganadas"])
        print("▪ Partidas jugadas:", t["Partidas jugadas"])
        print()

# Entrega pistas según la cantidad de intentos
def pistas(i, num_secreto, intentos):
    # Cuenta los intentos restantes
    print("¡Ese no era el número! ¡Recórcholis!")
    if i == 0:
        print("Intentos restantes: 2")

    else:
        print("Intento restante: 1")

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
def validar_continuar(continuar):
    while True:
        continuar = input(continuar).strip().lower()
        if continuar in ['s', 'n']:
            return continuar
        print("Debes ingresar s (sí) o n (no).\n")

# Verifica que es un nombre válido
def validar_nombre():
    while True:
        nombre = input("Ingresa tu nombre: ").strip()
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
        print("¡Felicitaciones, pudiste adivinar! ¡El tesoro es tuyo! 👑💰\n")
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