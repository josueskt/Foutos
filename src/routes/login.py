from flask import Blueprint , render_template , request 

from flask import  render_template
from database.db import get_Conection
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from flask import Flask, request, session, redirect, url_for, render_template, flash , blueprints
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import  check_password_hash
#entidades 



login=Blueprint('login',__name__)
conn = get_Conection()

@login.route('/', methods=['GET', 'POST'])
def login():
   
 
    return render_template('login.html')