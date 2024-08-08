# Sistema de inventario con manejo de errores

# Creacion del diccionario para el inventario
inventario = {}

# Creacion de la funcion para añadir al diccionario
def crear_articulo (articulo : str, cantidad : int):
    if articulo in inventario:
        return None
    else:
        inventario.update({articulo : cantidad})

# Creacion de la funcion para actualizar el inventario +
def update_add_cant (articulo : str, cantidad : int):
    try:
        if articulo in inventario:
            cantidad = abs(cantidad)
            try:
                add = inventario[articulo] + cantidad
                inventario[articulo] = add
                print(f'Cantidad en stock: {inventario[articulo]}')
            except:
                print('No hay suficientes articulos para retirar')
        else:
            pass
    except:
        print('No esta en el inventario este articulo')
    
# Creacion de la funcion para actualizar el inventario -
def update_minus_cant (articulo : str, cantidad : int):
    try:
        if articulo in inventario:
            try:
                rest = inventario[articulo] - cantidad
                if rest < 0:
                    raise ValueError
                else:
                    inventario[articulo] = rest
                    print(f'Cantidad en stock: {inventario[articulo]}')
            except:
                print('No hay suficientes articulos para retirar')
        else:
            raise ValueError
    except:
        print('No esta en el inventario este articulo')
        
crear_articulo('perico', 5)
update_add_cant('perico', 2)
update_minus_cant('perico', 3)