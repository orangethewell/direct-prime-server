from flask import request, jsonify
from .app import app
from .modules import db
from .models import User, Delivery
import datetime

@app.route("/api")
def index():
    return jsonify({"message": "API funcionando!"})

# User code reference
# 100 - User registered with success
# 101 - User already exists
# 102 - User doesn't have deliveries

@app.route("/api/users", methods=["POST"])
def create_user():
    data = request.json
    some_user = User.query.filter(User.email == data['email']).one_or_none()
    if some_user:
        return jsonify({"error": "Já existe um usuário com este email", "code": 101}), 400
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        role=data['role'],
        main_operation_geocode=data["main_operation_geocode"],
        created_at=datetime.datetime.now(datetime.timezone.utc)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Usuário criado com sucesso!", "code": 100}), 201

@app.route("/api/users/<int:user_id>", methods=["GET"])
def get_user_info(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "role": user.role,
        "main_operation_geocode": user.main_operation_geocode
    }), 200

@app.route("/api/users/<int:user_id>/deliveries", methods=["GET"])
def get_user_deliveries(user_id):
    courier_deliveries = Delivery.query.filter(Delivery.courier_user_id == user_id).all()
    if len(courier_deliveries) > 0:
        return jsonify([{"id": d.id, "product_name": d.product_name} for d in courier_deliveries])

    company_deliveries = Delivery.query.filter(Delivery.sending_company_user_id == user_id).all()
    if len(company_deliveries) > 0:
        return jsonify([{"id": d.id, "product_name": d.product_name} for d in company_deliveries])
    
    return jsonify({"error": "Nenhum encomendas encontradas", "code": 102}), 404


@app.route("/api/deliveries", methods=["GET"])
def get_deliveries():
    deliveries = Delivery.query.all()
    return jsonify([{"id": d.id, "product_name": d.product_name} for d in deliveries])
