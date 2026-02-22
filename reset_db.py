import os
from app import app, db
from seeds import seed_foods

def reset_database():
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, 'habits.db')
    
    if os.path.exists(db_path):
        print(f"A remover base de dados antiga em: {db_path}")
        os.remove(db_path)
    
    with app.app_context():
        print("A criar nova base de dados com a estrutura atualizada...")
        db.create_all()
        print("A popular a base de dados com alimentos...")
        seed_foods()
        print("Sucesso! A base de dados foi recriada.")
        print("Agora pode executar 'python create_admin.py <user> <pass>' para criar o seu utilizador.")

if __name__ == "__main__":
    reset_database()
