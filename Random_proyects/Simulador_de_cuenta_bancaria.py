class Persona:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):

    def __init__(self, nombre, apellido, no_cuenta, balance):
        super().__init__(nombre, apellido)
        self.no_cuenta = no_cuenta
        self.balance = balance

    def __str__(self):
        return f'Nombre: {self.nombre}\nApellido: {self.apellido}\nNumero de cuenta: {self.no_cuenta}\nBalance de la cuenta: ${self.balance}'

    def deposito(self, monto):
        self.balance += monto
        print(f'\nSu nuevo balance es: ${self.balance}\n')

    def retiro(self, monto):
        if monto <= self.balance:
            self.balance -= monto
            print(f'\nSu nuevo balance es: ${self.balance}\n')
        else:
            print('\nFondos insuficientes\n')

def crear_cliente():
    while True:
        nombre = ((input('Digite su nombre: ')).lower()).capitalize()
        comprobacion = nombre.isalpha()

        if comprobacion == True:
            break
        else:
            continue
    while True:
        apellido = ((input('Digite su apellido: ')).lower()).capitalize()
        comprobacion = apellido.isalpha()

        if comprobacion == True:
            break
        else:
            continue
    while True:
        try:
            no_cuenta = int(input('Digite su numero de cuenta: '))
            if type(no_cuenta) == int and 14 <= len(str(no_cuenta)) <= 16:
                break
        except ValueError:
            print('Numero de cuenta invalido')
    while True:
        try:
            balance = float(input('Digite el balance inicial de la cuenta: '))
            if type(balance) == float:
                break
        except ValueError:
            print('balance invalido')


    cliente = Cliente(nombre, apellido, no_cuenta, balance)

    return cliente

def inicio():
    while True:

        respuesta = ((input('Hola, deseas incribirte en el banco?\n(si/no)\n')).lower()).capitalize()

        if respuesta == 'Si':
            menu(nuevo_usuario(crear_cliente()))
            break
        elif respuesta == 'No':
            print('Una lastima, hasta pronto')
            break
        else:
            print('Su entrada no es valida\n')
            continue

def menu(cliente):
    while True:
        respuesta = ((input('\nQue accion desea Realizar?\n'
              '-Deposito\n'
              '-Retiro\n'
              '-salir\n')).lower()).capitalize()

        if respuesta == 'Deposito':
            comprobar_monto(cliente, respuesta)
        elif respuesta == 'Retiro':
            comprobar_monto(cliente, respuesta)
        elif respuesta == 'Salir':
            print('Hasta pronto')
            break
        else:
            print('Entrada no valida\n')
            continue

def nuevo_usuario(usuario):
    print('\nNuevo usuario registrado')
    print(usuario)
    return usuario

def comprobar_monto(cliente, respuesta):
    while True:
        try:
            monto = float(input(f'Ingrese el monto a {respuesta}: $'))
            if type(monto) == float:
                if respuesta == 'Retiro':
                    cliente.retiro(monto)
                elif respuesta == 'Deposito':
                    cliente.deposito(monto)
                break
        except ValueError:
            print('monto invalido')

inicio()