from flask import Blueprint , render_template ,request , redirect , url_for , flash , current_app
from flask import session
from  database.db import get_Conection
import psycopg2
import urllib.request
import os
from werkzeug.utils import secure_filename

subirimagenes=Blueprint('subirimagen',__name__,url_prefix='/')
conn=get_Conection()


ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@subirimagenes.route('/subirimagen', methods=['GET'])
def imagen():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        
    
    
    

        
    return render_template('subir_imagen.html', account =account )

@subirimagenes.route('/subirimagen', methods=['POST'])
def subir(): 
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
        titulo = request.form['titulo']
        descripcion= request.form['descripcion']
        file = request.files['file']
        
        if file.filename == '':
            flash('No image selected for uploading')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))
               
            cursor.execute('INSERT INTO foto (titulo,descripcion,id_user,imagen) VALUES(%s,%s,%s,%s)',(titulo,descripcion,session['id'],filename))
            print('enviado')
            return redirect(url_for('Inicio.profile')) 
               

