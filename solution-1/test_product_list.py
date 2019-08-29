from product_list import app
import json
import pytest

test_client = app.test_client()

def test_get_all_products():
    rv = test_client.get('/products')
    assert rv.status_code == 200
    assert rv.mimetype == 'application/json' 
    assert len(rv.json) == 1

def test_get_product():
    rv = test_client.get('/products/0')
    assert rv.status_code == 200
    assert rv.mimetype == 'application/json' 

    product = rv.json
    assert product['name'] == 'Product1'
    assert product['price'] == 40
    assert product['quantity'] == 7
   
def test_create_product():
    product = { 'name': 'Coffee', 'price':16.99, 'quantity':2 }  
    rv = test_client.post('/products', data=json.dumps(product))
    assert rv.status_code == 201
    assert rv.mimetype == 'application/json' 

    assert rv.json['name'] == 'Coffee'

def test_create_product():
    product = { 'name': 'Coffee', 'price':16.99, 'quantity':2 }  
    rv = test_client.post('/products', data=json.dumps(product))
    assert rv.status_code == 201
    assert rv.mimetype == 'application/json' 

    assert rv.json['name'] == 'Coffee'

def test_update_product():
    
    product = { 'name': 'Coffee', 'price':10.99, 'quantity':2 } # discount!
    rv = test_client.put('/products/1', data=json.dumps(product))

    # Get the item again
    rv = test_client.get('/products/1' )
    assert rv.json['price'] == 10.99

@pytest.mark.skip("Not implemented")
def test_delete_product():
    rv = test_client.delete('/products/1')
    assert rv.status_code == 200

    # Get the item again
    rv = test_client.get('/products/1' )
    assert rv.status_code == 404

    rv = test_client.get('/products')
    assert len(rv.json) == 1
