from flask import Blueprint , render_template  , redirect ,url_for
from flask import session, flash,request
from  database.db import get_Conection
import psycopg2
from random import *
inicio=Blueprint('Inicio',__name__,url_prefix='/')
conn=get_Conection()
@inicio.route('/inicio')
def profile():
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        cursor.execute('SELECT id_foto , imagen FROM foto')
        Fot= cursor.fetchall()
        
     

        items = Fot
        n = len(Fot)
        i=0
        while i <=n:
            i+=1
            x = sample(items,  1)
            fotos = []
            fotos.insert(i,x)
        print(fotos)
        
        
    return render_template('inicio.html', account =account , Fot = Fot)
    
    

