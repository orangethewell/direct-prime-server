from .modules import db
import enum
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Float, Text, Uuid, ARRAY, Enum

class UserRole(enum.Enum):
    Courier = 0
    Company = 1
    ServiceManager = 2

class DeliveryStatus(enum.Enum):
    Pending = 0
    Assigned = 1
    OnCourse = 2
    Failed = 3
    Completed = 4

class Session(db.Model):
    __tablename__ = 'sessions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    device_id = Column(String(255), nullable=False)
    device_name = Column(String(255), nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    g_uuid = Column(Uuid, unique=True, nullable=True)
    last_logged_in = Column(DateTime, nullable=False)
    last_position_geocode = Column(ARRAY(Float), nullable=False)

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    email = Column(String(255), nullable=False, unique=True)
    cellphone = Column(String(20), nullable=True)
    password = Column(String(255), nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    created_at = Column(DateTime, nullable=False)
    profile_image = Column(String(255), nullable=True)
    main_operation_geocode = Column(ARRAY(Float), nullable=False)
    average_review_score = Column(Float, nullable=True)

    deliveries = db.relationship('Delivery', backref='user', lazy=True)

class Delivery(db.Model):
    __tablename__ = 'deliveries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    courier_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sending_company_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    receiving_company_user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    sender_geocode = Column(ARRAY(Float), nullable=True)
    receiver_geocode = Column(ARRAY(Float), nullable=True)
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
