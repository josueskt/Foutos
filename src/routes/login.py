from flask import Blueprint , render_template 

main=Blueprint('login',__name__)

@main.route('/')
def login():
    return render_template('login.html')