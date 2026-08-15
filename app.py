from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

# Homepage route with a welcome message
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product Catalog API!"})


# Returns all products, optionally filtered by ?category=
@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return jsonify(filtered)
    return jsonify(products)


# Returns a single product by ID, or 404 if not found
@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    product = next((p for p in products if p["id"] == id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)

if __name__ == "__main__":
    app.run(debug=True)
