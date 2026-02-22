import os
from datetime import datetime, timedelta
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_bcrypt import Bcrypt
from models import db, User, DailyLog, TrainingPlan, Exercise, FoodItem

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'habits.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# --- Helpers ---
def get_or_create_log(user_id, date=None):
    if date is None:
        date = datetime.utcnow().date()
    log = DailyLog.query.filter_by(user_id=user_id, date=date).first()
    if not log:
        log = DailyLog(user_id=user_id, date=date)
        db.session.add(log)
        db.session.commit()
    return log

def calculate_streak(user_id):
    logs = DailyLog.query.filter_by(user_id=user_id).order_by(DailyLog.date.desc()).all()
    if not logs: return 0
    streak = 0
    current_date = datetime.utcnow().date()
    if logs[0].date < current_date - timedelta(days=1): return 0
    expected_date = logs[0].date
    for log in logs:
        if log.date == expected_date:
            streak += 1
            expected_date -= timedelta(days=1)
        else: break
    return streak

# --- Rotas ---
@app.route('/')
@login_required
def index():
    return redirect(url_for('dashboard'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('dashboard'))
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Login inválido.', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# --- ABA: DASHBOARD ---
@app.route('/dashboard')
@login_required
def dashboard():
    filter_days = int(request.args.get('days', 7))
    today = datetime.utcnow().date()
    start_date = today - timedelta(days=filter_days-1)
    logs = DailyLog.query.filter(DailyLog.user_id == current_user.id, DailyLog.date >= start_date).order_by(DailyLog.date.asc()).all()
    
    dates = [log.date.strftime('%d/%m') for log in logs]
    calories = [log.calories_consumed for log in logs]
    water = [log.water_liters for log in logs]
    weight = [log.weight for log in logs]
    sleep = [log.sleep_hours for log in logs]
    reading = [log.reading_pages for log in logs]
    workout = [log.workout_minutes for log in logs]
    
    # Macros totais do período
    total_protein = sum(log.protein_consumed for log in logs)
    total_carbs = sum(log.carbs_consumed for log in logs)
    total_fats = sum(log.fats_consumed for log in logs)
    
    # Insights
    insights = []
    if len(sleep) >= 2:
        avg_sleep_recent = sum(sleep[-3:]) / min(3, len(sleep))
        avg_sleep_past = sum(sleep[:-3]) / max(1, len(sleep)-3)
        if avg_sleep_recent > avg_sleep_past and avg_sleep_past > 0:
            insights.append(f"A tua média de sono subiu recentemente para {avg_sleep_recent:.1f}h!")
        elif avg_sleep_recent < avg_sleep_past:
            insights.append(f"Atenção: A tua média de sono desceu para {avg_sleep_recent:.1f}h.")
            
    if len(water) >= 3 and all(w >= current_user.goal_water for w in water[-3:]):
        insights.append(f"Excelente! Bebeste {current_user.goal_water}L+ de água consistentemente nos últimos 3 dias.")
        
    if len(calories) > 0:
        avg_cals = sum(calories) / len(calories)
        if avg_cals <= current_user.goal_calories:
            insights.append("Estás dentro da tua meta calórica média!")
        else:
            insights.append("A tua média calórica está acima da meta.")
    
    streak = calculate_streak(current_user.id)
    return render_template('dashboard.html', streak=streak, dates=dates, calories=calories, water=water, weight=weight, sleep=sleep, 
                           reading=reading, workout=workout,
                           total_protein=total_protein, total_carbs=total_carbs, total_fats=total_fats, 
                           filter_days=filter_days, insights=insights)

# --- ABA: ALIMENTAÇÃO ---
@app.route('/alimentacao', methods=['GET', 'POST'])
@login_required
def alimentacao():
    filter_days = int(request.args.get('days', 7))
    today = datetime.utcnow().date()
    start_date = today - timedelta(days=filter_days-1)
    logs = DailyLog.query.filter(DailyLog.user_id == current_user.id, DailyLog.date >= start_date).order_by(DailyLog.date.asc()).all()
    
    food_items = FoodItem.query.all()
    log_today = get_or_create_log(current_user.id)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'add_water':
            amount = float(request.form.get('amount', 0))
            unit = request.form.get('unit') # 'liters' or 'cups'
            if unit == 'cups': amount *= 0.25 # 1 copo = 250ml
            log_today.water_liters += amount
            db.session.commit()
            flash(f'Adicionado {amount}L de água', 'success')
        return redirect(url_for('alimentacao'))

    return render_template('alimentacao.html', logs=logs, food_items=food_items, log_today=log_today, filter_days=filter_days)

@app.route('/adicionar_alimento', methods=['GET', 'POST'])
@login_required
def adicionar_alimento():
    category_filter = request.args.get('category')
    if category_filter:
        food_items = FoodItem.query.filter_by(category=category_filter).all()
    else:
        food_items = FoodItem.query.all()
        
    categories = db.session.query(FoodItem.category).distinct().all()
    categories = [c[0] for c in categories if c[0]]
    
    log_today = get_or_create_log(current_user.id)

    if request.method == 'POST':
        food_id = request.form.get('food_id')
        grams = float(request.form.get('grams', 0))
        food = FoodItem.query.get(food_id)
        if food:
            cals = int((food.calories_per_100g / 100) * grams)
            prot = (food.protein_per_100g / 100) * grams
            carbs = (food.carbs_per_100g / 100) * grams
            fats = (food.fats_per_100g / 100) * grams
            
            log_today.calories_consumed += cals
            log_today.protein_consumed += prot
            log_today.carbs_consumed += carbs
            log_today.fats_consumed += fats
            
            db.session.commit()
            flash(f'Adicionado {grams}g de {food.name} ({cals} kcal)', 'success')
            return redirect(url_for('alimentacao'))

    return render_template('adicionar_alimento.html', food_items=food_items, categories=categories, current_category=category_filter)

# --- ABA: TREINO ---
@app.route('/treino', methods=['GET', 'POST'])
@login_required
def treino():
    filter_days = int(request.args.get('days', 7))
    today = datetime.utcnow().date()
    start_date = today - timedelta(days=filter_days-1)
    logs = DailyLog.query.filter(DailyLog.user_id == current_user.id, DailyLog.date >= start_date).order_by(DailyLog.date.asc()).all()
    
    plans = TrainingPlan.query.filter_by(user_id=current_user.id).all()
    log_today = get_or_create_log(current_user.id)

    if request.method == 'POST':
        action = request.form.get('action')
        if action == 'log_workout':
            log_today.workout_minutes += int(request.form.get('minutes', 0))
            log_today.calories_burned += int(request.form.get('calories', 0))
            plan_id = request.form.get('plan_id')
            if plan_id:
                log_today.training_plan_id = int(plan_id)
            db.session.commit()
            flash('Treino registado!', 'success')
        elif action == 'create_plan':
            name = request.form.get('plan_name')
            new_plan = TrainingPlan(name=name, user_id=current_user.id)
            db.session.add(new_plan)
            db.session.commit()
            flash('Plano criado!', 'success')
        elif action == 'add_exercise':
            plan_id = request.form.get('plan_id')
            name = request.form.get('exercise_name')
            sets = int(request.form.get('sets', 3))
            reps = request.form.get('reps', '10')
            weight = float(request.form.get('weight', 0.0))
            
            new_exercise = Exercise(name=name, sets=sets, reps=reps, weight=weight, plan_id=plan_id)
            db.session.add(new_exercise)
            db.session.commit()
            flash('Exercício adicionado!', 'success')
        elif action == 'delete_plan':
            plan_id = request.form.get('plan_id')
            plan = TrainingPlan.query.get(plan_id)
            if plan and plan.user_id == current_user.id:
                db.session.delete(plan)
                db.session.commit()
                flash('Plano apagado!', 'success')
        elif action == 'delete_exercise':
            exercise_id = request.form.get('exercise_id')
            exercise = Exercise.query.get(exercise_id)
            if exercise and exercise.plan.user_id == current_user.id:
                db.session.delete(exercise)
                db.session.commit()
                flash('Exercício apagado!', 'success')
        return redirect(url_for('treino'))

    return render_template('treino.html', logs=logs, plans=plans, log_today=log_today, filter_days=filter_days)

# --- ABA: VIDA ---
@app.route('/vida', methods=['GET', 'POST'])
@login_required
def vida():
    log_today = get_or_create_log(current_user.id)
    if request.method == 'POST':
        log_today.reading_pages = int(request.form.get('pages', 0))
        log_today.weight = float(request.form.get('weight', 0))
        log_today.sleep_hours = float(request.form.get('sleep_hours', 0))
        db.session.commit()
        flash('Hábitos de vida atualizados!', 'success')
        return redirect(url_for('vida'))
    return render_template('vida.html', log_today=log_today)

# --- ABA: PERFIL (PESSOAL) ---
@app.route('/perfil', methods=['GET', 'POST'])
@login_required
def perfil():
    if request.method == 'POST':
        current_user.goal_calories = int(request.form.get('goal_calories', 2000))
        current_user.goal_water = float(request.form.get('goal_water', 2.0))
        current_user.goal_weight = float(request.form.get('goal_weight', 70.0))
        current_user.goal_workout_time = int(request.form.get('goal_workout_time', 30))
        current_user.goal_sleep_hours = float(request.form.get('goal_sleep_hours', 8.0))
        current_user.goal_reading_pages = int(request.form.get('goal_reading_pages', 20))
        db.session.commit()
        flash('Metas atualizadas!', 'success')
        return redirect(url_for('perfil'))
    return render_template('perfil.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=5000)
