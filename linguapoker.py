## Lingua Poker es un programa en Python que ayudará
## al usuario a aprender lo básico de distintos idiomas.
import math
import random

preguntas = [
    {
        "pregunta": "¿Qué significa 'raise' en Poker?",
        "opciones": [
            "Retirarse",
            "Aumentar la apuesta",
            "Repartir cartas"
        ],
        "correcta": "Aumentar la apuesta"
    },

    {
        "pregunta": "¿Qué significa 'fold' en Poker?",
        "opciones": [
            "Retirarse",
            "Aumentar la apuesta",
            "Ganar la partida"
        ],
        "correcta": "Retirarse"
    },

    {
        "pregunta": "¿Qué significa 'check' en Poker?",
        "opciones": [
            "Pasar sin apostar",
            "Retirarse",
            "Apostar todo"
        ],
        "correcta": "Pasar sin apostar"
    },

    {
        "pregunta": "¿Qué significa 'bet' en Poker?",
        "opciones": [
            "Apostar",
            "Barajar",
            "Retirarse"
        ],
        "correcta": "Apostar"
    }
]
# Calcula el valor total del pot sumando las apuestas. --> Para cuando se agreguen las cartas y el juego de cartas
def calcularpot(bet1, bet2): 
    # Recibe dos apuestas, las suma y devuelve el total.
    return bet1 + bet2


# Calcula cuántas fichas le quedan al jugador después de apostar. --> Para cuando se agreguen las cartas y el juego de cartas
def calcfichasrestan(fichas, bet):
    # Recibe las fichas actuales y la apuesta.
    # Resta la apuesta a las fichas y devuelve el resultado.
    return fichas - bet


# Calcula la probabilidad de obtener una determinada mano de Poker. --> Para cuando se agreguen las cartas y el juego de cartas
def calcprobapoker(manofav, totcartas=52, manosize=5):
    # Calcula el total de manos posibles usando combinaciones.
    # Divide las manos favorables entre las manos posibles.
    # Convierte el resultado a porcentaje.
    totalmanos = math.comb(totcartas, manosize)
    proba = manofav / totalmanos

    return proba * 100


# Compara la puntuación del jugador con la de la computadora. --> Para cuando se agreguen las cartas y el juego de cartas
def compararscore(scorejugador, scorepc):
    # Compara puntuaciones.
    # Si la del jugador es mayor, gana el jugador. Si la de la computadora es mayor, gana la casa.
    # Si son iguales, hay empate.

    if scorejugador > scorepc:
        return "Usted gana"

    elif scorejugador < scorepc:
        return "La casa gana"

    else:
        return "Empate"


# Comprueba si la respuesta del usuario es correcta.
def reviansw(answ_usuario, answ_bien):
    # Convierte ambas respuestas a minúsculas y las compara para ver si son iguales.
    return answ_usuario.lower() == answ_bien.lower()


# Hace una pregunta de idioma al jugador.
def hacerpregunta():
    # Elige una pregunta de la lista.
    # Revuelve las opciones para cambiar la posición.
    # Muestra las opciones y recibe la respuesta.
    # Comprueba si la respuesta es correcta.

    pregunta = random.choice(preguntas)
    opciones = pregunta["opciones"].copy()
    random.shuffle(opciones)

    print("\nPregunta:")
    print(pregunta["pregunta"])

    for i in range(len(opciones)):
        print(i + 1, ".", opciones[i])

    respuesta = input("Selecciona una opción: ")

    if respuesta.isdigit():
        respuesta = int(respuesta)

        if respuesta >= 1 and respuesta <= len(opciones):
            respuesta_usuario = opciones[respuesta - 1]

            if respuesta_usuario == pregunta["correcta"]:
                print("¡Correcto!")
                return True

    print("Incorrecto.")
    print("La respuesta era:", pregunta["correcta"])

    return False


# Solicita una apuesta válida al jugador.
def pedir_apuesta(fichas):
    # Solicita una cantidad para apostar.
    # Mientras la cantidad sea inválida, vuelve a pedirla.
    # Cuando sea válida, devuelve la cantidad.

    while True:
        apuesta = int(input("¿Cuánto quieres apostar?: "))

        if apuesta > 0 and apuesta <= fichas:
            return apuesta

        else:
            print("Apuesta inválida. Intenta nuevamente.")


# Ejecuta una ronda.
def jugar_ronda(fichas):
    # Solicita una apuesta válida.
    # Calcula el pot.  --> Para cuando se agreguen las cartas y el juego de cartas
    # Hace una pregunta de idioma.
    # Si el jugador responde correctamente, recibe una recompensa.
    # Si responde incorrectamente, pierde la apuesta.
    # Finalmente devuelve las fichas actualizadas.

    apuesta = pedir_apuesta(fichas)

    pot = calcularpot(apuesta, apuesta)

    print("\nTu apuesta:", apuesta)
    print("Pot:", pot)

    correcta = hacerpregunta()

    if correcta:
        ganancias = pot * 2
        fichas = fichas + ganancias

        print("¡Ganaste la ronda!")
        print("Ganaste:", ganancias)

    else:
        fichas = fichas - apuesta

        print("Perdiste la ronda.")
        print("Perdiste:", apuesta)

    return fichas


# Ejecuta el menú principal del juego.
def juego():
    # Inicializa fichas del jugador.
    # Mientras tenga fichas, permite jugar rondas.
    # Después de cada ronda pregunta si desea continuar.
    # El juego termina si el jugador sale o se queda sin fichas.
    # 1500 fichas iniciales.

    fichas = 1500

    print("================================")
    print("         LINGUA POKER")
    print("================================""")

    while fichas > 0:

        print("\nTienes", fichas, "fichas.")

        fichas = jugar_ronda(fichas)

        if fichas <= 0:
            print("\nTe quedaste sin fichas.")
            break

        continuar = input(
            "\n¿Quieres jugar otra ronda? (s/n): "
        )

        if continuar.lower() != "s":
            break

    print("\nGracias por jugar Lingua Poker.")
    print("Fichas finales:", fichas)


# Prueba las funciones principales del programa.
def tests():
    # Ejecuta diferentes casos de prueba usando assert.
    # Si una condición es falsa, Python mostrará un error.

    assert calcularpot(100, 200) == 300

    assert calcfichasrestan(1000, 250) == 750

    assert compararscore(80, 70) == "Usted gana"
    assert compararscore(60, 90) == "La casa gana"
    assert compararscore(75, 75) == "Empate"

    assert reviansw("Raise", "raise") == True
    assert reviansw("Fold", "raise") == False

    proba = calcprobapoker(4)

    assert proba > 0
    assert proba < 1

    print("Todo funcionando")


# Ejecutar las pruebas.
tests()

# Iniciar el juego.
juego()
