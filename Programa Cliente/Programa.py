route = ''
address = ''

def main():
    opcion = ''
    #opcion = 0
    while opcion != '5' :
        print('\n==================================================')
        print('\t1. Ingresar ruta')
        print('\t2. Ingresar direccion')
        print('\t3. Ver Datos')
        print('\t4. Enviar Datos')
        print('\t5. Salir')
        print('==================================================')
        opcion = input('\tSeleccione una opcion:\n\t')

        if opcion == '1':
            route = input('\tEscriba la ruta del archivo\n\t')
        elif opcion == '2':
            address = input('\tEscriba la direccion del balanceador\n\t')
        elif opcion == '3':
            fs = open('entrada.txt','r')
            print( fs.read() )
        elif opcion == '4':
            print('opcion 4')
        elif opcion == '5':
            continue
        else:
            print('Error!! Por favor escoja una opcion valida.')
        

# Llamo el metodo main
main()