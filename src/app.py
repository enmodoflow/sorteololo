# Flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from pymongo import MongoClient
import modulos.mongo as mongo
import os
from datetime import date, datetime

# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'Quedate en tu casa que mira que es facil'

fecha_hoy = datetime.now()

# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    texto = ''
    if request.method == 'POST':
        nick = request.form.get('nick')
        existe = list(mongo.find({"usuarios":"usuarios"}))
        if len(existe) != 0:
            mongo.collection.insert_one({"usuarios":"usuarios", "nick":nick, "fecha": fecha_hoy})
            return redirect(url_for('juego'))
        else:
            texto = 'El nickname ya existe en la base de datos'
    return render_template('login.html')

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    return render_template('index.html')


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)