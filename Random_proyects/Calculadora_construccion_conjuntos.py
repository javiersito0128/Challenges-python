# Programa para construccion de conjuntos recidenciales (solo contemplara las torres)

# Solicitar datos al usuario
    # Datos del conjunto por torre B = base de la torre en metros, cant_tor = cantidad de torres del conjunto residencial
b = float(input('Ingrese en metros la base del edificio a construir:\n>>> '))
cant_tor = int(input('Ingrese en enteros la cantidad de torres a construir:\n>>> '))

    # Medidas de dentro el edificio cant_pisos = cantidad de pisos por torre, pisos_altura = altura de cada piso de la torre en metros
cant_pisos = int(input('Ingrese en enteros la cantidad de pisos a construir:\n>>> '))
pisos_altura = float(input('Ingrese en metros la altura de cada piso:\n>>> '))

    # Calcular altura del edificio a partir de los pisos solicitados H = altura total de la torre en metros
h = cant_pisos * pisos_altura


# Creacion de las medidas de un ladrillo referencia N3 en metros
    # Base del ladrillo en metros
ladrillo_n3_base = 0.4
    # Altura del ladrillo en metros
ladrillo_n3_altura = 0.2
    # Grosor del ladrillo en metros
ladrillo_n3_grosor = 0.08
    # Area del ladrillo referencia N3
ladrillo_n3_area = ladrillo_n3_altura * ladrillo_n3_base


# Calculo de los ladrillos necesarios para el total de la construccion
    # Calcular el total de las bases, alturas en metros y sus areas en m^2
        # Bases totales de todas las torres
total_de_bases = ((b * cant_tor) * (cant_pisos + 1))
        # Area de las bases
area_bases = total_de_bases *2
        # Altura totales de todas las torres se multiplica por 4 debido a las 4 paredes de cada torre
total_de_alturas = ((h * 4) * cant_tor)
        # Area de las Paredes, se multiplica por 4 debido a la igualdad de (4b x h4)
        #ya la altura se habia multiplicado por 4 en total alturas
area_paredes = total_de_alturas * (total_de_bases * 4)

    # Calculo de ladrillos apartir de los datos ingresados por el usuario
        # Calculo del total de ladrillos en bases (incluye los pisos)
total_de_ladrillos_bases = round(total_de_bases / ladrillo_n3_area, 2)
        # Calculo del total de ladrillos en paredes
total_de_ladrillos_paredes = round(area_paredes / ladrillo_n3_area, 2)


# Creacion del volumen del concreto en metros a:l:g (ancho, largo y grosor)
    # Grosor del concreto para una estabilidad optima de la estructura en m
grosor_concreto = 0.2
    # Volumen total de los pisos en m^3 (se multiplica por 2 para contemplar las 2 caras de las bases)
volumen_pisos = (area_bases * 2) * grosor_concreto
    # Volumen total de las paredes en m^3 (se multiplica por 2 para contemplar las 2 caras de las paredes)
volumen_paredes = (area_paredes * 2) * grosor_concreto
    # Volumen total de toda la construccion en m^3
volumen_total = volumen_paredes + volumen_pisos


# Calculo para cantidad de concreto total necesitado, en base de 11m^3
    # Materiales necesarios para hacer 11m^3 de concreto
        # Bolsas de cemento 50kg
bolsas_de_cemento = 55
        # Arena en m^3
arena = 6.27
        # Grava en m^3
grava = 7.32
        # Agua en lts
agua = 2821.5

    # Calculo de materiales totales necesarios en base a los volumenes
proporciones_totales = volumen_total / 11

    # Materiales necesarios para hacer el total del concreto
        # Bolsas de cemento 50kg totales con las proporciones resultantes
bolsas_de_cemento_total = round(bolsas_de_cemento * proporciones_totales, 2)
        # Arena en m^3 totales con las proporciones resultantes
arena_total = round(arena * proporciones_totales, 2)
        # Grava en m^3 totales con las proporciones resultantes
grava_total = round(grava * proporciones_totales, 2)
        # Agua en lts totales con las proporciones resultantes
agua_total = round(agua * proporciones_totales, 2)

print(f'Ladrillos necesarios: {(total_de_ladrillos_bases + total_de_ladrillos_paredes):,}\n'
      f'Materiales necesarios para el concreto:\n'
      f'- Bolsas de cemento: {bolsas_de_cemento_total:,}\n'
      f'- Arena: {arena_total:,} m^3\n'
      f'- Grava: {grava_total:,} m^3\n'
      f'- Agua: {agua_total:,} lts')
