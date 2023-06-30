#### I will write this readme file in english instead of greek!

Explanation:
This is a RESTful API built in Python and it's using the Flask framework since it's ideal for lightweight APIs
It manages orders and products.

After running the server, you can now use POSTMAN to interact with the API
In the postman URL you should see this `Running on http://127.0.0.1:5000` and from here on you modify it in the ways below

How to Run(Examples):
----To manage PRODUCTS----
GET /products - Retrieve all products.
POST /products - Add a new product.
GET /products/{product_id} - Retrieve a specific product.
PUT /products/{product_id} - Update a product.
DELETE /products/{product_id} - Delete a product.

`For Example`

To get all products: GET http://localhost:5000/products
To add a new product: POST http://localhost:5000/products
and in the `Request Body: {"name": "New Product", "description": "New Description", "price": 9.99}`

Get a specific product: GET http://localhost:5000/products/1 *where 1 indicates the ID of the product*

To update a product: PUT http://localhost:5000/products/1
and in the Request body: {"price": 11.99}

Delete a product: DELETE http://localhost:5000/products/1

----To manage ORDERS----
To manage orders, use the following endpoints:
GET /orders - Retrieve all orders.
POST /orders - Place a new order.
GET /orders/{order_id} - Retrieve a specific order.
PUT /orders/{order_id} - Update an order.

`For Example`
Get all orders: GET http://localhost:5000/orders

To place a new order: POST http://localhost:5000/orders and in the
`Request body: {"customer_name": "John Doe", "address": "123 Street", "total_amount": 50.0}`
Get a specific order: GET http://localhost:5000/orders/1

Update an order's status: PUT http://localhost:5000/orders/1 and in the
`Request body: {"status": "shipped"}`

How to run the test_api.py:
Write this in terminal 😼
python -m unittest test_api.py
