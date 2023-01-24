
from confg import config
from flask import Flask, request, session, redirect, url_for, render_template, flash , blueprints
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash

from database.db import get_Conection

#entidades 



#rutas  de html para la api 
from routes import ruta_uno
from routes import inicio
from routes import login
from routes import register
from routes import subir_foto

from routes import configuracion
from routes import profile
from routes import comunidad



app = Flask(__name__)
#registra un error y lo manda al html 
def no_encontrado(error):
    return render_template('errore.html'),404

app.config.from_object(config['development'])


#asignacion rutas o creacion de rutas 
app.register_blueprint(ruta_uno.main , url_prefix='/ruta_uno')
app.register_blueprint(inicio.main ,url_prefix='/main')
app.register_blueprint(register.main ,url_prefix='/register')




app.register_blueprint(configuracion.main ,url_prefix='/user/config')
app.register_blueprint(profile.main , url_prefix = '/profile')
app.register_blueprint(comunidad.main ,url_prefix = '/comunidad')
app.register_blueprint(subir_foto.main ,url_prefix='/upload/foto')
    

conn = get_Conection()


@app.route('/')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
    
        # User is loggedin show them the home page
        return render_template('home.html', username=session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))
 
@app.route('/login/', methods=['GET', 'POST'])
def login():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
   
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        print(password)
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            password_rs = account['password']
            print(password_rs)
        
            if check_password_hash(password_rs, password):
                session['loggedin'] = True
                session['id'] = account['id']
                session['username'] = account['username']
               
                return redirect(url_for('home'))
            else:
                
                flash('Incorrect username/password')
        else:
            
            flash('Incorrect username/password')
 
    return render_template('login.html')
  
@app.route('/register', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
    
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
    
        _hashed_password = generate_password_hash(password)
 
        #Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
       
        if account:
            flash('Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('Username must contain only characters and numbers!')
        elif not username or not password or not email:
            flash('Please fill out the form!')
        else:
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute("INSERT INTO users (fullname, username, password, email) VALUES (%s,%s,%s,%s)", (fullname, username, _hashed_password, email))
            conn.commit()
            flash('You have successfully registered!')
    elif request.method == 'POST':
       
        flash('Please fill out the form!')
   
    return render_template('register.html')
   
   
@app.route('/logout')
def logout():
    
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
  
   return redirect(url_for('login'))





    
if __name__ == '__main__':
    app.register_error_handler(404 , no_encontrado)
    app.run(debug = True) 
    




