from flask import Flask , render_template

from blue_p.usuario.register import usuario
from blue_p.usuario.profile import perfil
from blue_p.inicio.Inicio import inicio
from blue_p.fotos.subir_foto import foto_gente

def c_app():
    app = Flask(__name__, template_folder='../Templates')
    app.register_blueprint(usuario)
    app.register_blueprint(perfil)
    app.register_blueprint(inicio)
    app.register_blueprint(foto_gente)
    return app