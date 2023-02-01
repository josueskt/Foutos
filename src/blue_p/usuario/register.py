from flask import Flask, request, session, redirect, url_for, render_template, flash
import psycopg2 #pip install psycopg2 
import psycopg2.extras
import re 
from werkzeug.security import generate_password_hash, check_password_hash
from database.db import get_Conection
from flask import flash, Blueprint , render_template ,request,redirect,url_for
from database.db import get_Conection
usu=Blueprint('usuar',__name__,url_prefix='/')

conn = get_Conection()



   
