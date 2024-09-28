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
sucesivamente. Los resultados se guardan en listas, una con los nombres, \
otra con la contidad y la ultima con el costo por unidad.
'''

def ingresar_productos():
    nombres_productos = []
    cantidades_productos = []
    costos_unidad = []
    i = 1
    while True:
        nombre = input(f"Ingrese el nombre del produto {i} (o escriba 'done' \
        para finalizar):")
        if nombre == "done":
            break
        cantidad = int(input(f"Ingrese la cantidad del producto {i}:"))
        costo = float(input(f"Ingrese el costo por unidad del producto {i}:"))

        nombres_productos.append(nombre)
        cantidades_productos.append(cantidad)
        costos_unidad.append(costo)
        i += 1
    return nombres_productos, cantidades_productos, costos_unidad


'''
Aquí se hace llamar el inventario total con los valores que el usuario indicó \
anteriormente. Estos se acomodan en base a la posición de cada lista \
respectivamente.
'''

inventario = ingresar_productos()
print("\n-----RESUMEN INVENTARIO-----")
for i in inventario:
    print(i)


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
