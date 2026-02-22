from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    # Metas (Perfil)
    goal_calories = db.Column(db.Integer, default=2000)
    goal_water = db.Column(db.Float, default=2.0)
    goal_weight = db.Column(db.Float, default=70.0)
    goal_workout_time = db.Column(db.Integer, default=30) # minutos por dia
    goal_workout_days = db.Column(db.Integer, default=3) # dias por semana
    goal_sleep_hours = db.Column(db.Float, default=8.0) # horas por noite
    goal_reading_pages = db.Column(db.Integer, default=20) # páginas por dia
    
    logs = db.relationship('DailyLog', backref='user', lazy=True)
    training_plans = db.relationship('TrainingPlan', backref='user', lazy=True)

class DailyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=datetime.utcnow().date)
    
    # Alimentação
    calories_consumed = db.Column(db.Integer, default=0)
    water_liters = db.Column(db.Float, default=0.0)
    
    # Treino
    calories_burned = db.Column(db.Integer, default=0)
    workout_minutes = db.Column(db.Integer, default=0)
    
    # Vida
    reading_pages = db.Column(db.Integer, default=0)
    weight = db.Column(db.Float, default=0.0)
    sleep_hours = db.Column(db.Float, default=0.0)
    
    # Macronutrientes consumidos no dia
    protein_consumed = db.Column(db.Float, default=0.0)
    carbs_consumed = db.Column(db.Float, default=0.0)
    fats_consumed = db.Column(db.Float, default=0.0)
    
    training_plan_id = db.Column(db.Integer, db.ForeignKey('training_plan.id'), nullable=True)
    training_plan = db.relationship('TrainingPlan', backref='logs', lazy=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    __table_args__ = (db.UniqueConstraint('user_id', 'date', name='_user_date_uc'),)

class TrainingPlan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    exercises = db.relationship('Exercise', backref='plan', lazy=True, cascade="all, delete-orphan")

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sets = db.Column(db.Integer, default=3)
    reps = db.Column(db.String(50)) # ex: "15" ou "10-12" ou "30s"
    weight = db.Column(db.Float, default=0.0) # Peso em kg
    image_url = db.Column(db.String(255), nullable=True)
    plan_id = db.Column(db.Integer, db.ForeignKey('training_plan.id'), nullable=False)

class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    calories_per_100g = db.Column(db.Integer, nullable=False)
    protein_per_100g = db.Column(db.Float, default=0.0)
    carbs_per_100g = db.Column(db.Float, default=0.0)
    fats_per_100g = db.Column(db.Float, default=0.0)
    category = db.Column(db.String(50)) # Carnes, Peixes, Hidratos, Legumes, Laticínios, Bebidas
