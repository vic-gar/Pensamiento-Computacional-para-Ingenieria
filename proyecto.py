'''
El proyecto se basa en un gestor de inventario para tiendas, actualmente el
proyecto solo cuenta con 5 productos máximo, se pedirán el nombre del
producto al usuario, la cantidad de ese mismo producto y el costo
por unidad del producto. Con estos datos se otorgarán datos para facilitar
ciertos operativos dentro de la tienda.
'''
'''
Inicio del programa
'''
'''
En esta etapa se le indica al usuario que coloque la totalidad de productos
con su nombre, total de productos que hay actualmente y su precio por unidad.
Utilizamos un ciclo while para que el numero de veces que pide al usuario
un producto sea infinito o hasta que el usuario indique 'done'. El programa
indica el numero del producto con un acumulador que despues de cada iteración
de un nuevo producto sume 1, así indicando que el siguiente sea 2 y así
sucesivamente. Los resultados se guardan en listas, una con los nombres,
otra con la contidad y la ultima con el costo por unidad.
'''

def ingresar_productos():
    inventario = []
    i = 1
    numero_productos = int(input("Ingrese el numero de productos que incluirá \
en su inventario "))
    while i <= numero_productos:
        producto = []
        j = 1
        while j == 1:
            nombre = input(f"Ingrese el nombre del producto {i}: ")
            cantidad = int(input(f"Ingrese la cantidad del producto {i}: "))
            costo = float(input(f"Ingrese el costo por unidad del \
producto {i}: "))

            producto.append(nombre)
            producto.append(cantidad)
            producto.append(costo)
            j += 1
        inventario.append(producto)
        i += 1
    return inventario

'''
En esta funcion se calcula el costo total del inventario, se itera en cada
elemento de la matriz, siendo cada elemento de esta una lista, y se multiplica
el valor en la posicion 1 por el valor de la posición 2, para luego pasar al
siguiente elemento en la matriz.
'''
def costo_inventario(inventario):
    total = 0
    for producto in inventario:
        total += producto[1] * producto[2]
    return total

'''
En estas dos funciones siguientes se hace llamar al inventario para modificarlo
y hacerlo un diccionario, uno que sea espefífico de las cantidades de los
productos y otro para los precios, y así poder modificar sus valores dependiendo
de lo que el usuario desee.
'''
'''
Función de cantidad
'''

def dicc_cantidad(inventario):
    matriz = []
    i = 0
    while i < len(inventario):
        lista = []
        j = 0
        while j < 1:
            producto = inventario[i][0]
            cantidad = inventario[i][1]
            lista.append(producto)
            lista.append(cantidad)
            j += 1
        matriz.append(lista)
        i+=1
    diccionario = dict(matriz)
    return diccionario

'''
Funcion de costo
'''

def dicc_precio(inventario):
    matriz = []
    i = 0
    while i < len(inventario):
        lista = []
        j = 0
        while j < 1:
            producto = inventario[i][0]
            precio = inventario[i][2]
            lista.append(producto)
            lista.append(precio)
            j += 1
        matriz.append(lista)
        i+=1
    diccionario = dict(matriz)
    return diccionario

'''
En las siguientes funciones podemos modificar los costos y cantidades de los
productos al llamar dentro de estas funciones a las funciones anteriores que
convirtieron el inventario a diccionarios.
'''
'''
Funcion de cantidad
'''

def modifica_cantidad(inventario, producto):
    diccionario = dicc_cantidad(inventario)
    if producto in diccionario:
        nueva_cantidad = int(input(f"Indica la nueva cantidad de {producto}: "))
        diccionario[producto] = nueva_cantidad
    else:
        print("Entrada invalida")
    return diccionario

'''
Funcion de costo
'''
def modifica_precio(inventario, producto):
    diccionario = dicc_precio(inventario)
    if producto in diccionario:
        nuevo_precio = float(input(f"Indica el nuevo precio de {producto}: "))
        diccionario[producto] = nuevo_precio
    else:
        print("Entrada invalida")
    return diccionario


'''
Aquí se hace llamar el inventario total con los valores que el usuario indicó
anteriormente. Estos se acomodan en base a la posición de cada lista
respectivamente.
'''

inventario = ingresar_productos()
print("\n--------RESUMEN INVENTARIO--------")
for i in inventario:
    print("Nombre:",i[0],"//"" Cantidad:",i[1],"//"" Costo por unidad:",i[2])



'''
Por ultimo se imprime un menú para poder acceder a algunas funciones extras,
como cosultar el costo total del inventario, cambiar alguna cantidad o
cambiar algun precio de algun producto.
'''

opcion = input("\nIndica la opción que quieras elegir: \n1. Costo del \
inventario \n2. Modificar cantidad \n3. Modificar costo\n").lower()
if(opcion == 'costo del inventario'):
    costo_inventario = costo_inventario(inventario)
    print("\nEl costo total del inventario es:\n", "$",costo_inventario)
elif(opcion == 'modificar cantidad'):
    producto = input("\nIndica el producto que quieras modificar: ")
    modifica_cantidad = modifica_cantidad(inventario,producto)
    print("\nNuevo inventario con respecto de la cantidad\n",modifica_cantidad)
elif(opcion == 'modificar costo'):
    producto = input("\nIndica el producto que quieras modificar: ")
    modifica_precio = modifica_precio(inventario,producto)
    print("\nNuevo inventario con respecto del precio por \
unidad\n",modifica_precio)
else:
    print("entrada no valida")

'''
Fin del programa
'''
