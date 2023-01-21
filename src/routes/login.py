from flask import Blueprint , render_template  ,request,redirect,url_for
from models.modelUser import modelUser

from database.db import get_Conection

#entidades 
from models.entitis.user import User


main=Blueprint('login',__name__)

@main.route('/login' ,methods=['GET','POST'])
def login():
    if request.method == 'POST':
        conn = get_Conection() 
        user = User(0,request.form['correo'],request.form['password'])
        logged =modelUser.login(conn,user) 
        if logged != None:
            if logged.password:
                return redirect(url_for('main'))
        else:
        
         return render_template('login.html')
    else:
       return render_template('login.html')
   