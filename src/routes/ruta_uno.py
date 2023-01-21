from flask import Blueprint , render_template 

main=Blueprint('comunidad',__name__)

@main.route('/')
def inicio():
    return render_template('comunidad.html')