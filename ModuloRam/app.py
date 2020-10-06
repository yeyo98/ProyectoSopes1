from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def ObtenerRam():
    fs = open('/elements/procs/ram-module','r')
    mensaje = fs.read()
    fs.close()
    return mensaje

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)