def farmacia():
	x = 00
	while True:
		x += 1
		yield f'F-{x}'


def perfumeria():
	x = 00
	while True:
		x += 1
		yield f' P-{x} '


def cosmetica():
	x = 00
	while True:
		x += 1
		yield f' C-{x} '


f = farmacia()
p = perfumeria()
c = cosmetica()


def turno(eleccion):
	print('*' * 30)
	print('Su turno es:')
	if eleccion == 1:
		print(next(f))
	elif eleccion == 2:
		print(next(p))
	elif eleccion == 3:
		print(next(c))
	print('Espere y sera atendido en breve')
	print('*' * 30)
