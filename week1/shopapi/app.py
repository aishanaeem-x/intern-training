# app.py
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity 
from flask_bcrypt import Bcrypt
import json
import os

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(BASE_DIR, "products.json")
USER_FILE= os.path.join(BASE_DIR, "users.json")

app.config["JWT_SECRET_KEY"]= "dev-secret-change-in-prod"
jwt= JWTManager(app)
bcrypt=Bcrypt(app)

def load_products():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

def save_products(products):
    with open(DATA_FILE, "w") as f:
        json.dump(products, f, indent=4)

def load_users():
    if os.path.exists(USER_FILE):
        with open(USER_FILE, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f, indent=4)

def find_user(username):
    users=load_users()
    return next((u for u in users if u["username"]==username),None)

@app.route("/products", methods=["GET"])
def get_products():
    products = load_products()
    return jsonify(products), 200

@app.route("/products", methods=["POST"])
def add_product():
    products = load_products()
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "name and price are required"}), 400
    new_product = {
        "id": len(products) + 1,
        "name": data["name"],
        "price": data["price"],
        "stock": data.get("stock", 0)
    }
    products.append(new_product)
    save_products(products)
    return jsonify(new_product), 201

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    products = load_products()
    product = next((p for p in products if p["id"] == id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    products = [p for p in products if p["id"] != id]
    save_products(products)
    return jsonify({"message": "Deleted successfully"}), 200

@app.route("/register", methods=["POST"])
def register():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")

    if not username or not password:
        return jsonify({"error":"username and password required"}),400
    
    users=load_users()

    if find_user(username):
        return jsonify({"error":"username already exists"}),409
    hashed = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user={
        "id":len(users)+1,
        "username":username,
        "password": hashed
    }

    users.append(new_user)
    save_users(users)

    return jsonify({"message":"user registered"}),201

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password required"}), 400

    users = load_users()
    user = find_user(username)

    if not user or not bcrypt.check_password_hash(user["password"], password):
        return jsonify({"error": "invalid credentials"}), 401

    token = create_access_token(identity=str(user["id"]))
    return jsonify({"access_token": token}), 200

@app.route("/protected")
@jwt_required()
def protected():
    user_id = get_jwt_identity()
    return jsonify({ "message": f"hello user {user_id}" }), 200

if __name__ == "__main__":
    app.run(debug=True)