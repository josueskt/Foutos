from flask import flash, Blueprint , render_template ,request,redirect,url_for
from database.db import get_Conection
main=Blueprint('register',__name__)


@main.route('/')
def register():
    
     return render_template('register.html')