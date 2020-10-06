from flask import Flask, jsonify, request

app = Flask(__name__)

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

@app.route('/usoram_cpu', methods=['GET'])
def ObtenerRamyCpu():
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

    fs = open('/elements/procs/cpu-module','r')
    info = fs.read()
    fs.close()  # CIERRO CONEXION

    valores = info.split(',')
    usage = int(valores[0])
    total = int(valores[1])
    
    porcentaje = ( usage/total ) *100

    return jsonify( {'ram': total, 'cpu': porcentaje} )

# PARA CORRER EL ARCHIVO EN LA CONSOLA ES python app.py
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)