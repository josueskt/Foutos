from flask import Blueprint , render_template 

main=Blueprint('register',__name__)

@main.route('/')
def inicio():
    return render_template('register.html')