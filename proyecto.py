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
    numero_productos = int(input("Ingrese el numero de productos que incluirá en su inventario "))
    while i <= numero_productos:
        producto = []
        j = 1
        while j == 1:
            nombre = input(f"Ingrese el nombre del producto {i}: ")
            cantidad = int(input(f"Ingrese la cantidad del producto {i}: "))
            costo = float(input(f"Ingrese el costo por unidad del producto {i}: "))

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
Aquí se hace llamar el inventario total con los valores que el usuario indicó
anteriormente. Estos se acomodan en base a la posición de cada lista
respectivamente.
'''

inventario = ingresar_productos()
print("\n--------RESUMEN INVENTARIO--------")
for i in inventario:
    print("Nombre:",i[0]," Cantidad:",i[1]," Costo por unidad:",i[2])



'''
Por ultimo se llama a la función para calcluar el costo total del inventario
que se imprime automaticamente despues de desplegar el resumen del mismo.
'''

costo_inventario = costo_inventario(inventario)
print("\nEl costo total del inventario es:\n", "$",costo_inventario)

'''
Fin del programa
'''
