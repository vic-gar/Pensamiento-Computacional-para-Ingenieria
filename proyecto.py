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
del inicio para calcular el total de productos, el costo del inventario \
actual y el descuento por mayoreo. Luego se imprime el resultado al usuario.
'''

inventario_total_costo = costo_inventario(cantidad_producto_1, costo_producto_1, \
cantidad_producto_2, costo_producto_2, cantidad_producto_3, costo_producto_3, \
cantidad_producto_4, costo_producto_4, cantidad_producto_5, costo_producto_5)

print("El costo total del inventario es:", inventario_total_costo)

productos = total_productos(cantidad_producto_1, cantidad_producto_2, \
cantidad_producto_3, cantidad_producto_4, cantidad_producto_5)

print("El total de productos en el inventrio es:", productos)

print("Indica la cantidad de producto para el descuento por mayoreo y el costo \
por unidad de ese producto")
cantidad_producto_may = int(input())
costo_producto_may = float(input())
costo_mayoreo = calcular_descuento_mayoreo(cantidad_producto_may, \
costo_producto_may)

print("El costo con descuento es:", costo_mayoreo)

'''
Fin del programa
'''
