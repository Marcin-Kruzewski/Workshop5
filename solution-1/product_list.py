from flask import Flask, escape, request, jsonify, Response

app = Flask(__name__)
products = {0: {'name':'Product1', 'price':40, 'quantity':7}}

def get_new_id():
    return max(products.keys()) + 1

@app.route('/product/',methods = ['GET'])
def get_all_products():
    return jsonify(products)
    
@app.route('/product/',methods = ['POST'])
def add_product():
    request.get_json(force=True)
    _id = get_new_id()
    p = {'name':request.json.get('name'), 'price':request.json.get('price'), 'quantity':request.json.get('quantity')}
    products[_id] = p
    return jsonify(p)

@app.route('/product/<int:_id>',methods=['GET'])
def get_product(_id):
    return jsonify(products[_id])

@app.route('/product/<int:_id>',methods=['PUT'])
def update_product(_id):
    request.get_json(force=True)
    p = {'name':request.json.get('name'), 'price':request.json.get('price'), 'quantity':request.json.get('quantity')}
    products[_id] = p
    return jsonify(products[_id])
        
@app.route('/product/<int:_id>',methods=['DELETE'])
def remove_product(_id):
    del(products[_id])
    return jsonify(success=True)
