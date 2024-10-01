import os.path
import pickle

from envio import *


# --------------------------------------------------------------
#                   Opcion 1
# --------------------------------------------------------------
def validar_opcion(mensaje):
    print(" 1 - " + mensaje)
    print(" 0 - Cancelar.")
    op = int(input("Ingresar opción: "))
    while op > 1 or op < 0:
        print(" 1 - " + mensaje)
        print(" 0 - Cancelar.")
        op = int(input("Ingresar opción (una opción valida): "))
    return op


def opcion1(csv, fd):
    """
    strip(): Está función esta ahí para eliminar los carácteres en blanco,
    incluyendo saltos de línea al final de cada línea que se lee.

    split(","): Divide cada línea en una lista de elementos, usando la coma como delimitador.
    Así que por cada línea, obtendrás una lista con los valores separados por comas.

    :param csv: -> Archivo.csv a leer
    :param fd: -> Archivo Binario a sobre-escribir cada vez que se elija la opcion
    :return: -> Sobre-escribe el archivo binario "fd"
    """
    if os.path.exists(fd):
        mensaje = "Desea crear y sobre-escribir el archivo binario nuevamente?"
        op = validar_opcion(mensaje)
        if op == 0:
            print("Ha cancelado la operacion de generar nuevamente el archivo binario.")
            return

    archivo_csv = open(csv, "r")   # read csv para recuperar los datos
    m = open(fd, "wb")  # write binary, crea el archivo, y sobreescribe el contenido

    cont = 0
    for linea in archivo_csv:
        cont += 1
        if cont >= 3:
            lista_linea = linea.strip().split(",")
            # lista_linea = ['8547', 'Del $ol 456.', '4', '2']
            # codigo STR, direccion STR, tipo INT, pago INT
            codigo = lista_linea[0]
            direccion = lista_linea[1]
            tipo = int(lista_linea[2])
            pago = int(lista_linea[3])

            env = Envio(codigo, direccion, tipo, pago)
            pickle.dump(env, m)     # env = objeto a guardar, m = archivo donde guardar
            m.flush()   # opcional # Garantizar que se escriban los datos en el archivo inmediatamente

    print(f"Se cargo el archivo binario con {cont-2} registros")
    archivo_csv.close()
    m.close()


# --------------------------------------------------------------
#                   Opcion 2
# --------------------------------------------------------------
def validar_rango(inf, sup, msj):
    # funcion reutilizada del tp3
    valor = int(input(msj))
    while sup < valor or valor < inf:
        print("El valor ingresado no es correcto. Intente nuevamente.")
        valor = int(input(msj))
    return valor


def opcion2(fd):
    """
    2 - Cargar por teclado los datos de un envio, aplicando procesos de validación para cada campo, y
    agregar un registro con esos datos directamente al final del archivo binario. Cada vez que se elija
    esta opción, el nuevo registro debe agregarse al final del archivo binario, sin perder ninguno de los
    registros que el archivo ya contenía. Si el archivo no existiese, debe ser creado y luego agregar el
    registro cargado.
    :param fd: -> nombre del archivo binario
    :return:
    """
    m = open(fd, "ab")  # append binary, para agregar elementos al final del archivo conservando su contenido anterior

    # codigo STR, direccion STR, tipo INT, pago INT
    codigo = input("Codigo postal: ")
    direccion = input("Direccion postal: ")
    tipo = validar_rango(0, 6, "Tipo de envio (entre 0 y 6): ")
    pago = validar_rango(1, 2, "Forma de pago (entre 1 y 2): ")
    env = Envio(codigo, direccion, tipo, pago)
    pickle.dump(env, m)

    print("Carga terminada")
    print()
    m.close()


# --------------------------------------------------------------
#                   Opcion 3
# --------------------------------------------------------------
def opcion3(fd):
    """
    3 - Mostrar todos los datos de todos los registros del archivo binario, tal como están grabados (sin
    ningún proceso de ordenamiento previo). Cada registro debe ocupar una sola línea en pantalla, y
    debe mostrarse también el nombre del país al que corresponde el código postal.
    :param fd: -> nombre del archivo binario
    :return:
    """
    if not os.path.exists(fd):
        print(f"No existe el archivo: {fd}"
              f"\nIngrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        env = pickle.load(m)
        print(env)

    m.close()


# --------------------------------------------------------------
#                   Opcion 4
# --------------------------------------------------------------
def opcion4(fd, cp):
    """
    4 - Mostrar todos los registros del archivo binario cuyo código postal sea igual a cp, siendo cp
    un valor que se carga por teclado. Al final del listado mostrar una línea adicional indicando cuántos
    registros se mostraron. (BUSQUEDA SECUENCIAL)
    :param fd: -> nombre del archivo binario
    :param cp: -> codigo postal a buscar
    :return:
    """
    if not os.path.exists(fd):
        print(f"No existe el archivo: {fd}"
              f"\nIngrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    cont = 0
    while m.tell() < tam:
        env = pickle.load(m)
        if env.codigo == cp:
            print(env)
            cont += 1

    print(f"Se mostraron la cantidad de {cont} registros.")
    m.close()


# --------------------------------------------------------------
#                   Opcion 5
# --------------------------------------------------------------
def opcion5(fd, d):
    """
    5 - Buscar si existe en el archivo binario un registro cuya dirección postal sea igual a d, siendo
    d un valor que se carga por teclado. Si existe mostrar el registro completo. Si no existe indicar
    con un mensaje.
    La búsqueda debe detenerse al encontrar el primer registro que coincida con el criterio pedido.
    :param fd: -> nombre del archivo binario
    :param d: -> direccion postal a buscar
    :return:
    """
    if not os.path.exists(fd):
        print(f"No existe el archivo: {fd}"
              f"\nIngrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)
    se_encontro = False     # bandera para saber si encontramos el resultado o no

    while m.tell() < tam:
        env = pickle.load(m)
        if env.direccion == d:
            print(env)
            se_encontro = True
            break

    if not se_encontro:
        print(f"No se encontró un registro en el archivo con la dirección {d}")

    m.close()


# --------------------------------------------------------------
#                   Opcion 6
# --------------------------------------------------------------
def opcion6(fd):
    """
    6 - Determinar y mostrar la cantidad de envíos de cada combinación posible entre tipo de envío y forma
    de pago en el archivo binario. Como son siete tipos de envíos posibles y son dos las formas de pago
    posibles, entonces se trata de 7 * 2 = 14 contadores, que obviamente deben ser gestionados en una
    matriz de conteo. Muestre solo los contadores cuyo valor final sea diferente de cero.
    :param fd: -> archivo binario a leer
    :return:
    """
    if not os.path.exists(fd):
        print(f"No existe el archivo: {fd}"
              f"\nIngrese primero algún registro con la opción 1 o 2.")
        return

    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    f = 2   # f = forma_pago(1, 2) -> env.pago
    c = 7   # c = tipo_envio(0, 6) -> env.tipo
    matriz = [[0] * c for i in range(f)]

    while m.tell() < tam:
        env = pickle.load(m)
        matriz[env.pago-1][env.tipo] += 1
    m.close()

    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            if matriz[f][c] > 0:
                print(f"Tipo Envio: {c} | Forma Pago: {f+1} | Cantidad: {matriz[f][c]}")

    return matriz


# --------------------------------------------------------------
#                   Opcion 7
# --------------------------------------------------------------
def opcion7(matriz):
    """
    7 - En base a la matriz que se pidió generar en el ítem anterior, muestre la cantidad total de envíios
    contados por cada tipo de envío posible, y la cantidad total de envíos contados por cada forma de
    pago posible. Es decir, se pide por un lado, totalizar las filas de esa matriz, y por otro, totalizar las
    columnas.
    :param matriz: -> matriz generada en el punto 6
    :return:
    """
    # f = forma_pago(1, 2) -> env.pago
    # c = tipo_envio(0, 6) -> env.tipo

    for f in range(len(matriz)):
        cant_total_pago = 0
        for c in range(len(matriz[0])):
            cant_total_pago += matriz[f][c]
        print(f"Forma de Pago: {f+1} | Cantidad total de envios: {cant_total_pago}")

    print()
    for c in range(len(matriz[0])):
        cant_total_tipo = 0
        for f in range(len(matriz)):
            cant_total_tipo += matriz[f][c]
        print(f"Tipo de Envío: {c} | Cantidad total de envios: {cant_total_tipo}")


# --------------------------------------------------------------
#                   Opcion 8
# --------------------------------------------------------------
def opcion8_promedio(fd):
    """
    8 - Recorrer el archivo binario, y calcular el importe promedio pagado entre todoslos envíos que figuran
    en el archivo. Y ahora sí, generar en memoria un arreglo de registros/objetos con todos los envíos
    del archivo binario cuyo importe sea mayor al promedio que acaba de calcular. Muestre el arreglo,
    pero ordenado de menor a mayor de acuerdo al código postal. En este punto, los programadores
    deben considerar que la cantidad de datos en el vector podría ser realmente un número grande o
    muy grande, y por lo tanto, no deberían aplicar un método de ordenamiento simple. Tienen al menos
    el Shellsort explicado en clases.
    :param fd:
    :return prom: --> esta funcion es para calcular el promedio solamente
    """
    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    cont = acum = 0

    while m.tell() < tam:
        env = pickle.load(m)
        importe = env.calcular_importe()   # se llama al método de la clase envío para calcular su importe
        acum += importe
        cont += 1

    m.close()

    prom = 0
    if cont > 0:
        prom = acum / cont
    print(f"El promedio de los importes de los envíos del arreglo {prom}")

    return prom


def opcion8(fd, prom):
    """
    :param fd: -> archivo binario a leer
    :param prom: -> promedio a comparar calculado en la anterior funcion para generar el array
    :return v_envios: -> lista con los envios con un importe superior al promedio
    """
    v_envios = []
    m = open(fd, "rb")  # read binary, porque solo nos interesa leer el contenido del archivo
    tam = os.path.getsize(fd)

    while m.tell() < tam:
        env = pickle.load(m)
        importe = env.calcular_importe()  # se llama al método de la clase envío para calcular su importe

        if importe > prom:
            add_in_order(v_envios, env)

    m.close()

    # mostrar el arreglo que generamos en el anterior bucle
    for i in v_envios:
        print(i)

    return v_envios


def add_in_order(v_envios, env):
    izq, der = 0, len(v_envios) - 1
    pos = 0     # realmente no es necesario es solo para que no tire el error de que puede no existir.

    while izq <= der:
        c = (izq + der) // 2
        if v_envios[c].codigo == env.codigo:
            pos = c
            break
        elif v_envios[c].codigo >= env.codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    v_envios[pos:pos] = [env]


def opcion9(v_envios, cp):
    """
    9 - Buscar segun el algoritmo de busqueda que corresponda un codigo postal en el arreglo creado. al final
    debe mostrar los datos del primero que coincida
    :param v_envios: --> arreglo creado en el punto anterior
    :param cp:  --> codigo postal a buscar en un arreglo ordenado por codigo postal
    :return:
    """
    izq, der = 0, len(v_envios) - 1
    pos = -1

    while izq <= der:
        c = (izq + der) // 2
        if v_envios[c].codigo == cp:
            pos = c
            break
        elif v_envios[c].codigo >= cp:
            der = c - 1
        else:
            izq = c + 1

    if pos >= 0:
        print(v_envios[pos])
    else:
        print("No existe un envio con este codigo postal")

