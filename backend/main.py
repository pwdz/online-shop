from flask import Blueprint
from flask.helpers import flash, make_response
from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from backend.dtos.users import RegisterInput, LoginInput
import backend.services.users as users
import backend.services.admins as admins
import backend.services.products as products
import backend.utils.login as loginService
from functools import wraps

main = Blueprint('main', __name__)
register_schema = RegisterInput()
login_schema = LoginInput()


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            valid = users.check_token(
                request.headers["Authorization"].replace('Bearer ', ''))
            if valid:
                return f(*args, **kwargs)
            else:
                flash('You need to login first')
                return redirect(url_for('main.login'))
        else:
            flash('You need to login first')
            return redirect(url_for('main.login'))
    return wrap


def admin_login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if "Authorization" in request.headers:
            valid = admins.check_token(
                request.headers["Authorization"].replace('Bearer ', ''))
            if valid:
                return f(*args, **kwargs)
            else:
                flash('You need to login first')
                return redirect(url_for('main.login'))
        else:
            flash('You need to login first')
            return redirect(url_for('main.login'))
    return wrap


@main.route('/register', methods=['POST'])
def register():
    errors = register_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.register(request.form['email'], request.form['password'],
                             request.form.get('name', None),  request.form.get('lastname', None), request.form.get('address', None))
        print(res)
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.form
        errors = login_schema.validate(data)
        if errors:
            res = make_response(
                jsonify({"success": False, "message": errors}), 400)
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        try:
            res = loginService.login(data['email'], data['password'])
            session['token'] = res['token']
            # session['logged_in'] = True
            res = make_response(jsonify({"success": True, "data": res}), 200)
            res.headers.add("Access-Control-Allow-Origin", "*")

            return res
        except Exception as e:
            print(e)
            res = make_response(
                jsonify({"success": False, "message": e.args}), 400)
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
    res = make_response(
        jsonify({"success": False, "message": "Redirected to login page"}), 400)
    res.headers.add("Access-Control-Allow-Origin", "*")
    return res


@main.route('/edit', methods=['PUT'])
@login_required
def edit():
    try:
        res = users.edit(request.headers["Authorization"].replace('Bearer ', ''), request.form.get('password'),
                         request.form.get('name', None),  request.form.get('lastname', None), request.form.get('address', None))
        print("hey you")
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400

@main.route('/addprod', methods=['POST'])
def addProduct():
    print("shir")
    print(request)
    print(request.data)
    return ":)"
    # try:
        # res = products.edit(request)
