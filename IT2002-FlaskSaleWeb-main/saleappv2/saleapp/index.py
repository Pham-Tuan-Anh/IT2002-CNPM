from flask import render_template, request,redirect

from saleapp import app, dao,login
from flask_login import login_user
from saleapp import admin
app.secret_key = 'hbfsdakuhg34i2hjmgeiufshds,fosijgf'


@app.route("/")
def index():
    categories = dao.load_categories()
    products = dao.load_products(category_id=request.args.get("category_id"),
                                 kw=request.args.get('keyword'))
    return render_template('index.html',
                           categories=categories,
                           products=products)


@app.route('/products/<int:product_id>')
def details(product_id):
    p = dao.get_product_by_id(product_id)
    return render_template('details.html', product=p)

@login.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    app.run(debug=True)
