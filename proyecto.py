'''
El proyecto se basa en un gestor de inventario para tiendas, actualmente el \
proyecto solo cuenta con 5 productos máximo, se pedirán el nombre del \
producto al usuario, la cantidad de ese mismo producto y el costo \
por unidad del producto. Con estos datos se otorgarán datos para facilitar \
ciertos operativos dentro de la tienda.
'''
'''
Inicio del programa
'''

'''
Esta función indica el precio a mayoreo dependiendo de la cantidad del \
producto comprado, siendo todos el mismo producto, y su costo unitario, \
así, podemos indicar que si se compró entre 20  y 49 productos se aplica \
un descuento del 15%, si compras más de 49 se hace un descuento del 25%
'''

def calcular_descuento_mayoreo(cantidad_producto,costo_producto):
    if cantidad_producto >= 50:
        descuento = 0.25
    elif cantidad_producto >= 20 and cantidad_producto < 50:
        descuento = 0.15
    else:
        descuento = 0
    costo = cantidad_producto * costo_producto
    costo_descuento = costo * (1 - descuento)
    return costo_descuento



'''
En esta etapa se le indica al usuario que coloque la totalidad de productos \
con su nombre, total de productos que hay actualmente y su precio por unidad. \
Utilizamos un ciclo while para que el numero de veces que pide al usuario \
un producto sea infinito o hasta que el usuario indique 'done'. El programa \
indica el numero del producto con un acumulador que despues de cada iteración \
de un nuevo producto sume 1, así indicando que el siguiente sea 2 y así\
sucesivamente. Los valores de la acumuación, del nombre, de la cantidad \
y del costo por unidad se guardan para poder utilizarlos para modificar estos \
valores después.
'''

acum = 1
while True:

    nombre_producto = input(f"Ingrese el nombre del producto {acum} (Escriba done para terminar):")

    if nombre_producto == "done":
        break

    cantidad_producto = int(input(f"Ingrese la cantidad de unidades de {nombre_producto}:"))
    precio_producto = float(input(f"Ingrese el costo por unidad de {nombre_producto}:"))

    globals()[f"nombre_producto_{acum}"] = nombre_producto
    globals()[f"cantidad_producto_{acum}"] = cantidad_producto
    globals()[f"precio_producto_{acum}"] = precio_producto

    print(f"Producto {acum}: {nombre_producto}, {cantidad_producto} unidades, ${precio_producto} cada producto.")

    acum = acum + 1

'''
Aquí se hace llamar el inventario total con los valores que el usuario indicó \
anteriormente.
'''

print("\n----INVENTARIO----")
for i in range (1, acum):
    nombre = globals()[f"nombre_producto_{i}"]
    cantidad = globals()[f"cantidad_producto_{i}"]
    precio = globals()[f"precio_producto_{i}"]
    print(f"Producto{i}: {nombre}, Cantidad: {cantidad}, Precio{precio}")


'''
Para finalizar, se mandan los datos dados por el usuario a las fuciones \
del inicio para calcular el descuento por mayoreo. Luego se imprime el \
resultado al usuario.
'''

print("\n Indica la cantidad de producto para el descuento por mayoreo y el \
costo por unidad de ese producto")

cantidad_producto_may = int(input())
costo_producto_may = float(input())

costo_mayoreo = calcular_descuento_mayoreo(cantidad_producto_may, \
costo_producto_may)

print("El costo con descuento es:", costo_mayoreo)

'''
Fin del programa
'''
