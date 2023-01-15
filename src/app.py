from flask import Flask
from confg import config



#rutas 
from routes import ruta_uno
from routes import inicio

app = Flask(__name__)
def no_encontrado(error):
    return "<h1>not foud</h1>",404

app.config.from_object(config['development'])


#asignacion rutas
app.register_blueprint(ruta_uno.main , url_prefix='/ruta_uno')
app.register_blueprint(inicio.main ,url_prefix='/main')
    
if __name__ == '__main__':
    app.register_error_handler(404 , no_encontrado)
    app.run(debug = True)