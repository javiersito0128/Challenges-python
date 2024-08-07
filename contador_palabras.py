# Contador de palabras de un texto

# Input del texto a reconocer
texto = input('>>> ').lower()

# Convertir el texto en una lista
texto = texto.split()

# Convertir en un set para despreciar las repeticiones
unicas = set(texto)

# Creacion del diccionario para almacenar la clave-valor
recuento_palabras = {}

# Creacion del bucle para contar las palabras del texto
for palabra in unicas:
    if palabra not in ['de', 'la', 'que', 'con', 'para', 'por', 'y', 'las']:
        no_apariciones = texto.count(palabra)
        recuento_palabras.update({palabra : no_apariciones})
    else:
        continue

# Imprimir recuento
for clave,valor in recuento_palabras.items():
    print(f'Palabra: {clave}\n'
          f'Apariciones: {valor}')

