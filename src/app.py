from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
import os
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_Conection

from app import c_app

#llamado de extencion
conn = get_Conection()
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = c_app()
UPLOAD_FOLDER = 'C:\\Users\\ASUS\\Documents\\Foutus\\src\\app\\static\\img\\todos'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/login/', methods=['GET', 'POST'])
def login():
    

    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if 'loggedin' in session:
        return redirect(url_for('Inicio.profile'))
    # Check if "username" and "password" POST requests exist (user submitted form)
    elif request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
      
 
        # Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        # Fetch one record and return result
        account = cursor.fetchone()
 
        if account:
            password_rs = account['comtrasea']
            print(password_rs)
            # If account exists in users table in out database
            if check_password_hash(password_rs, password):
                # Create session data, we can access this data in other routes
                session['loggedin'] = True
                session['id'] = account['id_user']
                session['username'] = account['username']
                # Redirect to home page
                return redirect(url_for('Inicio.profile'))
            else:
                # Account doesnt exist or username/password incorrect
                flash('Incorrect username/password')
        else:
            # Account doesnt exist or username/password incorrect
            flash('Incorrect username/password')
    
 
    return render_template('login.html')
  
@app.route('/register/', methods=['GET', 'POST'])
def register():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
 
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'imagen' in request.files :
        # Create variables for easy access
        fullname = request.form['fullname']
        username = request.form['username']
        password = request.form['password']
        descripcion = request.form['descripcion']
        file = request.files['imagen']

        _hashed_password = generate_password_hash(password)
 
        #Check if account exists using MySQL
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        print(account)
        # If account exists show error and validation checks
        if account:
            flash('la cuenta ya existe!')
        elif not re.match(r'[^@]+@[^@]+.[^@]+', username):
            flash('e-mail invalido')

        elif not username or not password or not fullname  or not file:
            flash('por favor  llene todos los campos ')
        else:
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            # Account doesnt exists and the form data is valid, now insert new account into users table
            cursor.execute("INSERT INTO users (fullname, username, imagen, descripcion, comtrasea) VALUES (%s,%s,%s,%s,%s)", (fullname, username, filename, descripcion, _hashed_password))
            conn.commit()
            return redirect(url_for('login'))
           
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        flash('Please fill out the form!')
    # Show registration form with message (if any)
    return render_template('register.html')
   
@app.route('/logout')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('profile'))
  


#registra un error y lo manda al html 
#subir foto





@app.route('/subirimagen', methods=['GET','POST'])
def imagen():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        
      
    if request.method == 'POST': 
        titulo = request.form['titulo']
        descripcion= request.form['descripcion']
        file = request.files['file']
        id =  session['id']
        id_categoria = request.form.get('categoriaa')
        if file.filename == '':
            flash('No image selected for uploading')
            
        
        else :
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           
            cursor.execute('INSERT INTO foto (titulo, descripcion, imagen, id_user , id_categoria) VALUES (%s,%s,%s,%s,%s)', (titulo,descripcion ,filename , id , id_categoria ))
            conn.commit()
            print('enviado' , id_categoria)
            return redirect(url_for('Inicio.profile')) 
      

    
    

    return render_template('subir_imagen.html', account =account )


def no_encontrado(error):
    return render_template('errore.html'),404

if __name__ == '__main__':
    app.register_error_handler(404 , no_encontrado)
    app.run(debug = True) 
    




    
    app.run(debug = True) 
    
    
    
