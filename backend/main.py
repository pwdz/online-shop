from flask import Blueprint
from flask.helpers import flash, make_response
from flask import Flask, render_template, url_for, request, session, redirect, jsonify
from backend.dtos.users import RegisterInput, LoginInput, IncreaseBalance, EditInput, BuyInput
from backend.dtos.categories import AddInput, RemoveInput, EditInput
from backend.dtos.receipts import ChangeInput
import backend.services.users as users
import backend.services.admins as admins
import backend.services.products as products
import backend.services.categories as categories
import backend.services.receipts as receipts
import backend.utils.login as loginService
from backend.dtos.products import AddProductInput, EditProductInput, GetProductInput
from functools import wraps

main = Blueprint('main', __name__)
register_schema = RegisterInput()
increase_balance_schema = IncreaseBalance()
user_edit_schema = EditInput()
login_schema = LoginInput()
buy_schema = BuyInput()
category_input_schema = AddInput()
category_remove_schema = RemoveInput()
category_edit_schema = EditInput()
receipt_input_schema = ChangeInput()
product_input_schema = AddProductInput()
productedit_input_schema = EditProductInput()
productfilter_input_schema = GetProductInput()

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

@main.after_request
def add_cors_headers(response):
    whitelist = ['127.0.0.1:5000']
    parts = request.base_url.split("/")
    base_url = parts[2]
    if base_url in whitelist:
        response.headers.add("Access-Control-Allow-Origin", "*")

    return response


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
            # res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        try:
            res = loginService.login(data['email'], data['password'])
            session['token'] = res['token']
            # session['logged_in'] = True
            res = make_response(jsonify({"success": True, "data": res}), 200)
            # res.headers.add("Access-Control-Allow-Origin", "*")

            return res
        except Exception as e:
            print(e)
            res = make_response(
                jsonify({"success": False, "message": e.args}), 400)
            # res.headers.add("Access-Control-Allow-Origin", "*")
            return res
    res = make_response(
        jsonify({"success": False, "message": "Redirected to login page"}), 400)
    # res.headers.add("Access-Control-Allow-Origin", "*")
    return res


@main.route('/users/edit', methods=['PUT'])
@login_required
def edit():
    errors = user_edit_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.edit(request.headers["Authorization"].replace('Bearer ', ''), request.form.get('password'),
                         request.form.get('name', None),  request.form.get('lastname', None), request.form.get('address', None))
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/users/balance', methods=['PUT'])
@login_required
def increase_balance():
    errors = increase_balance_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = users.increase_balance(request.headers["Authorization"].replace(
            'Bearer ', ''), request.form.get('balance'))
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/users/receipts', methods=['GET'])
@login_required
def get_my_receipts():
    try:
        res = receipts.get_list(
            request.headers["Authorization"].replace('Bearer ', ''))
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/categories/list', methods=['GET'])
def get_category_list():
    try:
        res = categories.get_list()
        return jsonify({"success": True, "data": res})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/categories', methods=['POST'])
@admin_login_required
def add_category():
    errors = category_input_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = categories.add_new(request.form.get('catName'))
        return jsonify({"success": True, "data": res})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/categories', methods=['PUT'])
@admin_login_required
def edit_category():
    errors = category_edit_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = categories.edit(request.form.get('catName'),
                              request.form.get('newName'))

        return jsonify({"success": True, "data": res})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/categories', methods=['DELETE'])
@admin_login_required
def remove_category():
    errors = category_remove_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = categories.remove(request.form.get('name'))
        return jsonify({"success": True, "data": res})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/receipts', methods=['PUT'])
@admin_login_required
def change_receipt_sate():
    errors = receipt_input_schema.validate(request.form)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = receipts.change_state(
            request.form.get('id'), request.form.get('state'))
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/products', methods=['POST'])
@admin_login_required
def add_product():
    data = request.form
    errors = product_input_schema.validate(data)
    if errors:
        res = make_response(
            jsonify({"success": False, "message": errors}), 400)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
    try:
        res = products.addNew(data.get('name'),
                              data.get('price'),
                              data.get('count'),
                              soldCount=0,
                              category=data.get('category'),
                              # img = request.form.get('image')
                              )
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/products/list', methods=['GET', 'POST'])
# @add_cors_headers
def get_products_list():
    data = request.form
    errors = productfilter_input_schema.validate(data)
    if errors:
        res = make_response(
            jsonify({"success": False, "message": errors}), 400)
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res
 
    try:
        res = products.get_list(data.get('category'), data.get('price_ascending'), data.get('price_descending'), data.get('date'), data.get('price_range_min'), data.get('price_range_max'))
        return make_response(jsonify({"success": True, "data": res}), 200)
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/users/receipts', methods=['GET'])
@admin_login_required
def get_receipts_list():
    try:
        res = receipts.get_list()
        return jsonify({"success": True, "data": res})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


@main.route('/admins/products', methods=['PUT'])
@admin_login_required
def edit_product():
    data = request.form
    errors = productedit_input_schema.validate(data)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        res = products.edit(data.get('name'),
                            data.get('new_name'),
                            data.get('new_category'),
                            data.get('new_price'),
                            data.get('new_count')
                            )
        return jsonify({"success": True, "data": res})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400

@main.route('/users/buy', methods=['POST'])
@login_required
def buy_products():
    data = request.form
    errors = buy_schema.validate(data)
    if errors:
        return jsonify({"success": False, "message": errors}), 400
    try:
        product_exists, product_price = products.check_storage(data.get('product_name'), data.get('count'))

        cost = product_price * int(data.get('count'))
        has_enough_balance = users.check_balance(request.headers["Authorization"].replace('Bearer ', ''), cost)

        if not product_exists:
            return jsonify({"success": False, "message": "storage doesn't gave enought of this product"})
        elif not has_enough_balance:
            return jsonify({"success": False, "message": "You don't have enough balance. Charge you wallet first."})
        else:
            products.buy_product(data.get('product_name'), data.get('count'))

            users.decrease_balance(request.headers["Authorization"].replace('Bearer ', ''), cost)            


            receipts.add(data.get('product_name'), data.get('count'),request.headers["Authorization"].replace('Bearer ', '') ,cost)

            return jsonify({"success": True, "message": "Items are bought"})

    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": e.args}), 400


