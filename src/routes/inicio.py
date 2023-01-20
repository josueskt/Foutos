from flask import Blueprint , render_template 




from database.db import get_Conection






from database.db import get_Conection


main=Blueprint('init',__name__)

def traer_imagenes():
    conn = get_Conection()
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM fotos")
        foto = cursor.fetchone()
        conn.commit()
        conn.close()
        return foto
    

@main.route('/')

def inicio():
    
    return render_template('inicio.html')
