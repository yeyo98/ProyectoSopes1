from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from requests import get

import rutas

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])
def prueba():
    rutaA = 'http://{}{}'.format(rutas.routes['ipa'],rutas.routes['feature'])
    rutaB = 'http://{}{}'.format(rutas.routes['ipb'],rutas.routes['feature'])

    datosA = get(rutaA)
    datosB = get(rutaB)
    return jsonify({'serveA':datosA.json(),'serveB':datosB.json()}) 

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)