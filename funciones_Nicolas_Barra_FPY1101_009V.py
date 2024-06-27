import os

libros = []
prestamos = []

def registrar():
    try:
        titulo  = input('Ingrese el título del libro: \n')
        autor   = input('Ingrese el autor del libro: \n')
        año     = input('Ingrese el año de publicación del libro: \n')
        sku     = titulo + autor + año
        estado  = 0 #( 0 = sin prestar // 1 = prestado )
        
        libro = {
            'titulo'    :   titulo,
            'autor'     :   autor,
            'año'       :   año,
            'sku'       :   sku,
            'estado'    :   estado
        }
        libros.append(libro)
        print('Libro registrado con éxito.\n')
    except ValueError:
        print('Registro erróneo.')

def prestar():
    try:
        usuario         = input("Ingrese su nombre de usuario: \n")
        compara_sku     = input("Ingrese el SKU del libro: \n")
        titulo_prestamo = libros.__contains__(compara_sku)
        fecha_prestamo  = input("Ingrese la fecha actual: \n")
        
        prestamo = {
            'usuario'        : usuario,
            'titulo'         : titulo_prestamo,
            'fecha_prestamo' : fecha_prestamo
        }

        for libro in libros:

            if  {libro['sku']} == compara_sku and {libro['estado']} != 0:
                print("El libro se encuentra actualmente prestado.")

            else:
                libro['estado'] = 1
                prestamos.append(prestamo)
                print("Se ha prestado el libro con éxito.")

    except ValueError:
        print("No se ha podido completar el proceso.")

def listar():
    print('TÍTULO\t\t\t''AUTOR\t\t\t''AÑO PUBLICACIÓN\t\t\t''SKU\n')
    for libro in libros:
        print(f'{libro['titulo']}\t\t{libro['autor']}\t\t{libro['año']}\t\t\t{libro['sku']}\n')

def imprimir():
    with open('detalles_prestamos.txt', 'w') as archivo:
        archivo.write('USUARIO\t\t\t''TÍTULO\t\t\t''FECHA PRESTAMO\n')
        for prestamo in prestamos:
                archivo.write(f'{prestamos['usuario']}\t\t\t{prestamos['titulo_prestamo']}\t\t\t{prestamos['fecha_prestamo']}\t\t\t')
                print('Archivo creado con éxito.')

def menu():
    while True:
        try:
            print('==============================================')
            print('==================== MENU ====================')
            print('==============================================')
            print('1. Registrar libros | 2. Prestar libros | 3. Listar libros | 4. Imprimir reporte de prestamos | 5. Salir')
            op = int(input('Ingrese una opción: '))

            if op == 1:
                registrar()
            if op == 2:
                prestar()
            if op == 3:
                listar()
            if op == 4:
                imprimir()
            if op == 5:
                print('Programa finalizado...\nDesarrollado por Nicolás Barra\nRUN: 17.675.696-9')
                break
        except ValueError:
            print('El valor ingresado es incorrecto.')



