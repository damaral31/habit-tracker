import sys
from app import app, db, bcrypt
from models import User

def create_admin(username, password):
    with app.app_context():
        # IMPORTANTE: Criar tabelas primeiro para evitar erro "no such column"
        # se a base de dados for nova ou estiver desatualizada.
        db.create_all()
        
        try:
            # Check if user already exists
            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                print(f"Erro: O utilizador '{username}' já existe.")
                return

            # Hash the password and create user
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = User(username=username, password_hash=hashed_password)
            
            db.session.add(new_user)
            db.session.commit()
            print(f"Sucesso: Utilizador '{username}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar utilizador: {e}")
            print("Dica: Se alterou os modelos da base de dados, apague o ficheiro 'habits.db' e tente novamente.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 create_admin.py <username> <password>")
    else:
        create_admin(sys.argv[1], sys.argv[2])
