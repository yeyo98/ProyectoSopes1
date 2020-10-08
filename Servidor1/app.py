from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from requests import get, post

import json
import rutas

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def allDates():
    rutaA = 'http://{}{}'.format(rutas.routes['ipa'],rutas.routes['feature'])
    rutaB = 'http://{}{}'.format(rutas.routes['ipb'],rutas.routes['feature'])

    datosA = get(rutaA) # DATOS DEL SERVIDOR A
    datosB = get(rutaB) # DATOS DEL SERVIDOR B
    return jsonify({'serveA':datosA.json(),'serveB':datosB.json()}) 


@app.route('/BalanceadorNotas', methods=['POST'])
def Balanceador():
    content = request.get_json()
    autor = content['autor']
    nota = content['nota']

    rutaA = 'http://{}{}'.format(rutas.routes['ipa'],rutas.routes['feature'])
    rutaB = 'http://{}{}'.format(rutas.routes['ipb'],rutas.routes['feature'])

    datosA = get(rutaA) # DATOS DEL SERVIDOR A
    datosB = get(rutaB) # DATOS DEL SERVIDOR B
    
    ip = rutas.routes['ipb'] if selectServer( datosA.json() , datosB.json() ) else rutas.routes['ipa']
    url = 'http://{}{}'.format( ip , rutas.routes['newnote'] )
    
    #response = None
    try:
        post( url , data=json.dumps( {'autor': autor, 'nota': nota}) )
        return jsonify( {'estado': 200, 'message': 'Se paso la cita correctamente'} )
    except:
        return jsonify( {'estado': 400, 'message': 'Hubo un error para pasar la cita'} )

# false->serverA true->serverB
def selectServer(serverA, serverB):
    if serverA['estado'] == 400:
        return True
    elif serverB['estado'] == 400:
        return False
    elif serverA['cantidad'] > serverB['cantidad']:
        return True
    elif serverA['cantidad'] < serverB['cantidad']:
        return False
    elif serverA['ram'] < serverB['ram']:
        return False
    elif serverA['ram'] > serverB['ram']:
        return True
    elif serverA['cpu'] < serverB['cpu']:
        return False
    elif serverA['cpu'] > serverB['cpu']:
        return True
    
    return False
    



# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)