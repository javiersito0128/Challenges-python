# Encriptador Cesar (English alphabet (A-Z))
import time
inicio = time.time()

# Variable de control del desplazamiento
n = 3

# Input para digitar la clave
clave = input('>>> ').upper()

# Variable para guardar la clave cifrada
cript_pass = ''

# Ciclo for para cifrar la clave
for char in clave:
    new_char = ord(char)
    indice = clave.index(char)
    if 65 <= new_char <= 87:
        cript_pass += chr(new_char + n) 
    elif 88 <= new_char <= 90:
        cript_pass += chr(((new_char - 88) + 65))
    else:
        pass

# Variable para guardar la clave decifrada
decript_pass = ''

# Ciclo para descifrar la clave
for char in cript_pass:
    new_char = ord(char)
    indice = cript_pass.index(char)
    if 68 <= new_char <= 90:
        decript_pass += chr(new_char - n) 
    elif 65 <= new_char <= 67:
        decript_pass += chr(((new_char + 88) - 65))
    else:
        pass

print(f'Clave cifrada: {cript_pass}')
print(f'Clave decifrada: {decript_pass}')
print(round((time.time() - inicio)/5, 2))