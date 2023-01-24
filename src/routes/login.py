from flask import Blueprint , render_template  

from flask import  render_template

#entidades 



main=Blueprint('login',__name__)

@main.route('/', )
def login():
    
    return render_template('login.html')