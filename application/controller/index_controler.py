from application import app
from flask import render_template, request
import json
from application.model.entity.product import Produto

@app.route("/")
def index ():
    with open('application\\view\\static\\products.json') as product_file:
        products_list = json.load(product_file)

    list_of_products = []
    for product in products_list:
        list_of_products.append(Produto(product['id'], product['name'], product['image'],product['oldPrice'],product['price'],product['description'],product['installments']['count'],product['installments']['value']))
    
    return render_template("index.html", list_of_products = list_of_products)