from flask import Blueprint , render_template ,request , redirect , url_for
from flask import session
from  database.db import get_Conection
import psycopg2
subirimagenes=Blueprint('subirimagen',__name__,url_prefix='/')
conn=get_Conection()

@subirimagenes.route('/subirimagen', methods=['GET', 'POST'])
def imagen():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        
    elif  request.method == 'POST' and 'titulo' in request.form and 'descripcion' in request.form :
          
        titulo = request.form['titulo']
        descripcion= request.form['descripcion']
        
        cursor.execute('INSERT INTO foto (titulo,descripcion,id_user) VALUES(%s,%s,%s,%s)',(titulo,descripcion,session['id']))
        print('enviado')
        return redirect(url_for('Inicio.profile')) 
        
        
        
    return render_template('subir_imagen.html', account =account )