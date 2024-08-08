print(f'\nIniciando el juego. . . . .')

#Preguntar el nombre al usuario
nombre = input((f'\n\nEstimado jugador ingresa tu nombre: ').lower()).capitalize()


#Bienvenida y Instrucciones del juego
print(f'\nHola {nombre}, he pensado un numero entre el 1 y el 100\nA ver si adivinas cual es :P'
      f'\n\nINSTRUCCIONES:\n'
      f'-Cuentas con solo 8 intentos para adivinar el numero que he pensado.\n'
      f'-Tras acabarse los 8 intentos sera un "GAME OVER".')


#generacion del numero aleatorio
from random import randint

numero_aleatorio = randint(1,101)


#contador de intentos
intentos = 8


#Creacion del bucle
while intentos > 0:
    numero_usuario = int(input(f'\nIngrese un numero: '))

#condiciones del juego

    #En caso de adivinar el numero
    if numero_usuario == numero_aleatorio:
        print(f'FELICIDADES HAS ADIVINADO EL NUMERO\n'
              f'Te ha tomado {intentos} intentos')
        break

    #En caso de exceder los parametros del juego
    elif numero_usuario > 100 or numero_usuario < 1:
        print(f'Entrada no valida\n'
              f'Te quedan {intentos} intentos')

    #En caso numero incorrecto
    elif numero_usuario != numero_aleatorio:
        intentos -= 1
        print(f'Numero equivocado, vuelve a intentarlo\n'
              f'Te quedan {intentos} intentos')

#En caso de agotarse lo intentos GAME OVER
else:
      print(f'\n\nLo siento, no haz adivinado el numero :(\n'
            f'GAME OVER')
