from flask import Blueprint , render_template 

main=Blueprint('init',__name__)

@main.route('/')
def inicio():
    return render_template('inicio.html')
