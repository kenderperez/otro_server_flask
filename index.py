import os
from flask import Flask, request, render_template, send_from_directory
from flask import jsonify



app = Flask(__name__)


#ruta principal
@app.route('/')
def index():
    return render_template('index.html', data = 'hola')

@app.route('/subir_archivos', methods=['POST'])
def upload():
    if request.method == "POST":
        f = request.files['archivo']
        filename = f.filename
        nom = request.form['sd']
        print(nom)
        ruta = f'/videos/{filename}'
        f.save(os.path.join('./archivos', filename))
        
        data = open('datos.txt', 'a')
        data.write('\n' + ruta)
        data.close()
        return "Archivo subido"
"""
    Estas dos rutas son para servir el CSS y los iconos
"""
@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)

@app.route('/videos/<path:path>')
def send_webfont(path):
    return send_from_directory('videos', path)

@app.route('/get_content')
def contenido():
    data = open('datos.txt', 'r')
    cont = data.readlines()
    lista = []
    for linea in cont:
        
        newlinea = linea.rstrip('\n')
        lista.append(newlinea)
        print(linea)

    data.close()
   
    return jsonify({'mensaje': lista})

if __name__ == '__main__':
    app.run(debug=True, port=3000)