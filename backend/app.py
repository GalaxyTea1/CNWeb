import os

from flask import Flask, jsonify, request

import BusinessObjects as bo
import DataObjects as do

app = Flask(__name__)

db_ip = os.getenv('db_ip') #'10.0.2.15'
ConnectionData = {}
ConnectionData['user'] = 'postgres'
ConnectionData['password'] = 'postgres'
ConnectionData['host'] = str(db_ip)
ConnectionData['port'] = '5432'
ConnectionData['database'] = 'northwind'

@app.route('/')
def hello():    
    return 'this is backend'

@app.route('/test_insert')
def test_insert():
    #ConnectionString = 'database=northwind user=postgres password=postgres host=10.0.2.15 port=5432'
    c2 = do.Customer(ConnectionData)
    c1 = bo.Customer(1, 'DAU xanh', 'Peter', '566 Nui Thanh', 'Danang', '50000', 'Vietnam')
    s1 = c2.insert(c1)
    return s1

@app.route('/test_send_receive', methods=['POST'])
def test_send_receive():
    x = request.json['x']
    y = x + 1
    result = {}
    result['y'] = y
    return jsonify(result), 200


@app.route('/user/get_by_id', methods=['POST'])
def user_get_by_id():
    user_id = request.json['user_id']
    result = {}
    result['user_id'] = 1
    return jsonify(result), 200

@app.route('/user/insert', methods=['POST'])
def user_insert():
    data = request.json
    c1 = bo.Customer(data['CustomerID'], data['CustomerName'], data['ContactName'], data['Address'], data['City'], data['PostalCode'], data['Country'])
    c2 = do.Customer(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/user/all')
def get_all_user():
    result = do.Customer(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/user/get/<int:customer_id>')
def get_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/user/update/<int:customer_id>', methods=['PUT'])
def update_user_by_id(customer_id):
    data = request.json
    c = bo.Customer(CustomerID = customer_id, CustomerName=data['CustomerName'], ContactName=data['ContactName'],Address=data['Address'], City=data['City'], PostalCode=data['PostalCode'], Country=data['Country'])
    result = do.Customer(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/user/delete/<int:customer_id>', methods=['DELETE'])
def delete_user_by_id(customer_id):
    c = bo.Customer(CustomerID=customer_id)
    result = do.Customer(ConnectionData).delete(c)
    return jsonify({'message':result[0]}),result[1]

#Product
@app.route('/product/insert', methods=['POST'])
def product_insert():
    data = request.json
    c1 = bo.Product(data['ProductID'], data['ProductName'], data['SupplierID'], data['CategoryID'], data['Unit'], data['Price'])
    c2 = do.Product(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/product/all')
def get_all_product():
    result = do.Product(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/product/get/<int:product_id>')
def get_product_by_id(product_id):
    c = bo.Product(ProductID=product_id)
    result = do.Product(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/product/update/<int:product_id>', methods=['PUT'])
def update_product_by_id(product_id):
    data = request.json
    c = bo.Product(ProductID = product_id, ProductName=data['ProductName'], SupplierID=data['SupplierID'], CategoryID=data['CategoryID'], Unit=data['Unit'], Price=data['Price'])
    result = do.Product(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/product/delete/<int:product_id>', methods=['DELETE'])
def delete_product_by_id(product_id):
    c = bo.Product(ProductID=product_id)
    result = do.Product(ConnectionData).delete(c)
    return jsonify({'message':result[0]}),result[1]

#Shipper
@app.route('/shipper/insert', methods=['POST'])
def shipper_insert():
    data = request.json
    c1 = bo.Shipper(data['ShipperID'], data['ShipperName'], data['Phone'])
    c2 = do.Shipper(ConnectionData)
    s1 = c2.insert(c1)
    result = {}
    result['message'] = s1
    return jsonify(result), 200

@app.route('/shipper/all')
def get_all_shipper():
    result = do.Shipper(ConnectionData).get_all()
    return jsonify(result), 200

@app.route('/shipper/get/<int:shipper_id>')
def get_shipper_by_id(shipper_id):
    c = bo.Shipper(ShipperID=shipper_id)
    result = do.Shipper(ConnectionData).get_by_id(c)
    if result[1] != 200:
        return jsonify({'message': result[0]}), result[1]
    return jsonify(result[0].to_json()), 200

@app.route('/shipper/update/<int:shipper_id>', methods=['PUT'])
def update_shipper_by_id(shipper_id):
    data = request.json
    c = bo.Shipper(ShipperID = shipper_id, ShipperName=data['ShipperName'], Phone=data['Phone'])
    result = do.Shipper(ConnectionData).update(c)
    return jsonify({'message':result[0]}),result[1]

@app.route('/shipper/delete/<int:shipper_id>', methods=['DELETE'])
def delete_shipper_by_id(shipper_id):
    c = bo.Shipper(ShipperID=shipper_id)
    result = do.Shipper(ConnectionData).delete(c)
    return jsonify({'message':result[0]}),result[1]



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
