import psycopg2
from  psycopg2 import DatabaseError
from decouple import config
def get_Conection(): 
    try:
        return psycopg2.connect(
            
            host=config('PGSQL'),
            user = config('PG_user'),
            password=config('pasword'),
            database=config('database_name')
        )
    except DatabaseError as ex:
        raise ex
    #conecion a la base de datos  se llama a get_connection() para hacer primero importan i luego hacen la conecion con este eneto 