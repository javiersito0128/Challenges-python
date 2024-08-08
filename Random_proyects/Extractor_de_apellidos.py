'''
This code is for saparate common lasts_names from latinoamerica that excel can t.
the idea is to take the list of names from excel to paste it on a txt then run the program
with the name of the file.
'''

archivo = open('nombres')
listado = archivo.readlines()
archivo.close()
new_file = open('new_file.txt', 'w+')
def apellidos_extra_largos(linea):

    if linea[3] in ['DE', 'LA', 'LAS', 'LOS', 'DEL']:
        if linea[4] in ['LA', 'LAS', 'LOS']:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]} {linea[4]} {linea[5]}\n')
            new_file.write(apellido)
        else:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]} {linea[4]}\n')
            new_file.write(apellido)
    else:
        apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]}\n')
        new_file.write(apellido)
def apellidos_largos(linea):
    if linea[2] in ['DE', 'LA', 'LAS', 'LOS', 'DEL']:
        if linea[3] in ['LA', 'LAS', 'LOS']:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]} {linea[4]}\n')
            new_file.write(apellido)
        else:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]}\n')
            new_file.write(apellido)
    else:
        apellido = (f'{linea[0]} {linea[1]} {linea[2]}\n')
        new_file.write(apellido)
def apellidos(linea):
    if linea[1] in ['DE', 'LA', 'LAS', 'LOS', 'DEL']:
        if linea[2] in ['LA', 'LAS', 'LOS']:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]} {linea[3]}\n')
            new_file.write(apellido)
        else:
            apellido = (f'{linea[0]} {linea[1]} {linea[2]}\n')
            new_file.write(apellido)
    else:
        apellido = (f'{linea[0]} {linea[1]}\n')
        new_file.write(apellido)


for line in listado:
    linea = line.split()
    if linea[0] in ['DE', 'LA', 'LAS', 'LOS', 'DEL']:
        if linea[1] in ['LA', 'LAS', 'LOS']:
            apellidos_extra_largos(linea)
        else:
            apellidos_largos(linea)
    else:
        apellidos(linea)
        continue

new_file.close()
