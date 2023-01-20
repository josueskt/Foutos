from flask import Blueprint , render_template 

main=Blueprint('profile',__name__)

@main.route('/')
def profile():
    return render_template('profile.html')





