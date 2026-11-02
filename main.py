
## LINGUA POKER
## Programa educativo de Poker en Python.
## Su objetivo es enseñar vocabulario de Poker en inglés mediante preguntas durante el juego.

import math
import random
from collections import Counter

# ==========================================
# LISTA DE PREGUNTAS
# ==========================================

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
    },

    {
        "pregunta": "¿Qué significa 'pot' en Poker?",
        "opciones": ["Pozo de apuestas", "Carta comunitaria", "Jugador"],
        "correcta": "Pozo de apuestas"
    },

    {
        "pregunta": "¿Qué significa 'flop' en Poker?",
        "opciones": ["Las primeras tres cartas comunitarias", "La última carta", "Una apuesta"],
        "correcta": "Las primeras tres cartas comunitarias"
    },

    {
        "pregunta": "¿Qué significa 'river' en Poker?",
        "opciones": ["La quinta carta comunitaria", "La primera apuesta", "Una pareja"],
        "correcta": "La quinta carta comunitaria"
    },

    {
        "pregunta": "¿Qué significa 'all-in' en Poker?",
        "opciones": ["Apostar todas las fichas", "Retirarse", "Pasar sin apostar"],
        "correcta": "Apostar todas las fichas"
    }
]


# ==========================================
# FUNCIONES PRINCIPALES
# ==========================================

# Calcula el total del pot sumando dos apuestas.
def calcularpot(bet1, bet2):
    # Recibe dos apuestas, las suma y devuelve el total.
    return bet1 + bet2


# Calcula las fichas restantes después de una apuesta.
def calcfichasrestan(fichas, bet):
    return fichas - bet


# Calcula la probabilidad de obtener una mano de Poker.
def calcprobapoker(manofav, totcartas=52, manosize=5):
    # Calcula todas las combinaciones posibles.
    # Divide las manos favorables entre las posibles.
    # Convierte el resultado a porcentaje.

    totalmanos = math.comb(totcartas, manosize)
    proba = manofav / totalmanos

    return proba * 100


# Compara las puntuaciones del jugador y la computadora.
def compararscore(scorejugador, scorepc):
    # Determina si gana el jugador, la casa o si hay empate.

    if scorejugador > scorepc:
        return "Usted gana"

    elif scorejugador < scorepc:
        return "La casa gana"

    else:
        return "Empate"


# Comprueba si dos respuestas son iguales.
def reviansw(answ_usuario, answ_bien):
    # Convierte ambas respuestas a minúsculas y comprueba si son iguales.

    return answ_usuario.lower() == answ_bien.lower()

# ==========================================
# JUGADORES
# ==========================================

# Crea un jugador con sus datos iniciales.
def crear_jugador(nombre, fichas):
    # Recibe el nombre y las fichas iniciales.
    # Crea un diccionario con los atributos del jugador.
    # Inicializa sus cartas, apuesta y estado.
    # Devuelve el jugador creado.

    jugador = {
        "nombre": nombre,
        "fichas": fichas,
        "cartas": [],
        "apuesta": 0,
        "activo": True
    }

    return jugador


# Crea los tres participantes de la partida.
def crear_jugadores():
    # Crea un jugador humano y dos computadoras.
    # Guarda los tres jugadores dentro de una lista.
    # Devuelve la lista completa.

    jugadores = [
        crear_jugador("Player 1", 1500),
        crear_jugador("Computer 1", 1500),
        crear_jugador("Computer 2", 1500)
    ]

    return jugadores


# Muestra la información de todos los jugadores.
def mostrar_jugadores(jugadores):
    # Recorre la lista de jugadores.
    # Muestra el nombre, las fichas y el estado de cada uno.

    for jugador in jugadores:
        print("\nJugador:", jugador["nombre"])
        print("Fichas:", jugador["fichas"])
        print("Activo:", jugador["activo"])


def reiniciar_apuestas(jugadores):
    # Recorre todos los jugadores y establece su apuesta actual en cero.

    for jugador in jugadores:
        jugador["apuesta"] = 0


def procesar_accion(jugador, apuesta_actual, pozo):
    # Muestra las acciones disponibles.
    # Comprueba que la acción sea válida.
    # Calcula cuánto debe pagar el jugador.
    # Actualiza sus fichas, su apuesta y el pozo.
    # Si se retira, cambia su estado a inactivo.

    print("\nTurno de:", jugador["nombre"])
    print("Tus fichas:", jugador["fichas"])
    print("Tu apuesta actual:", jugador["apuesta"])
    print("Apuesta máxima de la ronda:", apuesta_actual)

    print("\n1. Check")
    print("2. Call")
    print("3. Raise")
    print("4. Fold")

    accion = input("Selecciona una acción: ").lower()

    if accion == "check":
        accion = "1"
    elif accion == "call":
        accion = "2"
    elif accion == "raise":
        accion = "3"
    elif accion == "fold":
        accion = "4"

    if accion == "1":
        if jugador["apuesta"] == apuesta_actual:
            print("Has pasado.")
        else:
            print("No puedes hacer Check. Debes igualar la apuesta.")
            return apuesta_actual, pozo

    elif accion == "2":
        cantidad = apuesta_actual - jugador["apuesta"]

        if cantidad == 0:
            print("Ya has igualado la apuesta.")
        elif cantidad <= jugador["fichas"]:
            jugador["fichas"] -= cantidad
            jugador["apuesta"] += cantidad
            pozo += cantidad
            print("Has igualado la apuesta.")
        else:
            print("No tienes suficientes fichas para hacer Call.")
            return apuesta_actual, pozo

    elif accion == "3":
        nueva_apuesta = input("¿Cuál será tu apuesta total en esta ronda?: ")

        if nueva_apuesta.isdigit():
            nueva_apuesta = int(nueva_apuesta)
            cantidad = nueva_apuesta - jugador["apuesta"]

            if nueva_apuesta > apuesta_actual and cantidad <= jugador["fichas"]:
                jugador["fichas"] -= cantidad
                jugador["apuesta"] = nueva_apuesta
                pozo += cantidad
                apuesta_actual = nueva_apuesta
                print("¡Has aumentado la apuesta!")
            else:
                print("Apuesta inválida.")
                return apuesta_actual, pozo
        else:
            print("Debes introducir un número.")
            return apuesta_actual, pozo

    elif accion == "4":
        jugador["activo"] = False
        print("Te has retirado de la ronda.")

    else:
        print("Acción inválida.")
        return apuesta_actual, pozo

    return apuesta_actual, pozo


def accion_computadora(jugador, apuesta_actual, pozo):
    # La computadora comprueba si necesita igualar la apuesta. Si no tiene suficientes fichas, se retira.
    # Si no necesita pagar, puede pasar o retirarse aleatoriamente.

    print("\nTurno de:", jugador["nombre"])

    if jugador["apuesta"] < apuesta_actual:
        cantidad = apuesta_actual - jugador["apuesta"]

        if cantidad <= jugador["fichas"]:
            jugador["fichas"] -= cantidad
            jugador["apuesta"] += cantidad
            pozo += cantidad
            print(jugador["nombre"], "hace Call.")
        else:
            jugador["activo"] = False
            print(jugador["nombre"], "hace Fold.")

    else:
        decision = random.choice(["check", "check", "fold"])

        if decision == "check":
            print(jugador["nombre"], "hace Check.")
        else:
            jugador["activo"] = False
            print(jugador["nombre"], "hace Fold.")

    return apuesta_actual, pozo


def ronda_apuestas(jugadores, pozo):
    # Establece la apuesta actual en cero.
    # Recorre los jugadores activos y les permite realizar acciones.
    # Si alguien aumenta la apuesta, los demás deben responder.
    # La ronda termina cuando todos los jugadores activos han respondido y tienen apuestas igualadas.

    apuesta_actual = 0
    respondieron = set() # Guarda elementos sin repetirlos

    while True:
        for i in range(len(jugadores)):
            jugador = jugadores[i]

            if not jugador["activo"]:
                continue

            if i not in respondieron or jugador["apuesta"] < apuesta_actual:

                apuesta_anterior = apuesta_actual

                if i == 0:
                    print("\nAntes de realizar tu acción...")
                    hacerpregunta()

                    apuesta_actual, pozo = procesar_accion(
                        jugador,
                        apuesta_actual,
                        pozo
                    )
                else:
                    apuesta_actual, pozo = accion_computadora(
                        jugador,
                        apuesta_actual,
                        pozo
                    )

                if apuesta_actual > apuesta_anterior:
                    respondieron = {i}
                else:
                    respondieron.add(i)

        activos = [
            (i, jugador)
            for i, jugador in enumerate(jugadores)
            if jugador["activo"]
        ]

        if len(activos) <= 1:
            break

        if all( # All comprueba si todas las condiciones son verdaderas
            i in respondieron and jugador["apuesta"] == apuesta_actual
            for i, jugador in activos
        ):
            break

    print("\nLa ronda de apuestas ha terminado.")
    print("Pozo acumulado:", pozo)

    return pozo


# Crea la baraja estándar de 52 cartas.
def crear_baraja():
    # Crea una lista con los cuatro palos y otra con los trece valores.
    # Recorre cada palo y combina cada uno con todos los valores.
    # Guarda cada carta como un diccionario dentro de la baraja.
    # Devuelve la baraja completa.

    palos = ["Hearts", "Diamonds", "Clubs", "Spades"]

    valores = [
        "2", "3", "4", "5", "6", "7",
        "8", "9", "10", "J", "Q", "K", "A"
    ]

    baraja = []

    for palo in palos:
        for valor in valores:

            carta = {
                "valor": valor,
                "palo": palo
            }

            baraja.append(carta)

    return baraja


# Revuelve las cartas.
def revolver_baraja(baraja):
    # Recibe la baraja y mezcla aleatoriamente la posición de sus cartas.
    # Devuelve la baraja mezclada.
    # Modifica la lista original, no crea una nueva.

    random.shuffle(baraja)

    return baraja


# Reparte una carta y la elimina de la baraja.
def repartir_carta(baraja):
    # Comprueba si todavía existen cartas disponibles.
    # Si hay cartas, extrae la última utilizando pop() y la devuelve.
    # Si la baraja está vacía, devuelve None.

    if len(baraja) > 0:
        return baraja.pop() ## .pop() saca un elemento de la lista y lo elimina

    else:
        return None


def repartir_cartas_privadas(jugadores, baraja):
    # Recorre dos veces la lista de jugadores.
    # En cada vuelta, reparte una carta a cada jugador.
    # Así, todos reciben dos cartas de forma alternada.

    for _ in range(2):
        for jugador in jugadores:
            carta = repartir_carta(baraja)
            jugador["cartas"].append(carta)


# Regla Burn Card: descarta una carta antes de repartir las comunitarias.
def repartir_flop(baraja):
    # Descarta una carta y reparte tres cartas comunitarias.

    repartir_carta(baraja)

    flop = []

    for _ in range(3):
        flop.append(repartir_carta(baraja))

    return flop


def repartir_turn(baraja):
    # Descarta una carta y reparte la cuarta carta comunitaria.

    repartir_carta(baraja)

    return repartir_carta(baraja)


def repartir_river(baraja):
    # Descarta una carta y reparte la quinta carta comunitaria.

    repartir_carta(baraja)

    return repartir_carta(baraja)


def jugar_rondas(jugadores, baraja):
    # Ejecuta las cuatro rondas de Texas Hold'em.
    # Después de cada etapa, organiza una ronda de apuestas.
    # Reinicia las apuestas individuales antes de cada nueva ronda.
    # Detiene la partida si solamente queda un jugador activo.

    pozo = 0
    cartas_comunitarias = []

    print("\n==============================")
    print("          PRE-FLOP")
    print("==============================")

    pozo = ronda_apuestas(jugadores, pozo)

    if sum(jugador["activo"] for jugador in jugadores) <= 1:
        return cartas_comunitarias, pozo

    reiniciar_apuestas(jugadores)

    print("\n==============================")
    print("            FLOP")
    print("==============================")

    flop = repartir_flop(baraja)
    cartas_comunitarias.extend(flop) # extend agrega elementos de una lista a otra

    mostrar_cartas(flop)

    pozo = ronda_apuestas(jugadores, pozo)

    if sum(jugador["activo"] for jugador in jugadores) <= 1: # sum suma los valroes de una colección
        return cartas_comunitarias, pozo

    reiniciar_apuestas(jugadores)

    print("\n==============================")
    print("            TURN")
    print("==============================")

    turn = repartir_turn(baraja)
    cartas_comunitarias.append(turn)

    mostrar_cartas(cartas_comunitarias)

    pozo = ronda_apuestas(jugadores, pozo)

    if sum(jugador["activo"] for jugador in jugadores) <= 1:
        return cartas_comunitarias, pozo

    reiniciar_apuestas(jugadores)
    ##Es demasiado codigo
    print("\n==============================")
    print("            RIVER")
    print("==============================")

    river = repartir_river(baraja)
    cartas_comunitarias.append(river)

    mostrar_cartas(cartas_comunitarias)

    reiniciar_apuestas(jugadores)

    pozo = ronda_apuestas(jugadores, pozo)

    return cartas_comunitarias, pozo


def mostrar_cartas(cartas):
    # Recorre la lista de cartas y muestra su valor y palo.

    for carta in cartas:
        print(carta["valor"], "of", carta["palo"])


def valor_carta(carta):
    # Convierte el valor de una carta a un número para poder comparar las cartas durante la evaluación.

    valores = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "10": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    return valores[carta["valor"]]


def obtener_escalera(valores):
    # Elimina valores repetidos y ordena las cartas.
    # Añade el As como valor 1 para reconocer escaleras bajas.
    # Comprueba si existen cinco valores consecutivos.
    # Devuelve el valor más alto de la escalera o cero si no existe.

    valores = sorted(set(valores), reverse=True)

    if 14 in valores:
        valores.append(1)
        valores = sorted(valores, reverse=True)

    contador = 1

    for i in range(len(valores) - 1):
        if valores[i] - 1 == valores[i + 1]:
            contador += 1

            if contador == 5:
                return valores[i - 3]

        else:
            contador = 1

    return 0


def evaluar_mano(cartas):
    # Recibe las siete cartas de un jugador.
    # Cuenta los valores y agrupa las cartas por palo.
    # Comprueba las combinaciones desde la más poderosa hasta la más débil y devuelve su puntuación.

    valores = [valor_carta(carta) for carta in cartas]

    conteo = Counter(valores)

    grupos = sorted(
        conteo.items(),
        key=lambda x: (x[1], x[0]),
        reverse=True
    )

    palos = {}

    for carta in cartas:
        palo = carta["palo"]

        if palo not in palos:
            palos[palo] = []

        palos[palo].append(valor_carta(carta))

    # Royal Flush y Straight Flush.
    for palo, valores_palo in palos.items():
        if len(valores_palo) >= 5:
            escalera_color = obtener_escalera(valores_palo)

            if escalera_color == 14:
                return (9, 14)

            if escalera_color > 0:
                return (8, escalera_color)

    # Four of a Kind.
    if grupos[0][1] == 4:
        kicker = max(
            valor for valor in valores
            if valor != grupos[0][0]
        )
        return (7, grupos[0][0], kicker)

    # Full House.
    ternas = [valor for valor, cantidad in grupos if cantidad == 3]
    parejas = [valor for valor, cantidad in grupos if cantidad == 2]

    if ternas and (parejas or len(ternas) >= 2):
        segunda_terna = max(parejas + ternas[1:])
        return (6, ternas[0], segunda_terna)

    # Flush.
    for valores_palo in palos.values():
        if len(valores_palo) >= 5:
            mejores = sorted(valores_palo, reverse=True)[:5]
            return (5, *mejores)

    # Straight.
    escalera = obtener_escalera(valores)

    if escalera > 0:
        return (4, escalera)

    # Three of a Kind.
    if ternas:
        kickers = sorted(
            [valor for valor in valores if valor != ternas[0]],
            reverse=True
        )[:2]

        return (3, ternas[0], *kickers)

    # Two Pair.
    if len(parejas) >= 2:
        kicker = max(
            valor for valor in valores
            if valor not in parejas[:2]
        )

        return (2, parejas[0], parejas[1], kicker)

    # One Pair.
    if parejas:
        kickers = sorted(
            [valor for valor in valores if valor != parejas[0]],
            reverse=True
        )[:3]

        return (1, parejas[0], *kickers)

    # High Card.
    mejores = sorted(valores, reverse=True)[:5]

    return (0, *mejores)


def determinar_ganadores(jugadores, cartas_comunitarias):
    # Obtiene los jugadores activos.
    # Evalúa las siete cartas de cada jugador.
    # Compara sus puntuaciones y guarda a los mejores.
    # Devuelve una lista con los ganadores.

    jugadores_activos = [
        jugador for jugador in jugadores
        if jugador["activo"]
    ]

    if len(jugadores_activos) == 1:
        return jugadores_activos, None

    ganadores = []
    mejor_puntuacion = None

    for jugador in jugadores_activos:
        siete_cartas = jugador["cartas"] + cartas_comunitarias

        puntuacion = evaluar_mano(siete_cartas)

        print("\nJugador:", jugador["nombre"])
        print("Combinación:", nombre_combinacion(puntuacion))

        if mejor_puntuacion is None or puntuacion > mejor_puntuacion:
            mejor_puntuacion = puntuacion
            ganadores = [jugador]

        elif puntuacion == mejor_puntuacion:
            ganadores.append(jugador)

    return ganadores, mejor_puntuacion


def repartir_pozo(ganadores, pozo):
    # Divide el pozo entre los ganadores.
    # Si existe un sobrante, se entrega al primer ganador.
    # Actualiza las fichas de cada ganador.

    if len(ganadores) == 0:
        return

    premio = pozo // len(ganadores)
    sobrante = pozo % len(ganadores)

    for i, jugador in enumerate(ganadores):
        cantidad = premio

        if i == 0:
            cantidad += sobrante

        jugador["fichas"] += cantidad

        print(
            jugador["nombre"],
            "recibe",
            cantidad,
            "fichas."
        )


def finalizar_partida(jugadores, cartas_comunitarias, pozo):
    # Determina los ganadores de la partida.
    # Muestra las mejores combinaciones.
    # Reparte el pozo y anuncia el resultado.

    print("\n==============================")
    print("       RESULTADO FINAL")
    print("==============================")

    ganadores, puntuacion = determinar_ganadores(
        jugadores,
        cartas_comunitarias
    )

    if len(ganadores) == 0:
        print("No hay jugadores ganadores.")
        return

    if len(ganadores) == 1:
        print("\n¡", ganadores[0]["nombre"], "ha ganado!", sep="")
    else:
        print("\n¡Tenemos un empate!")

    if puntuacion is not None:
        print(
            "Mejor combinación:",
            nombre_combinacion(puntuacion)
        )

    repartir_pozo(ganadores, pozo)


def nombre_combinacion(puntuacion):
    # Relaciona el número de puntuación con el nombre de la combinación correspondiente.

    nombres = [
        "High Card",
        "One Pair",
        "Two Pair",
        "Three of a Kind",
        "Straight",
        "Flush",
        "Full House",
        "Four of a Kind",
        "Straight Flush",
        "Royal Flush"
    ]

    return nombres[puntuacion[0]]


# ==========================================
# PREGUNTAS
# ==========================================

# Hace una pregunta aleatoria de vocabulario.
def hacerpregunta():
    # Selecciona una pregunta aleatoria.
    # Copia y mezcla sus opciones.
    # Muestra las opciones numeradas.
    # Recibe la respuesta del usuario.
    # Comprueba si es correcta, devuelve True o False.

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


# ==========================================
# SISTEMA DE APUESTAS
# ==========================================

# Solicita una apuesta válida al jugador.
def pedir_apuesta(fichas):
    # Solicita una cantidad de fichas.
    # Comprueba que sea un número positivo y que no supere las fichas disponibles.
    # Repite la solicitud si es inválida.

    while True:

        apuesta = input("¿Cuánto quieres apostar?: ")

        if apuesta.isdigit():

            apuesta = int(apuesta)

            if apuesta > 0 and apuesta <= fichas:
                return apuesta

        print("Apuesta inválida. Intenta nuevamente.")


# ==========================================
# PRUEBAS
# ==========================================

def tests():
    # Ejecuta pruebas con assert para comprobar que las funciones funcionan correctamente.

    # Pruebas de operaciones.
    assert calcularpot(100, 200) == 300
    assert calcfichasrestan(1000, 250) == 750

    # Pruebas de comparación de puntuaciones.
    assert compararscore(80, 70) == "Usted gana"
    assert compararscore(60, 90) == "La casa gana"
    assert compararscore(75, 75) == "Empate"

    # Pruebas de comparación de respuestas.
    assert reviansw("Raise", "raise") == True
    assert reviansw("Fold", "raise") == False

    # Prueba de probabilidad.
    proba = calcprobapoker(4)
    assert proba > 0
    assert proba < 1

    # Pruebas de creación de jugadores.
    jugador_prueba = crear_jugador("Test Player", 1000)

    assert jugador_prueba["nombre"] == "Test Player"
    assert jugador_prueba["fichas"] == 1000
    assert jugador_prueba["cartas"] == []
    assert jugador_prueba["apuesta"] == 0
    assert jugador_prueba["activo"] == True

    jugadores_prueba = crear_jugadores()

    assert len(jugadores_prueba) == 3
    assert jugadores_prueba[0]["nombre"] == "Player 1"
    assert jugadores_prueba[1]["nombre"] == "Computer 1"
    assert jugadores_prueba[2]["nombre"] == "Computer 2"

    # Pruebas de creación de la baraja.
    baraja_prueba = crear_baraja()

    assert len(baraja_prueba) == 52

    cartas_unicas = set(
        (carta["valor"], carta["palo"])
        for carta in baraja_prueba
    )

    assert len(cartas_unicas) == 52

    # Pruebas de reparto de cartas.
    cantidad_inicial = len(baraja_prueba)

    carta_prueba = repartir_carta(baraja_prueba)

    assert carta_prueba is not None
    assert len(baraja_prueba) == cantidad_inicial - 1

    # Prueba de mezcla de la baraja.
    baraja_prueba = crear_baraja()
    revolver_baraja(baraja_prueba)

    assert len(baraja_prueba) == 52

    # Pruebas de reparto de cartas privadas.
    jugadores_prueba = crear_jugadores()
    baraja_prueba = crear_baraja()

    revolver_baraja(baraja_prueba)
    repartir_cartas_privadas(jugadores_prueba, baraja_prueba)

    for jugador in jugadores_prueba:
        assert len(jugador["cartas"]) == 2

    assert len(baraja_prueba) == 46

    cartas_repartidas = []

    for jugador in jugadores_prueba:
        for carta in jugador["cartas"]:
            cartas_repartidas.append(
                (carta["valor"], carta["palo"])
            )

    assert len(set(cartas_repartidas)) == 6

    # Pruebas de cartas comunitarias.
    baraja_prueba = crear_baraja()
    revolver_baraja(baraja_prueba)

    flop_prueba = repartir_flop(baraja_prueba)

    assert len(flop_prueba) == 3
    assert len(baraja_prueba) == 48

    turn_prueba = repartir_turn(baraja_prueba)

    assert turn_prueba is not None
    assert len(baraja_prueba) == 46

    river_prueba = repartir_river(baraja_prueba)

    assert river_prueba is not None
    assert len(baraja_prueba) == 44

    cartas_comunitarias = flop_prueba + [
        turn_prueba,
        river_prueba
    ]

    assert len(cartas_comunitarias) == 5

    cartas_unicas = set(
        (carta["valor"], carta["palo"])
        for carta in cartas_comunitarias
    )

    assert len(cartas_unicas) == 5

    # Pruebas para reiniciar apuestas.
    jugadores_prueba = crear_jugadores()

    jugadores_prueba[0]["apuesta"] = 100
    jugadores_prueba[1]["apuesta"] = 200

    reiniciar_apuestas(jugadores_prueba)

    for jugador in jugadores_prueba:
        assert jugador["apuesta"] == 0

    # Pruebas para evaluar combinaciones.
    escalera_prueba = [10, 11, 12, 13, 14]
    assert obtener_escalera(escalera_prueba) == 14
    escalera_as_bajo = [14, 2, 3, 4, 5]
    assert obtener_escalera(escalera_as_bajo) == 5
    mano_prueba = [
        {"valor": "A", "palo": "Hearts"},
        {"valor": "A", "palo": "Spades"},
        {"valor": "A", "palo": "Clubs"},
        {"valor": "K", "palo": "Hearts"},
        {"valor": "K", "palo": "Spades"},
        {"valor": "2", "palo": "Diamonds"},
        {"valor": "3", "palo": "Clubs"}
    ]
    puntuacion = evaluar_mano(mano_prueba)
    assert puntuacion[0] == 6
    assert nombre_combinacion(puntuacion) == "Full House"
    
    # Pruebas para repartir el pozo.
    ganadores_prueba = [
        crear_jugador("Winner 1", 1000),
        crear_jugador("Winner 2", 1000)
    ]
    repartir_pozo(ganadores_prueba, 100)
    assert ganadores_prueba[0]["fichas"] == 1050
    assert ganadores_prueba[1]["fichas"] == 1050

    # Prueba de reparto con sobrante.
    ganadores_prueba = [
        crear_jugador("Winner 1", 1000),
        crear_jugador("Winner 2", 1000)
    ]
    repartir_pozo(ganadores_prueba, 101)
    assert ganadores_prueba[0]["fichas"] == 1051
    assert ganadores_prueba[1]["fichas"] == 1050

    # Prueba de un único jugador activo.
    jugadores_prueba = crear_jugadores()
    jugadores_prueba[1]["activo"] = False
    jugadores_prueba[2]["activo"] = False
    ganadores, puntuacion = determinar_ganadores(
        jugadores_prueba,
        []
    )
    assert len(ganadores) == 1
    assert ganadores[0]["nombre"] == "Player 1"
    assert puntuacion is None

    # Pruebas de las diez combinaciones de Poker.
    manos_prueba = [
        (
            [
                ("A", "Hearts"),
                ("K", "Clubs"),
                ("10", "Diamonds"),
                ("7", "Spades"),
                ("5", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            0
        ),
        (
            [
                ("A", "Hearts"),
                ("A", "Clubs"),
                ("10", "Diamonds"),
                ("7", "Spades"),
                ("5", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            1
        ),
        (
            [
                ("A", "Hearts"),
                ("A", "Clubs"),
                ("K", "Diamonds"),
                ("K", "Spades"),
                ("5", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            2
        ),
        (
            [
                ("A", "Hearts"),
                ("A", "Clubs"),
                ("A", "Diamonds"),
                ("K", "Spades"),
                ("5", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            3
        ),
        (
            [
                ("2", "Hearts"),
                ("3", "Clubs"),
                ("4", "Diamonds"),
                ("5", "Spades"),
                ("6", "Hearts"),
                ("K", "Clubs"),
                ("A", "Diamonds")
            ],
            4
        ),
        (
            [
                ("2", "Hearts"),
                ("5", "Hearts"),
                ("8", "Hearts"),
                ("J", "Hearts"),
                ("K", "Hearts"),
                ("3", "Clubs"),
                ("A", "Diamonds")
            ],
            5
        ),
        (
            [
                ("A", "Hearts"),
                ("A", "Clubs"),
                ("A", "Diamonds"),
                ("K", "Hearts"),
                ("K", "Spades"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            6
        ),
        (
            [
                ("A", "Hearts"),
                ("A", "Clubs"),
                ("A", "Diamonds"),
                ("A", "Spades"),
                ("K", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            7
        ),
        (
            [
                ("5", "Hearts"),
                ("6", "Hearts"),
                ("7", "Hearts"),
                ("8", "Hearts"),
                ("9", "Hearts"),
                ("K", "Clubs"),
                ("A", "Diamonds")
            ],
            8
        ),
        (
            [
                ("10", "Hearts"),
                ("J", "Hearts"),
                ("Q", "Hearts"),
                ("K", "Hearts"),
                ("A", "Hearts"),
                ("3", "Clubs"),
                ("2", "Diamonds")
            ],
            9
        )
    ]

    for cartas, resultado_esperado in manos_prueba:
        mano = [
            {"valor": valor, "palo": palo}
            for valor, palo in cartas
        ]

        resultado = evaluar_mano(mano)

        assert resultado[0] == resultado_esperado

    #Pruebas del sistema educativo.
    assert len(preguntas) >= 8

    for pregunta in preguntas:
        assert len(pregunta["opciones"]) == 3
        assert pregunta["correcta"] in pregunta["opciones"]


    print("¡Todas las pruebas funcionan!")


# ==========================================
# INICIO
# ==========================================

tests()

jugadores = crear_jugadores()
baraja = crear_baraja()
revolver_baraja(baraja)

print("\n==============================")
print("        LINGUA POKER")
print("==============================")

repartir_cartas_privadas(jugadores, baraja)

print("\nTus cartas privadas:")
mostrar_cartas(jugadores[0]["cartas"])

cartas_comunitarias, pozo = jugar_rondas(
    jugadores,
    baraja
)

finalizar_partida(
    jugadores,
    cartas_comunitarias,
    pozo
)

print("\n==============================")
print("       ESTADO FINAL")
print("==============================")

mostrar_jugadores(jugadores)

print("\nPozo final:", pozo)
print("Cartas restantes:", len(baraja))

print("\n==============================")
print("       FIN DE LA PARTIDA")
print("==============================")

print("\nCartas comunitarias:")
mostrar_cartas(cartas_comunitarias)

print("\nEstado de los jugadores:")
mostrar_jugadores(jugadores)

print("\nPozo acumulado:", pozo)
print("Cartas restantes:", len(baraja))

