from flask import Blueprint , render_template  , redirect ,url_for
from flask import session, flash,request
from  database.db import get_Conection
import psycopg2
import psycopg2.extras
import os
from werkzeug.utils import secure_filename
from random import *



UPLOAD_FOLDER = 'C:\\Users\\ASUS\\Documents\\Foutus\\src\\app\\static\\img\\todos'






config=Blueprint('congif',__name__,url_prefix='/')
conn=get_Conection()

@config.route('/configuracion')
def configuracion():
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
    return render_template('configuracion_usuario.html', account =account )    
       
@config.route('/configuracion', methods=['POST'])   
    
   
    
def actualizar_usuario (): 
 fullname = request.form['fullname']
    
 description = request.form['descripcion']
 file = request.files['photo']
 filename = secure_filename(file.filename)  
 if description == '' and fullname == '' : 
     flash("Campos vacios ")
  
 elif file.filename == '':
     
     
    
    
    
    
    
    
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('UPDATE users SET fullname = %s ,  descripcion = %s where id_user = %s', (fullname,description,session['id']))
    conn.commit()
    return redirect(url_for('Inicio.profile'))
        
 elif file.filename != '':   
    file.save(os.path.join(UPLOAD_FOLDER, filename))
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cursor.execute('UPDATE users SET fullname = %s ,imagen = %s,  descripcion = %s where id_user = %s', (fullname,filename,description,session['id']))
    conn.commit()
    return redirect(url_for('Inicio.profile'))    
    
    

