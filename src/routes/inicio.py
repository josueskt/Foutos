from flask import Blueprint , render_template 



from database.db import get_Conection







main=Blueprint('init',__name__)

@main.route('/')


def inicio():
      
        return render_template('inicio.html') 
    
    

