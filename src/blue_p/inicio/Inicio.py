from flask import Blueprint , render_template  , redirect ,url_for

inicio=Blueprint('Inicio',__name__,url_prefix='/')

@inicio.route('/inicio')
def profile():
    return render_template('inicio.html')
    
    

