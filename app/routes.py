from flask import request, jsonify
from .app import app
from .modules import db
from .models import User, Delivery

@app.route("/api")
def index():
    return jsonify({"message": "API funcionando!"})

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role'],
        created_at=data.get('created_at')
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuário criado com sucesso!"}), 201

@app.route("/api/deliveries", methods=["GET"])
def get_deliveries():
    deliveries = Delivery.query.all()
    return jsonify([{"id": d.id, "product_name": d.product_name} for d in deliveries])
