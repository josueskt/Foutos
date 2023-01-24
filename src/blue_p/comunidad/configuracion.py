from flask import Blueprint , render_template 

main=Blueprint('config',__name__)

@main.route('/')
def inicio():
    return render_template('configuracion_usuario.html')