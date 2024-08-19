import random
jugador_1 = int(input('''Ingresa un valor para jugar: 
1. Piedra, 2. Papel, 3.Tijera
'''))
jugador_2 = comienza = random.randint(1, 3)

if jugador_1 == 1:
    print("Elegiste piedra")
elif jugador_1 == 2:
    print("Elegiste papel")
elif jugador_1 == 3:
    print("Elegiste tijera")
else:
    print("Valor ingresado no válido")

if jugador_2 == 1:
    print("PC eligió piedra")
elif jugador_2 == 2:
    print("PC eligió papel")
elif jugador_2 == 3:
    print("PC eligió tijera")
else:
    print("Valor ingresado no válido")

if jugador_1 == jugador_2:
    print("Empate")
elif (jugador_1 == 1 and jugador_2 == 3) or (jugador_1 == 3 and jugador_2 == 2) or (jugador_1 == 2 and jugador_2 == 1):
    print("Ganaste")
else:
    print("PC gana")