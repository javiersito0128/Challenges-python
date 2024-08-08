# Crea un sistema de encuestas donde las respuestas se almacenen en un diccionario.

# Creacion del diccionario
encuesta = {}

# Creacion de la funcion para registrar la respuesta del usuario
def respuesta (documento : int, nombre : str, resp : str):
    try:
        if documento not in encuesta:
            encuesta.update({documento : 
                {'nombre' : nombre,
                'respuesta' : resp}})
        else:
            raise SystemError
    except:
        print (f'Ya ese usuario registro una respuesta\n')
        
# Creacion del loop para registrar varias respuestas
while True:
    doc = int(input('Ingrese su documento:\n>>> '))
    nombre = input('Ingrese su nombre:\n>>> ')
    
    print('Que piensas de la IA a futuro?')
    resp = input('>>> ')
    
    respuesta(doc, nombre, resp)
    
    validation = int(input(f'[1] - resgistrar otra\n'
                           f'[2] - salir\n'
                           f'>>> '))
    
    if validation == 1:
        continue
    else:
        break

# Imprimir resultados
for doc, rest in encuesta.items():
    for x in range(1):
        name, resp = rest.values()
    print(f'Documento: {doc}\n'
            f'Nombre: {name}\n'
            f'Respuesta: {resp}\n')
