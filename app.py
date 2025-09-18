from flask import Flask, request, jsonify

from data import product_records

app = Flask(__name__)



@app.route('/product', methods=["POST"])
def create_product():
    new_product = request.get_json()
    if type(new_product) != dict:
        return jsonify({"error": "please send a valid product using JSON with key-value pairs"}), 400
    product_records.append(new_product)
    return jsonify({"message": "product created successfully!", "product": new_product}), 201


@app.route('/products', methods=["GET"])
def get_all_products():
    if not product_records:
            return jsonify({"message": "no products found", "results": []}), 200
    return jsonify({"message": "products found", "results": product_records}), 200



@app.route('/products/active', methods=['GET'])
def get_active_products():
    active_products = []
    for product in product_records:
        if product.get("active") == True:
            active_products.append(product)
    if not active_products:
        return jsonify({"message": "no active products found", "results": []}), 200
    return jsonify({"message": "products found", "results": active_products}), 200



@app.route('/product/<product_id>', methods=["GET"])
def get_product(product_id):
    for product in product_records:
        if product["product_id"] == product_id:
            return jsonify({"message": "product found", "result": product}), 200
    return jsonify({"error": "product not found"}), 404
    

@app.route('/product/<product_id>', methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    for product in product_records:
        if product["product_id"] == product_id:
            product.update(data)
            return jsonify({"message": "product updated", "product": product}), 200
    return jsonify({"error": "product not found"}), 404
    

@app.route('/product/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    for product in product_records:
        if product["product_id"] == product_id:
            product_records.remove(product)
            return jsonify({"message": "product deleted"}), 200
    return jsonify({"error": "product not found"}), 404



if __name__ == '__main__':
    app.run(port='8086', host='0.0.0.0')