from flask import Flask , Blueprint ,render_template
from confg import config
from database.db import get_Conection
from psycopg2 import connect

#rutas 
from routes import ruta_uno
from routes import inicio
from routes import register
from routes import subir_foto
from routes import login
from routes import configuracion
from routes import profile



app = Flask(__name__)



def no_encontrado(error):
    return render_template('errore.html'),404

app.config.from_object(config['development'])


#asignacion rutas
app.register_blueprint(ruta_uno.main , url_prefix='/ruta_uno')
app.register_blueprint(inicio.main ,url_prefix='/main')
app.register_blueprint(register.main ,url_prefix='/register/user')
app.register_blueprint(login.main ,url_prefix='/login/user')
app.register_blueprint(configuracion.main ,url_prefix='/user/config')
app.register_blueprint(profile.main , url_prefix = '/profile')

app.register_blueprint(subir_foto.main ,url_prefix='/upload/foto')
@app.route('/a')
def home():
     con = get_Conection()
     cur = con.cursor()
     result=  cur.execute("SELECT 1 + 1")
     print(result)
     return "hola"
        
if __name__ == '__main__':
    app.register_error_handler(404 , no_encontrado)
    app.run(debug = True)