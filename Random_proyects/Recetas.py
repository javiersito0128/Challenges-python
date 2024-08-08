import shutil
from pathlib import Path
from os import system
from os import remove
import os
import time

ruta_base = Path(Path.home(), 'Recetario')
if not ruta_base.exists():
    os.makedirs(ruta_base)

os.chdir(ruta_base)

finalizar_prgrama = False

def contar_recetas():
    contador = 0
    for txt in Path(ruta_base).glob('**/*.txt'):
        contador += 1
    return contador
def mostrar_recetas(directorio):
    system('cls')
    print('-' * 50)
    print('Recetas:')
    lista_recetas = []
    contador = 1

    for txt in Path(directorio).glob('**/*.txt'):
        name = txt.stem
        print(f'[{contador}] - {name}')
        lista_recetas.append(txt)
        contador += 1
    print('-' * 50)
    if contador > 1:
        return lista_recetas
    else:
        system('cls')
        return False
def elegir_receta(lista_recetas):
    if lista_recetas != False:
        respuesta = 'x'
        while not respuesta.isnumeric() or int(respuesta) not in range(1, len(lista_recetas) + 1):
            respuesta = input('Escoja una receta:\n')
        return lista_recetas[int(respuesta) - 1]
    else:
        return False
def crear_receta(directorio):
    while True:
        system('cls')
        receta = input('Escriba el nombre de su receta:\n') + '.txt'
        ruta = Path(directorio, receta)
        if not ruta.exists():
            system('cls')
            abrir_nueva_receta = open(ruta, 'w')
            print('Escrbia su receta')
            print('*' * 50)
            print('Para terminar la receta escriba "Salir"')


            while True:
                texto = ((input()).lower()).capitalize()
                if texto != 'Salir':
                    txt = texto + '\n'
                    abrir_nueva_receta.write(txt)
                    continue
                else:
                    break
            print('*' * 50)
            abrir_nueva_receta.close()
            time.sleep(5)
            system('cls')
            print('Receta guardada')
            time.sleep(2)
            system('cls')
            break
        else:
            system('cls')
            print('Esa receta ya existe')
            time.sleep(2)
            system('cls')
            continue
def leer_receta(ruta):
    if ruta != False:
        system('cls')
        with open(ruta, 'r') as archivo:
            print('Esta es su receta:')
            print('*' * 50)
            print(archivo.read())
            print('*' * 50)
            print('Para salir escriba "Salir"')
        while True:
            txt = ((input()).lower()).capitalize()
            if txt == 'Salir':
                system('cls')
                break
            else:
                continue
    else:
        system('cls')
        print('No hay recetas en este directorio')
        time.sleep(2)
        system('cls')
def crear_directorio(ruta):
    while True:
        print("Escribe el nombre del nuevo directorio: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            time.sleep(2)
            system('cls')
            print(f'Tu directorio "{nombre_categoria}" ha sido creada')
            time.sleep(1)
            system('cls')
            break
        else:
            print("Lo siento, esa categoria ya existe")
            continue
def mostrar_directorios():
    system('cls')
    print('-' * 50)
    print("Directorios:")
    lista_direcorios = []
    contador = 1

    for carpeta in ruta_base.iterdir():
        directorio = carpeta.name
        print(f"[{contador}] - {directorio}")
        lista_direcorios.append(carpeta)
        contador += 1
    print('-' * 50)
    return lista_direcorios
def elegir_directorio(lista):
    respuesta = 'x'
    while not respuesta.isnumeric() or int(respuesta) not in range(1, len(lista) + 1):
        respuesta = input('Escoja una carpeta:\n')
    return lista[int(respuesta) - 1]
def directorios_exist():
    contador = 0
    for directorios in ruta_base.iterdir():
        contador += 1
    if contador == 0:
        system('cls')
        print('No hay directorios')
        time.sleep(2)
        system('cls')
        return False
    else:
        return True
def recetas_exist():
    if contar_recetas() == 0:
        system('cls')
        print('No hay recetas')
        time.sleep(2)
        system('cls')
        return False
    else:
        return True
def borrar_directorio(ruta):
    system('cls')
    shutil.rmtree(ruta)
    print('Directorio borrado')
    time.sleep(2)
    system('cls')
def borrar_receta(ruta):
    if ruta != False:
        system('cls')
        remove(ruta)
        print('Receta borrada\n')
        time.sleep(2)
        system('cls')
    else:
        system('cls')
        print('No hay recetas en este directorio')
        time.sleep(2)
        system('cls')


def inicio():
    system('cls')
    while not finalizar_prgrama:
        print('*' * 50)
        print('*' * 12 + ' Bienvenido al recetario ' + '*' * 13)
        print('*' * 50)
        print('\n')
        print(f'Las recetas estan en la ruta: {ruta_base}')
        print(f'Total recetas: {contar_recetas()}')


        print('Elige una opcion:')
        print('''
        [1] - Leer receta
        [2] - Crear receta
        [3] - Crear directorio
        [4] - Eliminar receta
        [5] - Eliminar directorio
        [6] - Salir''')
        print('\n')
        print('*' * 50)
        try:
            respuesta = int(input(''))
            if 1 <= respuesta <= 6:
                menu(respuesta)
            else:
                system('cls')
                print('Fuera de rango')
                time.sleep(2)
                system('cls')
        except:
            system('cls')
            print('Entrada invalida')
        continue
    print('Fin del programa')

def menu(respuesta):
    system('cls')
    global finalizar_prgrama
    while True:
        if respuesta == 1:
            if not directorios_exist():
                break
            else:
                if not recetas_exist():
                    break
                else:
                    leer_receta(elegir_receta(mostrar_recetas(elegir_directorio(mostrar_directorios()))))
                    break
        if respuesta == 2:
                if not directorios_exist():
                    break
                else:
                    crear_receta(elegir_directorio(mostrar_directorios()))
                    break
        if respuesta == 3:
            crear_directorio(ruta_base)
            break
        if respuesta == 4:
            if not directorios_exist():
                break
            else:
                if not recetas_exist():
                    break
                else:
                    borrar_receta(elegir_receta(mostrar_recetas(elegir_directorio(mostrar_directorios()))))
                    break
        if respuesta == 5:
            if not directorios_exist():
                break
            else:
                borrar_directorio(elegir_directorio(mostrar_directorios()))
                break
        if respuesta == 6:
            finalizar_prgrama = True
            break

inicio()