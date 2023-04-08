from flask import Blueprint , render_template  , redirect ,url_for , session 
import psycopg2
import psycopg2.extras

from database.db import get_Conection
conn = get_Conection()
misfotos=Blueprint('misfotos',__name__,url_prefix='/')
@misfotos.route('/misfotos')
def mios(): 
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        cursor.execute('SELECT id_foto , imagen FROM foto WHERE id_user = %s ',[session['id']] )
        foto = cursor.fetchall()
        # Show the profile page with account info
        return render_template('mis_fotos.html', account=account  , foto=foto)
    # User is not loggedin redirect to login page
   



