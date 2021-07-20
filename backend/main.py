from flask import Blueprint
from pymongo import message
from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from backend.dtos.users import RegisterInput, LoginInput
import backend.services.users as users

main = Blueprint('main', __name__)
register_schema = RegisterInput()
login_schema = LoginInput()


@main.route('/register', methods=['POST'])
def register():
    errors = register_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.register(request.form['email'], request.form['password'],
                             request.form.get('name', None),  request.form.get('lastname', None), request.form.get('address', None))

        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/login', methods=['POST'])
def login():
    errors = login_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.login(request.form['email'], request.form['password'])

        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400
