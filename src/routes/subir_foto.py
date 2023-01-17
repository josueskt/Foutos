from flask import Blueprint , render_template 

main=Blueprint('foto',__name__)

@main.route('/')
def inicio():
    return render_template('subir_foto.html')