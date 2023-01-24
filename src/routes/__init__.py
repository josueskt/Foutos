from flask import Flask
def create_app():
    app = Flask(__name__)
    from routes import login
    app.register_blueprint(login.login)
    return app