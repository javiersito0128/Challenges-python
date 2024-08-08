import shutil
from pathlib import Path
from os import system
from os import remove
import os
import time #liberia time sirve para hacer pausas en tu codigo

base = Path.home()
carpeta = Path(base, 'Desktop', 'Recetario')
comprobar_ruta = Path(carpeta, 'Recetas.txt')


def inicio():

    if not carpeta.exists():
        os.makedirs(carpeta)

    os.chdir(carpeta)

    if not comprobar_ruta.exists():
        recetas = open('Recetas.txt', 'w')
        recetas.close()


    while True:

        system('cls')
        respuesta = ((input('¡Hola!, deseas acceder al Recetario?\n'
                            '(Si/No)\n\n')).lower()).capitalize()
        if respuesta == 'Si':
            system('cls')
            menu()

        elif respuesta == 'No':
            system('cls')
            print('Oh, una pena, Hasta luego.')
            break

        else:
            system('cls')
            print('Entrada no valida')
            time.sleep(2)
            continue


def menu():
    while True:
        system('cls')
        respuesta = (input('Hola, Bienvenido al recetario\n'
                           'Que deseas hacer?\n'
                           '-Crear Directorio\n'
                           '-Crear Receta\n'
                           '-Ver Directorio\n'
                           '-Editar Receta\n'
                           '-Borrar directorio\n'
                           '-Borrar receta\n'
                           '-salir\n\n')).lower()

        if respuesta == 'crear directorio':
            system('cls')
            while True:

                directorio_nuevo = ((input('Si deseas regresar al menu anterior escribe "salir"\n\n'
                                           'Ingresa el nombre del nuevo directorio:\n')).lower()).capitalize()
                if directorio_nuevo == 'Salir':
                    break
                if comprobar_recetario(directorio_nuevo):

                    ruta = Path(carpeta, directorio_nuevo)
                    os.makedirs(ruta)
                    open_recetario_anexar(directorio_nuevo)
                    system('cls')
                    print('Directorio nuevo creado')
                    time.sleep(3)
                    break
                else:
                    system('cls')
                    print('Ese directorio ya existe!!!')
                    continue

        elif respuesta == 'crear receta':

            if directorios_no_exist():
                continue

            else:

                system('cls')

                while True:

                    print('Si desea volver al menu anterior escriba "salir"\n')
                    leer_recetario()
                    directorio = ((input('En que directorio deseas agregar la nueva receta?\n')).lower()).capitalize()

                    if directorio == 'Salir':
                        system('cls')
                        break

                    else:

                        if not comprobar_recetario(directorio):
                            system('cls')
                            salir = False
                            while True:
                                if salir:
                                    system('cls')
                                    break
                                receta_nueva = ((input('Ingresa el nombre de la nueva receta:\n')).lower()).capitalize()

                                if not comprobar_recetas(receta_nueva):
                                    system('cls')
                                    while True:
                                        escribir_nueva_receta = ((input('Desea escribir enseguida la nueva receta?\n'
                                                                        '(Si/No)\n\n')).lower()).capitalize()
                                        if escribir_nueva_receta == 'Si':
                                            system('cls')
                                            respuesta = 'Nueva'
                                            escribir_receta(directorio, receta_nueva, respuesta)
                                            system('cls')
                                            print('Receta guardada')
                                            time.sleep(2)
                                            salir = True
                                            break
                                        elif escribir_nueva_receta == 'No':
                                            ruta = Path(carpeta, directorio, convertir_a_texto(receta_nueva))
                                            abrir = open(ruta, 'w')
                                            abrir.close()
                                            system('cls')
                                            print('Sera para despues')
                                            time.sleep(3)
                                            salir = True
                                            break
                                        else:
                                            system('cls')
                                            print('Entrada no valida')
                                            continue
                                else:
                                    system('cls')
                                    print('Esa receta ya esta hecha!!!\n')
                                    continue
                            break
                        else:
                            system('cls')
                            print('Ese directorio no existe!!!\n')
                            continue

        elif respuesta == 'editar receta':

            system('cls')

            if directorios_no_exist():
                continue
            else:

                if recetas_no_exist():
                    system('cls')
                    continue
                else:

                    while True:

                        print('Si desea volver al menu anterior escriba "salir"\n')

                        leer_recetas()
                        print('\n')
                        receta_buscar = ((input('Elige la receta:\n')).lower()).capitalize()

                        if receta_buscar == 'Salir':
                            break
                        elif comprobar_recetas(receta_buscar):
                            editar_receta(receta_buscar)
                            time.sleep(3)
                            system('cls')
                            print('Receta editada\n')

                            while True:

                                salir = ((input('Si desea editar otra receta escriba "editar"\n'
                                                'Para regresar al menu anterior escriba "Salir"\n')).lower()).capitalize()
                                if salir == 'Salir':
                                    break
                                elif salir == 'Editar':
                                    system('cls')
                                    break
                                else:
                                    system('cls')
                                    print('Entrada no valida')
                                    continue
                            if salir == 'Salir':
                                break
                            elif salir == 'Editar':
                                continue
                        else:
                            system('cls')
                            print('Esa receta no existe!!!\n')
                            continue

        elif respuesta == 'ver directorio':

            system('cls')

            if directorios_no_exist():
                continue

            else:

                while True:

                    leer_recetario()
                    directorio = ((input('Para regresar al menu anterior escriba "Salir"\n'
                                         'En que directorio deseas buscar?\n')).lower()).capitalize()

                    if not comprobar_recetario(directorio):

                        system('cls')

                        if recetas_no_exist():
                            system('cls')
                            continue
                        else:

                            while True:

                                leer_recetas_directorio(directorio)
                                print('\n')
                                receta = ((input('Para volver al menu anterior escriba "Salir"\n'
                                                 'Que receta deseas ver?\n')).lower()).capitalize()
                                if comprobar_recetas(receta):

                                    system('cls')

                                    ver_recetario(directorio, receta)
                                    system('cls')
                                    break
                                elif receta == 'Salir':
                                    system('cls')
                                    break
                                else:
                                    system('cls')
                                    print('Esa receta no existe!!!\n')
                                    continue
                    elif directorio == 'Salir':
                        system('cls')
                        break
                    else:
                        system('cls')
                        print('Ese directorio no existe!!!\n')
                        continue
                continue

        elif respuesta == 'borrar directorio':
            system('cls')

            if directorios_no_exist():
                continue
            else:

                while True:
                    system('cls')
                    leer_recetario()
                    directorio = ((input('Para regresar al menu anterior escriba "Salir"\n'
                                         'Que directorio deseas borrar?\n')).lower()).capitalize()
                    if directorio == 'Salir':
                        system('cls')
                        break
                    if not comprobar_recetario(directorio):

                        system('cls')

                        while True:

                            system('cls')

                            respuesta = ((input('Estas seguro?\n'
                                                '(Si/No)\n')).lower()).capitalize()
                            if respuesta == 'Si':
                                system('cls')
                                abrir_lectura = open(comprobar_ruta, 'r+')
                                abrir_lectura.seek(0)
                                lista = abrir_lectura.readlines()
                                abrir_lectura.close()
                                abrir = open(comprobar_ruta, 'w+')
                                for elemento in lista:
                                    if elemento == (directorio + '\n'):
                                        indice = lista.index(elemento)
                                        lista.pop(indice)
                                    else:
                                        continue
                                abrir.writelines(lista)
                                abrir.close()
                                ruta = Path(carpeta, directorio)
                                shutil.rmtree(ruta)
                                print('Directorio borrado')
                                time.sleep(2)

                                break
                            elif respuesta == 'No':
                                system('cls')
                                break
                            else:
                                system('cls')
                                print('Entrada no valida\n')
                                time.sleep(2)
                                continue
                        continue
                    else:
                        system('cls')
                        print('Entrada no valida\n')
                        time.sleep(2)
                        continue
                continue

        elif respuesta == 'borrar receta':

            system('cls')

            if directorios_no_exist():
                continue

            else:

                while True:

                    leer_recetario()
                    directorio = ((input('Para regresar al menu anterior escriba "Salir"\n'
                                         'En que directorio deseas buscar?\n')).lower()).capitalize()
                    if directorio == 'Salir':
                        system('cls')
                        break
                    if not comprobar_recetario(directorio):

                        system('cls')

                        if recetas_no_exist():
                            system('cls')
                            continue
                        else:

                            while True:

                                leer_recetas_directorio(directorio)
                                print('\n')
                                receta = ((input('Para volver al menu anterior escriba "Salir"\n'
                                                 'Que receta deseas borrar?\n')).lower()).capitalize()

                                if receta == 'Salir':
                                    system('cls')
                                    break
                                elif comprobar_recetas(receta):

                                    system('cls')

                                    respuesta = ((input('Estas seguro?\n'
                                                        '(Si/No)\n')).lower()).capitalize()

                                    if respuesta == 'Si':
                                        system('cls')
                                        ruta = Path(carpeta, directorio, convertir_a_texto(receta))
                                        remove(ruta)
                                        print('Receta borrada\n')
                                        time.sleep(2)
                                        break
                                    elif respuesta == 'No':
                                        system('cls')
                                        break
                                    else:
                                        system('cls')
                                        print('Entrada no valida\n')
                                        time.sleep(2)

                                        continue
                                else:
                                    system('cls')
                                    print('Esa receta no exise!!!\n')
                                    continue
                            continue
                    else:
                        system('cls')
                        print('Ese diccionario no existe!!!\n')
                        continue
                continue

        elif respuesta == 'salir':
            system('cls')
            break

        else:
            system('cls')
            print('Entrada no valida')
            time.sleep(2)
            continue


def directorios_no_exist():

    system('cls')

    comprobar = open(comprobar_ruta)
    lista = comprobar.readlines()
    comprobar.close()

    if len(lista) == 0:
        system('cls')
        print('No haz creado ningun directorio')
        time.sleep(2)
        return True

    else:
        False
def recetas_directorios_no_exist(directorio):

    contador_directorio = 0

    for arch in Path(carpeta, directorio).glob('**/*.txt'):
        contador_directorio += 1

    if contador_directorio == 0:
        system('cls')
        print('No haz creado ninguna receta')
        time.sleep(2)
        return True

    else:
        return False
def recetas_no_exist():

    contador_recetas = 0

    for arch in Path(carpeta).glob('**/*.txt'):
        name = arch.name

        if name == 'Recetas.txt':
            continue

        else:
            contador_recetas += 1

    if contador_recetas == 0:
        system('cls')
        print('No haz creado ninguna receta')
        time.sleep(2)
        return True

    else:
        return False
def ver_recetario(directorio, receta):
    system('cls')

    for arch in Path(carpeta, directorio).glob('**/*.txt'):

        name = arch.name

        if name == convertir_a_texto(receta):

            ruta = Path(arch)
            abrir = open(ruta, 'r')
            abrir.seek(0)
            print(f'Esta es tu receta:\n'
                  f'{abrir.read()}')

            while True:
                respuesta = ((input('\nQue deseas hacer?\n'
                                    '-Salir\n'
                                    '-Editar\n')).lower()).capitalize()

                if respuesta == 'Salir':
                    system('cls')
                    break

                elif respuesta == 'Editar':
                    system('cls')
                    editar_receta(receta)
                    break

                else:
                    print('Entrada no valida')

            abrir.close()
            break

        else:
            continue
def convertir_a_texto(receta):
    receta = receta + '.txt'
    return receta
def editar_receta(editar_receta):
    system('cls')

    for arch in Path(carpeta).glob('**/*.txt'):

        name = arch.name
        stem = arch.stem

        if name == convertir_a_texto(editar_receta):

            ruta = Path(arch)
            abrir = open(ruta, 'r')
            abrir.seek(0)
            lista = abrir.readlines()
            abrir.close()

            if len(lista) == 0:

                ruta = Path(os.path.dirname(arch))
                directorio = ruta.name
                respuesta = 'Existente'
                escribir_receta(directorio, stem, respuesta)

            else:

                while True:

                    respuesta = ((input('Desea añadir informacion nueva o remplazar la existente?\n'
                                        '(nueva/existente/salir)\n')).lower()).capitalize()

                    if respuesta == 'Nueva':
                        ruta = Path(os.path.dirname(arch))
                        directorio = ruta.name
                        escribir_receta(directorio, stem, respuesta)
                        break

                    elif respuesta == 'Existente':
                        abrir_nuevo = open(ruta, 'w+')
                        salir = False
                        for line in lista:

                            if salir:
                                system('cls')
                                break
                            else:
                                while True:

                                    print(line)
                                    respuesta = ((input('Quieres cambiar esta linea?\n'
                                                        '(Si/No/Salir)\n')).lower()).capitalize()
                                    indice = lista.index(line)

                                    if respuesta == 'Si':
                                        system('cls')
                                        linea_nueva = ((input('Ingrese la nueva informacion:\n'
                                                              'Finalice el cambio presionando "enter"\n\n')).lower()).capitalize()
                                        linea_nueva = linea_nueva + '\n'
                                        lista[indice] = linea_nueva
                                        system('cls')
                                        print('Linea editada\n')
                                        break

                                    elif respuesta == 'No':
                                        system('cls')
                                        print('Siguiente linea\n')
                                        break
                                    elif respuesta == 'Salir':
                                        system('cls')
                                        salir = True
                                        break
                                    else:
                                        system('cls')
                                        print('Entrada no valida\n')
                                        continue

                        abrir_nuevo.writelines(lista)
                        system('cls')
                        print('Asi quedo su receta')
                        abrir_nuevo.seek(0)
                        print(abrir_nuevo.read())
                        abrir_nuevo.close()
                        time.sleep(3)
                        break
                    elif respuesta == 'Salir':
                        system('cls')
                        break
                    else:
                        system('cls')
                        print('Entrada no valida\n')
                        continue

        else:
            continue
def leer_recetas():

    print('Estas son todas sus recetas:')

    for arch in Path(carpeta).glob('**/*.txt'):
        name = arch.name
        if name == 'Recetas.txt':
            continue
        else:
            print(arch.stem)
def leer_recetas_directorio(directorio):

    print(f'Estas son sus recetas de {directorio}:')

    for arch in Path(carpeta, directorio).glob('**/*.txt'):
        name = arch.name
        if name == 'Recetas.txt':
            continue
        else:
            print(arch.stem)
def leer_recetario():
    recetario = Path(carpeta, 'Recetas.txt')
    abrir = open(recetario)
    leer = abrir.read()
    print('Estos son los directorios disponibles:')
    print(leer)
    abrir.close()
def escribir_receta(directorio, receta, respuesta):

    if respuesta == 'Nueva':
        system('cls')
        ruta = Path(carpeta, directorio, convertir_a_texto(receta))
        abrir_modo_anexar = open(ruta, 'a+')

        longuitud = open(ruta, 'r')
        lista = longuitud.readlines()
        longuitud.close()

        if len(lista) >= 1:
            print('Esta es tu receta:\n')
            abrir_modo_anexar.seek(0)
            print(abrir_modo_anexar.read())
        else:
            pass

        print('\nAñada lineas a su receta:\n'
              'Cuando termine de escribir pulsar "enter" y escriba "salir"\n')

        while True:

            texto = ((input('')).lower()).capitalize()

            if texto != 'Salir':
                abrir_modo_anexar.write(f'{texto}\n')
                continue

            else:
                abrir_modo_anexar.close()
                break
    if respuesta == 'Existente':
        ruta = Path(carpeta, directorio, convertir_a_texto(receta))
        abrir_modo_sobrescritura = open(ruta, 'w+')
        print('Escriba su receta:\n'
              'Cuando termine de escribir pulsar "enter" y escriba "salir"\n')

        while True:
            texto = ((input('')).lower()).capitalize()
            if texto != 'Salir':
                abrir_modo_sobrescritura.write(f'{texto}\n')
                continue
            else:
                abrir_modo_sobrescritura.close()
                break
def comprobar_recetas(receta_nueva):
    contador1 = 0
    contador2 = 0

    for arch in Path(carpeta).glob('**/*.txt'):
        contador1 += 1

    for arch in Path(carpeta).glob('**/*.txt'):

        name = arch.name

        if name == convertir_a_texto(receta_nueva):
            return True

        else:

            contador2 += 1

            if contador1 == contador2:
                return False

            else:
                continue
def comprobar_recetario(directorio):
    ruta = Path(carpeta, directorio)
    if not ruta.exists():
        return True
    else:
        False
def open_recetario_anexar(nuevo_directorio):
    ruta = Path(carpeta / 'Recetas.txt')
    abrir = open(ruta, 'a')
    abrir.write(f'{nuevo_directorio}\n')
    abrir.close()

inicio()
