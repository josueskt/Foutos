from flask import Blueprint , render_template 

foto_gente=Blueprint('foto',__name__)

@foto_gente.route('/subir_foto')
def inicio():
    return render_template('subir_imagen.html')
