# Generador de contraseñas

import random
import string


# Creacion de la longitud de la contraseña
length = 30

# Creacion de la contraseña alfanumerica
password = ''.join(random.choices(string.ascii_letters + string.digits, weights = None, cum_weights = None, k = length))

# Imprimir contraseña generada
print(password)