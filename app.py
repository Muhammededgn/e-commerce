from flask import Flask, render_template
from werkzeug.utils import quote  # Instead of url_quote

# Initialize the Flask application
app = Flask(__name__)

# Sample product data
products = [
    {'id': 1, 'name': 'Telefon', 'price': 1000},
    {'id': 2, 'name': 'Laptop', 'price': 5000}
]

# Initialize the cart
cart = []

@app.route('/add/<int:product_id>')
def add_to_cart(product_id):
    product = next((p for p in products if p['id'] == product_id), None)


if __name__ == '__main__':
    # Run the application
    app.run(host='0.0.0.0', port=5000)