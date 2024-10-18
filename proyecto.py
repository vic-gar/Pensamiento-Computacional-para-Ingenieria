"""
Evidencia proyecto Python.
Simulador para almacen de inventario.
El programa realiza un inventario en base a la cantidad de productos que
el usuario desea ingresar. Pide el nombre del producto, su cantidad y su
costo por unidad. En base al inventario se ejecutan diversas funciones hasta que
el usuario indique cerrar el programa.
"""

"""
======================== Funciones de ingreso de datos ========================
"""

def ingresar_productos():
    """
    (uso de funciones, ciclos, ciclos anidados, listas, listas anidadas)
    función auxiliar de ingreso de productos, esta funcion no recibe parametros,
    los genera para funciones posteriores.
    Genera la matriz de inventario para que por cada posición, siendo
    esta una lista, se coloquen los valores de nombre, cantidad y precio del
    producto deseado en la lista.
    devuelve: matriz del inventario con cadenas, enteros y floats.
    """
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

            nombre = nombre.lower()

            producto.append(nombre)
            producto.append(cantidad)
            producto.append(costo)
            j += 1
        inventario.append(producto)
        i += 1
    return inventario


def costo_inventario(inventario):
    """
    (uso de operadores, funciones, ciclos)
    recibe: inventario matriz de cadenas, enteros y floats
    Genera el producto de la cantidad y el costo por unidad de cada producto en
    la matriz y los suma al total.
    devuelve: total costo del inventario acumulado floats.
    """
    total = 0
    for producto in inventario:
        total += producto[1] * producto[2]
    return total


def modifica_cantidad(inventario, producto):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: inventario matriz de cadenas, enteros y floats; producto cadena de
    texto.
    Modifica el valor de la cantidad en entero del producto indicado por el
    usuario en la matriz inventario.
    devuelve: inventario matriz de cadenas, enteros y floats.
    """
    producto = producto.lower()
    producto = producto.strip()
    for prod in range(len(inventario)):
        if inventario[prod][0] == producto:
            nueva_cantidad = int(input(f"Indica la nueva cantidad \
de {producto} "))
            inventario[prod][1] = nueva_cantidad
            return inventario
    print("Producto invalido")


def modifica_precio(inventario, producto):
    """
    (uso de funciones, condicionales, ciclos)
    recibe: inventario matriz de cadenas, enteros y floats; producto cadena de
    texto.
    Modifica el valor del costo en entero del producto indicado por el usuario
    en la matriz inventario.
    devuelve: inventario matriz de cadenas, enteros y floats.
    """
    producto = producto.lower()
    producto = producto.strip()
    for prod in range(len(inventario)):
        if inventario[prod][0] == producto:
            nuevo_precio = float(input(f"Indica el nuevo costo de {producto} "))
            inventario[prod][2] = nuevo_precio
            return inventario
    print("Producto invalido")

"""
========================= Parte principal del programa =========================
"""

#Se imprime el resumen del inventario
inventario = ingresar_productos()
print("\n--------RESUMEN INVENTARIO--------")
for i in inventario:
    print("Nombre:",i[0],"//"" Cantidad:",i[1],"//"" Costo por unidad:",i[2])


#menú de opciones
while True:
    opcion = input("\nIndica la opción que quieras elegir: \n1. Costo del \
inventario \n2. Modificar cantidad \n3. Modificar costo\n4. \
Finalizar programa\n")
    opcion = opcion.lower()

    if opcion == 'costo del inventario' or opcion == "1":
        total_inventario = costo_inventario(inventario)
        print("\nEl costo total del inventario es:\n", "$",total_inventario)
    elif opcion == 'modificar cantidad' or opcion == "2":
        producto = input("\nIndica el producto que quieras modificar: ")
        inventario = modifica_cantidad(inventario,producto)
        print("\nNuevo inventario con respecto de la cantidad\n",
        inventario)
    elif opcion == 'modificar costo' or opcion == "3":
        producto = input("\nIndica el producto que quieras modificar: ")
        inventario = modifica_precio(inventario,producto)
        print("\nNuevo inventario con respecto del precio por unidad\n",
        inventario)
    elif opcion == 'finalizar programa' or opcion == "4":
        print("\nPrograma finalizado.")
        break
    else:
        print("entrada no valida")
