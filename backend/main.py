from flask import Blueprint
from pymongo import message
from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from .extensions import mongo
from backend.dtos.users import RegisterInput
import backend.services.users as users

main = Blueprint('main', __name__)
register_schema = RegisterInput()


@main.route('/register', methods=['POST'])
def register():
    print(request.form)
    errors = register_schema.validate(request.form)
    print(errors)
    if errors:
        print("holaaa")
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.register(request.form['email'], request.form['password'],
                             request.form.get('name', None),  request.form.get('lastname', None), request.form.get('address', None))

        return jsonify({"success": True, "message": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400
