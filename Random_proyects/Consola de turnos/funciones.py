import Generadores_Decoradores
from os import system
import time


def limpiar():
	time.sleep(2)
	system('cls')


def menu():
	while True:
		print('*' * 50)
		print(f'{" Bienvenido a Farmacias S.A.S ":*^50}')
		print('*' * 50)
		print('\n')
		print('Seleccione una opcion:\n'
		      '[1] Farmacia\n'
		      '[2] Perfumeria\n'
		      '[3] Cosmetiqueria\n'
		      '[4] Salir\n')
		respuesta = ''
		try:
			respuesta = int(input('>>> '))
			if 1 > respuesta or respuesta > 4:
				raise TypeError
		except:
			limpiar()
			print('Entrada invalida')
			limpiar()
		else:
			if respuesta == 4:
				limpiar()
				print('Fin del programa')
				limpiar()
				break
			limpiar()
			Generadores_Decoradores.turno(respuesta)
			limpiar()


menu()
