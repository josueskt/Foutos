import psycopg2
from  psycopg2 import DatabaseError
from decouple import config
def get_Conection(): 
   
    
 
    DB_HOST = "localhost"
    DB_NAME = "foutos"
    DB_USER = "postgres"
    DB_PASS = "1234"
 
    conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
    return conn
        
    #conecion a la base de datos  se llama a get_connection() para hacer primero importan i luego hacen la conecion con este eneto 