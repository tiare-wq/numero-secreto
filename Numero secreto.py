""" 'Número secreto' es un juego que consiste en ingresar dos números, un menor y uno mayor, que serán el rango del número secreto,
un número random. Se considera que es una parte del rompecabezas de un juego de aventura más grande. El Nigromante no mata al jugador,
solo no le da el tesoro.

Aún no domino bien JSON y txt por lo tanto no decidí no implementarlo. """

from funciones_NS import actualizar_resultados, minijuego, mostrar_todos_los_resultados, nueva_partida, validar_continuar, validar_nombre
import random
import time

# Función principal
def main():
    jugadores = {}

    while True:
        print("🔮 NUEVA PARTIDA\n")
        nombre = validar_nombre()
        nueva_partida(nombre, jugadores)

        # Solicita dos números, con un rango mínimo de 15. Se utiliza try/except para garantizar que sean números enteros
        while True:
            try:
                num1 = int(input("Ingrese el primer número (piénsalo bien...): "))
                break
            except ValueError:
                print("¿Y eso que es? ¿Se come? No, solo se aceptan números.\n")
        while True:
            try:
                num2 = int(input("Ingrese el segundo número (debe ser MAYOR que el primero): "))

                if num2 - num1 >= 15: # Comprueba el rango
                    break
                print("¡Al menos 15 números más grande! O sino el mago no aceptará...\n")
            except ValueError:
                print("¿Y eso que es? ¿Se come? No, solo se aceptan números.\n")

        num_secreto = random.randint(num1, num2) # Genera el número secreto

        print("Oh! ¡Entraste a mi juego! ¡Para obtener mi tesoro debes adivinar el número secreto! ¡Pero nadie me lo quitará! ¡JAJAJA!\n")
        time.sleep(2)
        print("📢 ¡Recuerda que el número secreto está entre el rango que diste!\n")

        resultado = minijuego(num1, num2, num_secreto)

        if resultado:
            time.sleep(1)
            print(f"Felicitaciones {nombre}, has ganado el reto.\n")

            actualizar_resultados(nombre, jugadores)
        
        respuesta = validar_continuar()
        
        if respuesta == 'n':
            mostrar_todos_los_resultados(jugadores)
            break

main()