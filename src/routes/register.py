from flask import flash, Blueprint , render_template ,request

main=Blueprint('register',__name__)

@main.route('/')
def inicio():
     return render_template('register.html')