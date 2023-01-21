from werkzeug.security import check_password_hash,generate_password_hash

class User():
    def __init__(self, id_user,nombre,apellido,foto,contasea,id_comunidad) -> None:
        self.id_user = id_user
        self.nombre = nombre
        self.apellido = apellido
        self.foto = foto
        self.contasea = contasea
        self.id_comunidad = id_comunidad
    @classmethod
    def check_pas(self,hashed_password,pasword):
        return self.check_password(hashed_password)
    
    print(generate_password_hash("aasdasd"))