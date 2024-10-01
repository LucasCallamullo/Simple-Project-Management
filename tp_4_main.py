from tp_4_funciones import *


def menu():
    print()
    print("1 - Generar Archivo.")
    print("2 - Agregar Archivo.")
    print("3 - Mostrar Archivo.")
    print("4 - Buscar en el archivo por Código Postal.")
    print("5 - Buscar en el archivo por Dirección Postal.")
    print("6 - Generar Matriz.")
    print("7 - Mostrar Matriz.")
    print("8 - Generar Arreglo.")
    print("9 - Búsqueda Binaria.")
    print("0 - Salir.")
    op = int(input("Ingresar opcion: "))
    return op


def principal():

    # nombre de nuestro archivo .csv
    csv = "envios-tp4.csv"
    csv = "envios-muestra.csv"

    # crear nuestro nombre del archivo
    fd = "envios.dat"

    # validar ingreso opcion 6
    matriz = None

    # validar ingreso opcion 8
    v_envios = None

    op = -1
    while op != 0:

        op = menu()

        if op == 1:
            opcion1(csv, fd)

        elif op == 2:
            opcion2(fd)

        elif op == 3:
            opcion3(fd)

        elif op == 4:
            cp = input("Ingresar código postal a buscar: ")
            opcion4(fd, cp)

        elif op == 5:
            d = input("Ingresar dirección postal a buscar: ")
            opcion5(fd, d)

        elif op == 6:
            matriz = opcion6(fd)

        elif op == 7:
            if matriz is None:
                print("Primero debe ingresar a la opción 6 para ejecutar esta opción.")
            else:
                opcion7(matriz)

        elif op == 8:
            if os.path.exists(fd):
                prom = opcion8_promedio(fd)
                v_envios = opcion8(fd, prom)

            else:
                print("Primero debe crear el archivo binario en la opción 1 u opción 2.")

        elif op == 9:
            if v_envios is None:
                print("Primero debe ingresar a la opción 8 para ejecutar esta opción.")
            else:
                cp = input("Ingresar código postal a buscar: ")
                opcion9(v_envios, cp)

        elif op == 0:
            print("Gracias por usar el menú.")

        else:
            print("Elija una opción correcta.")


if __name__ == '__main__':
    principal()
