from flask import Blueprint , jsonify 

main=Blueprint('inicio',__name__)

@main.route('/')
def get_user():
    return jsonify({'mesagge':'asdsdasdasd'})