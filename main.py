""" 'Número secreto' es un juego que consiste en ingresar dos números, un menor y uno mayor, que serán el rango del número secreto,
un número random. Se considera que es una parte del rompecabezas de un juego de aventura más grande. El Nigromante no mata al jugador,
solo no le da el tesoro. """

import funciones
import os
import random
import time
import tkinter as tk
from vista import VistaMinijuego as Vista

# Función principal
def main():
    ruta = funciones.garantizar_ruta() # Crea carpeta 'datos' si no existe, sin lanzar error si ya existe

    ruta_jugadores = os.path.join(ruta, "jugadores.json")
    jugadores = funciones.cargar_archivos(ruta_jugadores)

    ruta_top = os.path.join(ruta, "top.json")
    top = funciones.cargar_archivos(ruta_top)
    
    # Inicia Tkinter e instancia la ventana root
    root = tk.Tk()

    app = Vista(root)
        
    app.menu()

    funciones.menu()

    while True:
        try:
            opcion = int(input("Elija una opción: "))
            if opcion in range(1, 5):
                break
            print("Opción fuera de rango.\n")
        except ValueError:
            print("Debes ingresar valores numéricos.\n")

        print()
        if opcion == 1:
            print("🔮 NUEVA PARTIDA\n")
            nombre = funciones.validar_nombre()
            jugador = funciones.ingresar_jugador(nombre, jugadores)

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
                    print("¡Al menos 15 números más grande! El mago ya está poniendo caritas...\n")
                except ValueError:
                    print("¿Y eso que es? ¿Se come? No, solo se aceptan números.\n")

            num_secreto = random.randint(num1, num2) # Genera el número secreto

            print("Oh! ¡Entraste a mi juego! ¡Para obtener mi tesoro debes adivinar el número secreto! ¡Pero nadie me lo quitará! ¡JAJAJA!\n")
            time.sleep(1.5)
            print("📢 ¡Recuerda que el número secreto está entre el rango que diste!\n")

            resultado = funciones.minijuego(num_secreto)

            if resultado:
                time.sleep(1)
                print(f"Felicitaciones {jugador["Nombre"]}, has ganado el reto.\n")

            funciones.actualizar_resultados(jugador, resultado)
            # Valida si tiene las misma cantidad o más partidas ganadas que los jugadores del top
            validar_ranking = any(t["Partidas ganadas"] <= jugador["Partidas ganadas"] for t in top)
            if top and validar_ranking:
                funciones.actualizar_top(jugador, top)
            elif not top:
                jugador["Puesto"] = 1
                top.append(jugador)
                print("Jugador entró en el TOP\n")
            
            continuar = "¿Deseas volver al menú principal? (s/n): "
            respuesta = funciones.validar_continuar(continuar)
            
            if respuesta == 'n':
                print()
                funciones.guardar_archivos(jugadores, top, ruta_jugadores, ruta_top) # Guardar archivos

                time.sleep(1)
                funciones.mostrar_todos_los_resultados(jugadores)
                break
            
            time.sleep(1)
            continue
        
        elif opcion == 2:
            if top:
                print("✨ TOP 5\n")
                funciones.mostrar_top(top)
            else:
                print("Aún no hay ranking de jugadores\n")

        elif opcion == 3:
            borrar_archivos = "¿Estás seguro(a) que deseas borrar los datos de todos los jugadores? (s/n): "
            respuesta = funciones.validar_continuar(borrar_archivos)

            # Eliminar archivos
            if respuesta == 's':
                funciones.eliminar_datos(jugadores, top)
            else:
                print()
        
        else:
            funciones.guardar_archivos(jugadores, top, ruta_jugadores, ruta_top) # Guardar archivos

            funciones.mostrar_todos_los_resultados(jugadores)
            time.sleep(1)

            print("Saliendo del programa...")
            time.sleep(1)
            break

        time.sleep(1)
        input("Presiona ENTER para continuar")
    
    root.mainloop()

main()