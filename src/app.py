from flask import Flask , Blueprint ,render_template ,redirect ,url_for ,request , flash
from confg import config
from models.modelUser import modelUser

from database.db import get_Conection

#entidades 
from models.entitis.user import User


#rutas  de html para la api 
from routes import ruta_uno
from routes import inicio

from routes import register
from routes import subir_foto

from routes import configuracion
from routes import profile
from routes import comunidad



app = Flask(__name__)
#registra un error y lo manda al html 
def no_encontrado(error):
    return render_template('errore.html'),404

app.config.from_object(config['development'])


#asignacion rutas o creacion de rutas 
app.register_blueprint(ruta_uno.main , url_prefix='/ruta_uno')
app.register_blueprint(inicio.main ,url_prefix='/main')
app.register_blueprint(register.main ,url_prefix='/register')


app.register_blueprint(configuracion.main ,url_prefix='/user/config')
app.register_blueprint(profile.main , url_prefix = '/profile')
app.register_blueprint(comunidad.main ,url_prefix = '/comunidad')
app.register_blueprint(subir_foto.main ,url_prefix='/upload/foto')
    

main=Blueprint('login',__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))
@app.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        conn = get_Conection() 
        user = User(0,request.form['nombre'],request.form['password'])
        logged =modelUser.login(conn,user) 
        if logged != None:
            if logged.password:
                return redirect(url_for('main'))
        else:
        
         return render_template('login.html')
    else:
       return render_template('login.html')

    
if __name__ == '__main__':
    app.register_error_handler(404 , no_encontrado)
    app.run(debug = True) 