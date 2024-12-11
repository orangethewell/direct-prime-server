from .modules import db
import enum
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, Text, Uuid, Enum, JSON
from sqlalchemy.sql import func

class BikeKind(str, enum.Enum): 
    Motorbike = "Motorbike"
    Bike = "Bike"

class UserRole(str, enum.Enum):
    Courier = "Courier"
    Company = "Company"
    ServiceManager = "ServiceManager"

class DeliveryStatus(str, enum.Enum):
    Pending = "Pending"
    Assigned = "Assigned"
    OnCourse = "OnCourse"
    Failed = "Failed"
    Completed = "Completed"

class BikeVehicle(db.Model):
    __tablename__ = "bike_vehicles"
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id =  Column(Integer, ForeignKey('users.id'), nullable=False)
    kind = Column(Enum(BikeKind), nullable=False)
    bike_plate = Column(String(12), nullable=True)
    bike_color = Column(String(255), nullable=False)
    bike_brand = Column(String(255), nullable=False)

class Company(db.Model):
    __tablename__ = "company"
    id = Column(Integer, primary_key=True, autoincrement=True)
    owner_id =  Column(Integer, ForeignKey('users.id'), nullable=False)
    name = Column(String(255), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    cpf = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(DateTime)
    profile_image = Column(String(255), nullable=True)
    main_operation_geocode = Column(JSON, nullable=False)
    average_review_score = Column(Float, nullable=True)

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    courier_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sending_company_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiving_company_user_id = Column(Integer, ForeignKey('users.id'))
    sender_geocode = Column(JSON, nullable=True)
    receiver_geocode = Column(JSON, nullable=True)
    product_name = Column(String(255), nullable=False)
    product_image = Column(Text, nullable=True)
    product_details = Column(Text, nullable=True)
    status = Column(Enum(DeliveryStatus), nullable=False)

class DeliveryMessage(db.Model):
    __tablename__ = 'delivery_messages'
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_id = Column(Integer, ForeignKey('deliveries.id'), nullable=False)
    sender_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    message_content = Column(Text, nullable=False)

class DeliveryReview(db.Model):
    __tablename__ = 'delivery_reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    delivery_id = Column(Integer, ForeignKey('deliveries.id'), nullable=False)
    company_score = Column(Float, nullable=False)
    courier_score = Column(Float, nullable=False)
    company_score_comment = Column(String(255), nullable=True)
    courier_score_comment = Column(String(255), nullable=True)
