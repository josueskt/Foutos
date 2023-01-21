from flask import Blueprint , render_template 

main=Blueprint('comuni',__name__)

@main.route('/')
def comunidad():
    return render_template('Comunidad.html')