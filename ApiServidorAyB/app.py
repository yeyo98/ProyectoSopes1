from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from pymongo import MongoClient

import creds

app = Flask(__name__)
CORS(app)

client = None

@app.route('/usoram', methods=['GET'])
def ObtenerRam():
    fs = open('/elements/procs/ram-module','r')
    info = fs.read()
    fs.close()  # CIERRO CONEXION

    valores = info.split(',')
    totalram = int(valores[0])
    free = int(valores[1])
    cached = int(valores[2])
    buffer = int(valores[3])

    total = totalram - ( free + buffer + cached )
    total = ( total/totalram ) *100

    return '<h1>'+ str(total)+'/<h1>'

@app.route('/usocpu', methods=['GET'])
def ObtenerCpu():
    fs = open('/elements/procs/cpu-module','r')
    info = fs.read()
    fs.close()  # CIERRO CONEXION

    valores = info.split(',')
    usage = int(valores[0])
    total = int(valores[1])
    
    porcentaje = ( usage/total ) *100

    return '<h1>'+ str(porcentaje)+'/<h1>'

@app.route('/serverFeature', methods=['GET'])
def ObtenerRamyCpu():
    # CALCULO EL % DE LA RAM
    fs = open('/elements/procs/ram-module','r')
    info = fs.read()
    fs.close()  # CIERRO CONEXION

    valores = info.split(',')
    totalram = int(valores[0])
    free = int(valores[1])
    cached = int(valores[2])
    buffer = int(valores[3])

    total = totalram - ( free + buffer + cached )
    porcentajeRam = ( total/totalram ) *100

    # CALCULO EL % DE LA CPU
    fs = open('/elements/procs/cpu-module','r')
    info = fs.read()
    fs.close()  # CIERRO CONEXION

    valores = info.split(',')
    usage = int(valores[0])
    total = int(valores[1])
    
    porcentaje = ( usage/total ) *100
    
    # OBTENGO EL TAMAÑO DE LA DB
    try:
        Conexion()
        db = client[creds.mongodb['db']]
        coleccion = db['Citas']
        
        cont = coleccion.find({})
        cant = cont.count()
        client.close()
        return jsonify({'estado':200, 'ram': porcentajeRam, 'cpu': porcentaje, 'cantidad': cant})
    except:
        return jsonify( {'estado': 400, 'message': 'Hubo un error para obtener las caracterisiticas'} )

@app.route('/ingresarCita', methods=['POST'])
def ingresarCita():
    content = request.get_json()
    autor = content['autor']
    nota = content['nota']

    try:
        Conexion()
        db = client[creds.mongodb['db']]
        coleccion = db['Citas']
        post = {'autor': autor, 'nota': nota}
        
        coleccion.insert(post)
        client.close()
        return jsonify( {'estado': 200, 'message': 'Se ingreso la cita correctamente'} )
    except:
        return jsonify( {'estado': 400, 'message': 'Hubo un error para ingresar la cita'} )

@app.route('/recuperarCitas', methods=['GET'])
def getCitas():
    #content = request.get_json()
    #autor = content['autor']
    #nota = content['nota']
    try:
        Conexion()
        db = client[creds.mongodb['db']]
        coleccion = db['Citas']
        data = []
        
        for documento in coleccion.find({}):
            data.append( {'autor': documento['autor'], 'nota': documento['nota']} )

        client.close()
        return jsonify({'estado':200, 'arr': data})
    except:
        return jsonify( {'estado': 400, 'message': 'Hubo un error para recuperar las citas'} )

@app.route('/cantidadCitas', methods=['GET'])
def cantidadCitas():
    try:
        Conexion()
        db = client[creds.mongodb['db']]
        coleccion = db['Citas']
        
        cont = coleccion.find({})
        cant = cont.count()
        client.close()
        return jsonify({'estado':200, 'cantidad': cant})
    except:
        return jsonify( {'estado': 400, 'message': 'Hubo un error para obtener la cantidad de cita'} )


def Conexion():
    global client
    client = MongoClient(
        creds.mongodb['host'], 
        username = creds.mongodb['user'], 
        password = creds.mongodb['passwd']
    )

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)