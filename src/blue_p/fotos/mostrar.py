from flask import Blueprint , render_template ,request , redirect , url_for
from flask import session
from  database.db import get_Conection
import psycopg2
mostrar_fotos=Blueprint('mostrar',__name__,url_prefix='/')
conn=get_Conection()
@mostrar_fotos.route('/foto')
def subirfoto():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s ', [session['id']])
        account = cursor.fetchone()
       
        
        
        
    return render_template('mostrar_foto.html', account =account )