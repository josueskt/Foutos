from flask import Flask #FLASK es la


app=Flask(__name__) #Crear un nueva


@app.route('/')#Utilizar un decorador de

def hello():#Crear un función que
 return"Hola mundo, este es mi primer"