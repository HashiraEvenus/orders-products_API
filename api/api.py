from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

#Sample data(the water is from fiji(?))
products = [
    {"id": 1, "name": "product1", "description": "Description1", "price": 10.99},
    {"id": 2, "name": "product2", "description": "Description2", "price": 5.89},
    {"id": 3, "name": "product3", "description": "Description3", "price": 8.19},
    {"id": 4, "name": "Water", "description": "From a river💀", "price": 5.50}]

orders = []

urls = [
    ("https://www.example.com/product1", "Product"),
    ("https://www.example.com/product2", "Product"),
    ("https://www.example.com/contact", "Non-Product"),
    ("https://www.example.com/about", "Non-Product"),
]

#Routes for products

@app.route('/products', methods = ['GET'])
def get_products():
    #Returns the json with all the products
    return jsonify(products)

@app.route('/products', methods = ['POST'])
def add_product():
    #Adds a new product
    new_product = {
        "id": len(products) + 1,
        "name": request.json['name'],
        "description": request.json['description'],
        "price": request.json['price']
    }
    products.append(new_product)
    return jsonify(new_product),201


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):

    #Filtered generator expression to yield only products where id matches the product's id
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    #Error message if product not found
    return jsonify({'message':"Product does not exist"}),404


@app.route('/products/<int:product_id>', methods = ['PUT'])
def update_product(product_id):
    product = next((p for p in products if p['id'] == product_id),None)
    if product:
        product['name'] = request.json.get('name', product['name'])
        product['price'] = request.json.get('price', product['price'])
        product['description'] = request.json.get('description', product['description'])
        return jsonify(product)
    return jsonify({"message":"Product could not be updated / not found"}), 404

@app.route('/products/<int:product_id>', methods = ['DELETE'])
def delete_product(product_id):
    product = next((p for p in products if p['id'] == product_id),None)
    if product:
        products.remove(product)
        return jsonify({"message": "Product was deleted"})
    return jsonify({"message": "Product could not be deleted/not found"}),404
    #del(product)


#Routes for orders
@app.route('/orders', methods = ['GET'])
def get_orders():
    return jsonify(orders)

@app.route('/orders', methods = ['POST'])
def place_order():
    new_order = {
        "id": len(orders)+1,
        "customer_name": request.json['customer_name'],
        "address": request.json['address'],
        "total_amount": request.json['total_amount'],
        "status": "received"
    }
    orders.append(new_order)
    return jsonify(new_order), 201
@app.route('/orders/<int:order_id>', methods = ['PUT'])
def update_order(order_id):
    #Updates the order
    order = next((o for o in orders if o['id'] == order_id),None)
    if order:
        return jsonify(order)
    return jsonify({"message": 'Order was not found/updated'}),404

@app.route('/orders/<int:order_id>', methods = ['GET'])
def get_order(order_id):
    #Gets a specific order using the `id`
    order = next((o for o in orders if o['id'] == order_id),None)
    if order:
        return jsonify(order)
    return jsonify({"message": "Order was not found"})


if __name__ == '__main__':
    app.run()

#read readme.txt