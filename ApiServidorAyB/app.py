from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
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

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)