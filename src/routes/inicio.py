from flask import Blueprint , render_template 



from database.db import get_Conection







main=Blueprint('init',__name__)
def obtener():
    conn =get_Conection()
    lista = None
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM usuario " )
        lista = cursor.fetchone()
        conn.commit()
        conn.close()
        return lista
@main.route('/')


    



def inicio():
    
    return render_template('inicio.html')

