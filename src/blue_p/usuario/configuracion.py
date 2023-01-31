from flask import Blueprint , render_template  , redirect ,url_for , session 
import psycopg2
from database.db import get_Conection
conn = get_Conection()


config=Blueprint('config',__name__,url_prefix='/')
@config.route('/profile/configuracion')
def confi(): 
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if 'loggedin' in session:
            cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
    
    
        return render_template('configuracion_usuario.html' ,account = account)
    
    

