from .entitis.user import User
class modelUser():
    @classmethod
    def login (self , data ,user):
        try:
            cursor=data.connection.cursor()
            sql = """SELECT id,nombre,contasea  FROM usuario" where nombre ='{}'""".format(user.nombre)
            cursor.execute(sql)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user=User(row[0],row[1],User.check_pas(row[2],user.password))
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)