# Conversor de enteros a bases numericas: (binaria, octal, decimal, hexadecimal)

# Creacion de la funcion para convertir enteros a bases numericas
def convertidor_bases_numericas (numero : int, base_numerica : str):
    if base_numerica in ['bin', 'oct', 'dec', 'hex']:
        # Entero a Binario
        if base_numerica == 'bin':
            new_num = bin(numero)
            return print(f'Numero en binario: {new_num}')
        
        elif base_numerica == 'oct':
            # Entero a Octal
            new_num = oct(numero)
            return print(f'Numero en octal: {new_num}')
        
        elif base_numerica == 'dec':
            # Entero a Decimal
            new_num = float(numero)
            return print(f'Numero en decimal: {new_num}')
        
        else:
            # Entero a Hexadecimal
            new_num = hex(numero)
            return print(f'Numero en hexadecimal: {new_num}')
    else:
        pass
        
convertidor_bases_numericas(12, 'dec')
