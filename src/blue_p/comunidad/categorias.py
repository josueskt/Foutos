from flask import Blueprint , render_template  , redirect ,url_for
from flask import session, flash,request
from  database.db import get_Conection
import psycopg2
from random import *
import psycopg2.extras
categoria=Blueprint('categorias',__name__,url_prefix='/')
conn=get_Conection()

@categoria.route('/categoria/<id>')
def categori(id):
     
        cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        cursor.execute('SELECT * FROM foto where id_categoria = %s', (id,))
        Fot= cursor.fetchall()
        cursor.execute('SELECT nombre FROM categoria where id_categoria = %s', (id,))
        cat= cursor.fetchone()
        
     

    
       
        
        
        return render_template('categoria.html', account =account , Fot = Fot, cat = cat)
    
    

