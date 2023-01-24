

from app import c_app


#entidades 

app = c_app()
#registra un error y lo manda al html 
    
if __name__ == '__main__':
    
    app.run(debug = True) 