from flask import Blueprint , render_template 
from flask import session
from  database.db import get_Conection
import psycopg2
fotos=Blueprint('subirfoto',__name__,url_prefix='/')
conn=get_Conection()
@fotos.route('/subirimagen')
def subirfoto():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s ', [session['id']])
        account = cursor.fetchone()
       
        
        
        
    return render_template('subir_imagen.html', account =account )