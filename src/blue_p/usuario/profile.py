from flask import Blueprint , render_template  , redirect ,url_for

perfil=Blueprint('profile',__name__,url_prefix='/')
@perfil.route('/')
def home():
  
    return redirect(url_for('register.login'))

@perfil.route('/perfil')
def profile():
    return render_template('profile.html')





