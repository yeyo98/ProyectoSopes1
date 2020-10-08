import random
import nombre

route = ''
address = ''
notas = []

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
            global route
            route = input('\tEscriba la ruta del archivo\n\t')
            AnalyzeFile()
        elif opcion == '2':
            global address
            address = input('\tEscriba la direccion del balanceador\n\t')
        elif opcion == '3':
            ImprimirNotas()
        elif opcion == '4':
            EnviarDatos()
        elif opcion == '5':
            continue
        else:
            print('Error!! Por favor escoja una opcion valida.')
        

def AnalyzeFile():
    try:
        fs = open(route,'r')
        texto = fs.read()
        oraciones = texto.split('.')
        global notas
        notas = []

        for oracion in oraciones:
            numeroRandom = random.randrange(0,49)
            notas.append({'autor': nombre.Aleatorio[numeroRandom], 'nota': oracion})
        print('\t El archivo fue leido y analizado correctamente :D')
    except:
        print('\t *** ERROR!! Escriba una ruta valida para el archivo de entrada ***')

def ImprimirNotas():
    for nota in notas:
        print(nota)

def EnviarDatos():
    return 0
    

# Llamo el metodo main
main()