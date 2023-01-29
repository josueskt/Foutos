from flask import Flask , render_template

from blue_p.usuario.register import usu
from blue_p.usuario.profile import perfil
from blue_p.inicio.Inicio import inicio
from blue_p.fotos.subir_foto import fotos
from blue_p.fotos.subir_imagen import subirimagenes

def c_app():
    app = Flask(__name__, template_folder='../Templates')
    app.secret_key = "super secret key"
    app.register_blueprint(usu)
    app.register_blueprint(perfil)
    app.register_blueprint(inicio)
    app.register_blueprint(fotos)
    app.register_blueprint(subirimagenes)

    
    return app