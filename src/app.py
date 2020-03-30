# Flask
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import session
from pymongo import MongoClient
import modulos.mongo as mongo
import modulos.logica as logica
import os
from datetime import date, datetime
import random

# Iniciando FLASK
app = Flask(__name__)
app.secret_key = 'Quedate en tu casa que mira que es facil'

fecha_hoy = datetime.now()

# RUTAS 
@app.route('/', methods=['GET', 'POST'])
def inicio():
    texto = ''
    if request.method == 'POST':
        texto = 'Debe ingresar un email'
        email = request.form.get('nick')
        existe = list(mongo.collection.find({"usuarios":"usuarios", "email":email}))
        if existe != []:
            session['email'] = email
            session['nuevo'] = False
            return redirect(url_for('juego'))
        else:
            mongo.collection.insert_one({"usuarios":"usuarios", "email":email, "fecha": fecha_hoy})
            session['nuevo'] = True
            session['email'] = email
            return redirect(url_for('juego'))
    return render_template('login.html', texto=texto)

@app.route('/juego', methods=['GET', 'POST'])
def juego():
    email = session['email']
    nuevo_usuario = session['nuevo']
    fecha_hoy = datetime.now()
    tiempo_transcurrido = list(mongo.collection.find({"email":email}))
    for i in tiempo_transcurrido:
        fecha_sorteo = i['fecha']
        booleano = logica.calcular30dias(fecha_sorteo)
    if booleano == True or nuevo_usuario == True:
        lista_si_toca = ['true', 'false', 'true', 'true']
        lista = ['1.000€', '3.000€', 'una BMX 2430', '50€', '200€', '600€', 'un Peugeot 206 SX']
        num_random = random.randrange(3)
        num_random2 = random.randrange(6)
        ha_tocado = lista_si_toca[num_random]
        if ha_tocado == 'true':
            texto = (f'¡Genial! Has ganado {lista[num_random2]} y has entrado en el gran sorteo mensual')
            mongo.collection.insert_one({"super_premio": "super_premio", "email":email, "fecha": fecha_sorteo, "mes": fecha_sorteo.month, "premio_mensual" : lista[num_random2] })
        else:
            texto = '¡Vaya! No te ha tocado nada, vuelve a intentarlo el mes que viene'
    else:
        sacar_tiempo = logica.transformarHora(fecha_sorteo)
        texto = (f'No puedes volver a jugar, intentaste el sorteo por última vez {sacar_tiempo}')
    lista_super_sorteo = []
    super_sorteo = list(mongo.collection.find({"super_premio":"super_premio", "mes": fecha_hoy.month}))
    for i in super_sorteo:
        lista_super_sorteo.append([i['email'], i["premio_mensual"]])
    return render_template('index.html', texto=texto, lista_super_sorteo=lista_super_sorteo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run("0.0.0.0", port=port, debug=True)