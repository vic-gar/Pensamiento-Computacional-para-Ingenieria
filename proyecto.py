'''
El proyecto se basa en un gestor de inventario para tiendas, actualmente el \
proyecto solo cuenta con 5 productos máximo, se pedirán el nombre del \
producto al usuario, la cantidad de ese mismo producto y el costo \
por unidad del producto. Con estos datos se otorgarán datos como el costo del \
inventario y el total de productos.
'''
'''
Inicio del programa
'''
'''
Se define una función para calcular el costo del inventario, multiplicando la \
cantidad de productos de un tipo por el costo por unidad del mismo producto, y \
posteriormente sumando los resultados de cada uno de los productos dados.
'''

def costo_inventario(prod_1, cos_1, prod_2, cos_2, prod_3, cos_3, prod_4, \
cos_4, prod_5, cos_5):
     val_1 = prod_1 * cos_1
     val_2 = prod_2 * cos_2
     val_3 = prod_3 * cos_3
     val_4 = prod_4 * cos_4
     val_5 = prod_5 * cos_5
     costo = val_1 + val_2 + val_3 + val_4 + val_5
     return costo

'''
Se define una segunda función para calcular el total de productos sumando la \
cantidad dada de cada uno de los productos.
'''

def total_productos(prod_1, prod_2, prod_3, prod_4, prod_5):
    productos = prod_1 + prod_2 + prod_3 + prod_4 + prod_5
    return productos

'''
En esta etapa se le indica al usuario que coloque la totalidad de productos \
con su nombre, total de productos que hay actualmente y su precio por unidad. \
Ahora solo utilizaremos 5 productos en total.
'''

print("Coloca el nombre del producto 1, su cantidad y su precio por unidad")
nom_producto_1 = str(input())
cantidad_producto_1 = int(input())
costo_producto_1 = int(input())

print("Coloca el nombre del producto 2, su cantidad y su precio por unidad")
nom_producto_2 = str(input())
cantidad_producto_2 = int(input())
costo_producto_2 = int(input())

print("Coloca el nombre del producto 3, su cantidad y su precio por unidad")
nom_producto_3 = str(input())
cantidad_producto_3 = int(input())
costo_producto_3 = int(input())

print("Coloca el nombre del producto 4, su cantidad y su precio por unidad")
nom_producto_4 = str(input())
cantidad_producto_4 = int(input())
costo_producto_4 = int(input())

print("Coloca el nombre del producto 5, su cantidad y su precio por unidad")
nom_producto_5 = str(input())
cantidad_producto_5 = int(input())
costo_producto_5 = int(input())

'''
Para finalizar, se mandan los datos dados por el usuario a las fuciones \
del inicio para calcular el total de productos y el costo del inventario \
actual. Luego se imprime el resultado al usuario.
'''

inventario = costo_inventario(cantidad_producto_1, costo_producto_1, \
cantidad_producto_2, costo_producto_2, cantidad_producto_3, costo_producto_3, \
cantidad_producto_4, costo_producto_4, cantidad_producto_5, costo_producto_5)

print("El costo total del inventario es:", inventario)

productos = total_productos(cantidad_producto_1, cantidad_producto_2, \
cantidad_producto_3, cantidad_producto_4, cantidad_producto_5)

print("El total de productos en el inventrio es:", productos)

'''
Fin del programa
'''
