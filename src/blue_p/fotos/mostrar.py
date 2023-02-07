from flask import Blueprint , render_template ,request , redirect , url_for
from flask import session
from  database.db import get_Conection
import psycopg2
mostrar_fotos=Blueprint('mostrar',__name__,url_prefix='/')
conn=get_Conection()
@mostrar_fotos.route('/foto/<id>', methods=['GET','POST'] )
def mostrar(id):
    cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    
    # Check if user is loggedin
    if 'loggedin' in session:
        cursor.execute('SELECT * FROM users WHERE id_user = %s', [session['id']])
        account = cursor.fetchone()
        cursor.execute('SELECT * FROM foto WHERE id_foto = %s ', (id,))
        foto= cursor.fetchone()
        cursor.execute('SELECT id_user FROM foto WHERE id_foto = %s ', (id,))
        fot= cursor.fetchone()
        
        cursor.execute('SELECT * FROM users  WHERE id_user = %s', (fot))
        user_foto = cursor.fetchone()
        
        
        
        cursor.execute('SELECT * FROM comentario WHERE id_foto = %s ', (id,))
        comentarios= cursor.fetchall()
        
        if request.method == 'POST' and comentarios : 
            comentraio = request.form.get('comentario')
            if comentraio != None or comentraio != '' :
                cursor.execute("INSERT INTO comentario (texto ,id_user,id_foto) VALUES (%s,%s,%s)", (comentraio,session['id'],id))
                conn.commit()  
                return redirect(url_for('mostrar.mostrar' , id =id))
                   
        conn.commit()        
       
        
        
        
    return render_template('mostrar_foto.html', account= account, foto =foto , comentarios =comentarios , user_foto =user_foto)