##Lingua Poker es un programa en python que ayudará al usuario a aprender lo básico de distintos idiomas
##<------------------------Rodr_r--------------------------->
import math
##Funciones
def calcularpot(bet1, bet2):
    return bet1 + bet2
def calcfichasrestan(fichas,bet):
    return fichas - bet
def calcprobapoker(manofav,totcartas = 52, manosize = 5):
    totalmanos = math.comb(totcartas,manosize)
    proba = manofav / totalmanos
    return proba * 100
def compararscore(scorejugador,scorepc):
    if scorejugador > scorepc:
        return "Usted gana"
    elif scorejugador < scorepc:
        return "La casa gana"
    else:
        return "Empate"
def reviansw(answ_usuario, answ_bien):
    return answ_usuario.lower() == answ_bien.lower()
def tests():
    ##<----------- assert comprueba si es verdadero ---------->
    ##Calcular pot
    assert calcularpot(100,200) == 300
    ##Calcular fichas restantes
    assert calcfichasrestan(1000,250) == 750
    ##Comparar scores
    assert compararscore(80,70) == "Usted gana"
    assert compararscore(60,90) == "La casa gana"
    assert compararscore(75,75) == "Empate"
    ##Revisar respuesta
    assert reviansw("Raise","raise") == True
    assert reviansw("Fold","raise") == False
    proba = calcprobapoker(4)
    assert proba > 0
    assert proba < 1
    print("Todo funcionando")


##Calculations
##Probabilidad de Royal Flush y confirmar que funciona compararscore
"""print(f"Probabilidad de Royal Flush: {proba:.6f}%")"""
"""resultado = compararscore(85,72)
print(resultado)""" ## Imprime "Usted gana"
"print(total_manos)" ## Da un total de 2,598,960 combinaciones
"""answ = reviansw("Raise", "raise")
print(answ)""" #Confirmar que funciona respuesta de usuario minuscula mayuscula

##
fichas_iniciales = 1500
apuesta = 100

##
fichas_restantes = fichas_iniciales - apuesta
pot = 200
ganancias = pot * 2

##Probabilidades
##Las barajas tienen 52 cartas, cada mano son 5
total_manos = math.comb(52,5)  ##Comb calcula cuantas formas de 5 cartas hay eb las 52 sin importar orden
proba = calcprobapoker(4) ##Hay 4 royal flush

tests()