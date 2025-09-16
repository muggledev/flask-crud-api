from flask import Flask, request, jsonify

app = Flask(__name__)


product_records = [
    {
        "product_id": "1",
        "product_name": "Hasbro Gaming Clue Game",
        "description": "One murder... 6 suspects...",
        "price": 9.95,
        "active" : True
    },
    {
        "product_id": "2",
        "product_name": "Monopoly Board Game The Classic Edition, 2-8 players",
        "description" : "Relive the Monopoly experiences...", 
        "price": 35.50,
        "active": False
    }
]


@app.route('/product', methods=["POST"])
def create_product():
    new_product = request.get_json()
    product_records.append(new_product)
    return jsonify({"message": "Product created", "product": new_product}), 201


@app.route('/products', methods=["GET"])
def get_all_products():
    return jsonify(product_records), 200


@app.route('/products/active', methods=['GET'])
def get_active_products():
    active_products = [p for p in product_records if isinstance(p, dict) and p.get("active") == True]
    return jsonify(active_products), 200


@app.route('/product/<product_id>', methods=["GET"])
def get_product(product_id):
    for product in product_records:
        if product["product_id"] == product_id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404
    

@app.route('/product/<product_id>', methods=["PUT"])
def update_product(product_id):
    data = request.get_json()
    for product in product_records:
        if product["product_id"] == product_id:
            product.update(data)
            return jsonify({"message": "Product updated", "product": product}), 200
    return jsonify({"error": "Prodcut not found"}), 404
    

@app.route('/product/delete/<product_id>', methods=["DELETE"])
def delete_product(product_id):
    for product in product_records:
        if product["product_id"] == product_id:
            product_records.remove(product)
            return jsonify({"message": "Product deleted"}), 200
    return jsonify({"error": "Product not found"}), 404



if __name__ == '__main__':
    app.run(port='8086', host='0.0.0.0')