from app import app, db
from models import FoodItem

def seed_foods():
    with app.app_context():
        if not FoodItem.query.first():
            foods = [
                # -- CARNES --
                FoodItem(name='Vaca (Bife)', calories_per_100g=250, protein_per_100g=26, carbs_per_100g=0, fats_per_100g=15, category='Carnes'),
                FoodItem(name='Vaca (Carne Moída)', calories_per_100g=332, protein_per_100g=14, carbs_per_100g=0, fats_per_100g=30, category='Carnes'),
                FoodItem(name='Vaca (Lombo)', calories_per_100g=143, protein_per_100g=26, carbs_per_100g=0, fats_per_100g=4, category='Carnes'),
                FoodItem(name='Porco (Entrecosto)', calories_per_100g=277, protein_per_100g=14, carbs_per_100g=0, fats_per_100g=24, category='Carnes'),
                FoodItem(name='Porco (Lombo)', calories_per_100g=143, protein_per_100g=26, carbs_per_100g=0, fats_per_100g=3.5, category='Carnes'),
                FoodItem(name='Porco (Febras)', calories_per_100g=156, protein_per_100g=22, carbs_per_100g=0, fats_per_100g=7, category='Carnes'),
                FoodItem(name='Frango (Peito)', calories_per_100g=165, protein_per_100g=31, carbs_per_100g=0, fats_per_100g=3.6, category='Carnes'),
                FoodItem(name='Frango (Coxas)', calories_per_100g=209, protein_per_100g=26, carbs_per_100g=0, fats_per_100g=11, category='Carnes'),
                FoodItem(name='Frango (Asas)', calories_per_100g=203, protein_per_100g=30, carbs_per_100g=0, fats_per_100g=8, category='Carnes'),
                FoodItem(name='Peru (Peito)', calories_per_100g=104, protein_per_100g=24, carbs_per_100g=0, fats_per_100g=1, category='Carnes'),
                FoodItem(name='Pato', calories_per_100g=337, protein_per_100g=19, carbs_per_100g=0, fats_per_100g=28, category='Carnes'),
                FoodItem(name='Coelho', calories_per_100g=136, protein_per_100g=20, carbs_per_100g=0, fats_per_100g=5.5, category='Carnes'),
                FoodItem(name='Borrego / Cordeiro', calories_per_100g=294, protein_per_100g=25, carbs_per_100g=0, fats_per_100g=21, category='Carnes'),
                FoodItem(name='Codorniz', calories_per_100g=134, protein_per_100g=22, carbs_per_100g=0, fats_per_100g=4.5, category='Carnes'),

                # -- PEIXES E MARISCO --
                FoodItem(name='Bacalhau', calories_per_100g=82, protein_per_100g=18, carbs_per_100g=0, fats_per_100g=0.7, category='Peixes e Marisco'),
                FoodItem(name='Salmão', calories_per_100g=208, protein_per_100g=20, carbs_per_100g=0, fats_per_100g=13, category='Peixes e Marisco'),
                FoodItem(name='Atum (Fresco)', calories_per_100g=130, protein_per_100g=28, carbs_per_100g=0, fats_per_100g=0.6, category='Peixes e Marisco'),
                FoodItem(name='Atum (Lata em Água)', calories_per_100g=116, protein_per_100g=26, carbs_per_100g=0, fats_per_100g=1, category='Peixes e Marisco'),
                FoodItem(name='Dourada', calories_per_100g=90, protein_per_100g=19, carbs_per_100g=0, fats_per_100g=1.2, category='Peixes e Marisco'),
                FoodItem(name='Robalo', calories_per_100g=97, protein_per_100g=18, carbs_per_100g=0, fats_per_100g=2, category='Peixes e Marisco'),
                FoodItem(name='Pescada', calories_per_100g=78, protein_per_100g=17, carbs_per_100g=0, fats_per_100g=0.9, category='Peixes e Marisco'),
                FoodItem(name='Sardinha', calories_per_100g=208, protein_per_100g=25, carbs_per_100g=0, fats_per_100g=11, category='Peixes e Marisco'),
                FoodItem(name='Carapau', calories_per_100g=115, protein_per_100g=16, carbs_per_100g=0, fats_per_100g=5, category='Peixes e Marisco'),
                FoodItem(name='Espadarte', calories_per_100g=121, protein_per_100g=20, carbs_per_100g=0, fats_per_100g=4, category='Peixes e Marisco'),
                FoodItem(name='Polvo', calories_per_100g=82, protein_per_100g=15, carbs_per_100g=2.2, fats_per_100g=1, category='Peixes e Marisco'),
                FoodItem(name='Lulas', calories_per_100g=92, protein_per_100g=16, carbs_per_100g=3, fats_per_100g=1.4, category='Peixes e Marisco'),
                FoodItem(name='Choco', calories_per_100g=79, protein_per_100g=16, carbs_per_100g=0.8, fats_per_100g=0.7, category='Peixes e Marisco'),
                FoodItem(name='Camarão', calories_per_100g=99, protein_per_100g=24, carbs_per_100g=0.2, fats_per_100g=0.3, category='Peixes e Marisco'),

                # -- HIDRATOS --
                FoodItem(name='Arroz Branco', calories_per_100g=130, protein_per_100g=2.7, carbs_per_100g=28, fats_per_100g=0.3, category='Hidratos'),
                FoodItem(name='Arroz Basmati', calories_per_100g=121, protein_per_100g=3.5, carbs_per_100g=25, fats_per_100g=0.4, category='Hidratos'),
                FoodItem(name='Arroz Agulha', calories_per_100g=130, protein_per_100g=2.7, carbs_per_100g=28, fats_per_100g=0.3, category='Hidratos'),
                FoodItem(name='Arroz Integral', calories_per_100g=111, protein_per_100g=2.6, carbs_per_100g=23, fats_per_100g=0.9, category='Hidratos'),
                FoodItem(name='Arroz Vaporizado', calories_per_100g=123, protein_per_100g=2.9, carbs_per_100g=26, fats_per_100g=0.4, category='Hidratos'),
                FoodItem(name='Massa (Esparguete/Penne/Macarrão)', calories_per_100g=131, protein_per_100g=5, carbs_per_100g=25, fats_per_100g=1.1, category='Hidratos'),
                FoodItem(name='Batata Branca', calories_per_100g=77, protein_per_100g=2, carbs_per_100g=17, fats_per_100g=0.1, category='Hidratos'),
                FoodItem(name='Batata Doce', calories_per_100g=86, protein_per_100g=1.6, carbs_per_100g=20, fats_per_100g=0.1, category='Hidratos'),
                FoodItem(name='Batata Vermelha', calories_per_100g=70, protein_per_100g=1.9, carbs_per_100g=16, fats_per_100g=0.1, category='Hidratos'),
                FoodItem(name='Pão Bijou / Carcaça', calories_per_100g=289, protein_per_100g=9, carbs_per_100g=56, fats_per_100g=1.8, category='Hidratos'),
                FoodItem(name='Pão Integral', calories_per_100g=252, protein_per_100g=12, carbs_per_100g=43, fats_per_100g=3.5, category='Hidratos'),
                FoodItem(name='Pão de Mistura', calories_per_100g=260, protein_per_100g=9, carbs_per_100g=50, fats_per_100g=1.5, category='Hidratos'),
                FoodItem(name='Pão de Centeio', calories_per_100g=259, protein_per_100g=8.5, carbs_per_100g=48, fats_per_100g=3.3, category='Hidratos'),
                FoodItem(name='Pão de Mafra / Alentejano', calories_per_100g=270, protein_per_100g=9, carbs_per_100g=52, fats_per_100g=1.2, category='Hidratos'),

                # -- CHARCUTARIA E LACTICÍNIOS --
                FoodItem(name='Queijo Flamengo', calories_per_100g=353, protein_per_100g=24, carbs_per_100g=1.5, fats_per_100g=28, category='Laticínios e Charcutaria'),
                FoodItem(name='Queijo Mozzarella', calories_per_100g=280, protein_per_100g=28, carbs_per_100g=3.1, fats_per_100g=17, category='Laticínios e Charcutaria'),
                FoodItem(name='Queijo Fresco', calories_per_100g=299, protein_per_100g=11, carbs_per_100g=3.4, fats_per_100g=27, category='Laticínios e Charcutaria'),
                FoodItem(name='Requeijão', calories_per_100g=174, protein_per_100g=11, carbs_per_100g=3.4, fats_per_100g=13, category='Laticínios e Charcutaria'),
                FoodItem(name='Queijo Curado / Serra', calories_per_100g=400, protein_per_100g=25, carbs_per_100g=1, fats_per_100g=33, category='Laticínios e Charcutaria'),
                FoodItem(name='Queijo Edam', calories_per_100g=357, protein_per_100g=25, carbs_per_100g=1.4, fats_per_100g=28, category='Laticínios e Charcutaria'),
                FoodItem(name='Fiambre (Perna Extra)', calories_per_100g=145, protein_per_100g=17, carbs_per_100g=1.5, fats_per_100g=8, category='Laticínios e Charcutaria'),
                FoodItem(name='Fiambre de Peru / Frango', calories_per_100g=104, protein_per_100g=16, carbs_per_100g=2, fats_per_100g=3.5, category='Laticínios e Charcutaria'),
                FoodItem(name='Chouriço', calories_per_100g=455, protein_per_100g=24, carbs_per_100g=1.5, fats_per_100g=39, category='Laticínios e Charcutaria'),
                FoodItem(name='Presunto', calories_per_100g=235, protein_per_100g=28, carbs_per_100g=0, fats_per_100g=13, category='Laticínios e Charcutaria'),
                FoodItem(name='Paio', calories_per_100g=400, protein_per_100g=25, carbs_per_100g=1, fats_per_100g=33, category='Laticínios e Charcutaria'),
                FoodItem(name='Iogurte Natural', calories_per_100g=61, protein_per_100g=3.5, carbs_per_100g=4.7, fats_per_100g=3.3, category='Laticínios e Charcutaria'),
                FoodItem(name='Iogurte Grego', calories_per_100g=59, protein_per_100g=10, carbs_per_100g=3.6, fats_per_100g=0.4, category='Laticínios e Charcutaria'),
                FoodItem(name='Iogurte Líquido', calories_per_100g=75, protein_per_100g=3, carbs_per_100g=11, fats_per_100g=1.5, category='Laticínios e Charcutaria'),
                FoodItem(name='Leite Meio-gordo', calories_per_100g=47, protein_per_100g=3.3, carbs_per_100g=4.8, fats_per_100g=1.6, category='Laticínios e Charcutaria'),
                FoodItem(name='Leite Magro', calories_per_100g=35, protein_per_100g=3.4, carbs_per_100g=5, fats_per_100g=0.1, category='Laticínios e Charcutaria'),
                FoodItem(name='Bebida Vegetal (Aveia/Soja)', calories_per_100g=45, protein_per_100g=1, carbs_per_100g=6, fats_per_100g=1.5, category='Laticínios e Charcutaria'),

                # -- FRUTAS --
                FoodItem(name='Maçã', calories_per_100g=52, protein_per_100g=0.3, carbs_per_100g=14, fats_per_100g=0.2, category='Frutas'),
                FoodItem(name='Banana', calories_per_100g=89, protein_per_100g=1.1, carbs_per_100g=23, fats_per_100g=0.3, category='Frutas'),
                FoodItem(name='Laranja / Clementina', calories_per_100g=47, protein_per_100g=0.9, carbs_per_100g=12, fats_per_100g=0.1, category='Frutas'),
                FoodItem(name='Pêra', calories_per_100g=57, protein_per_100g=0.4, carbs_per_100g=15, fats_per_100g=0.1, category='Frutas'),
                FoodItem(name='Morango / Frutos Vermelhos', calories_per_100g=32, protein_per_100g=0.7, carbs_per_100g=7.7, fats_per_100g=0.3, category='Frutas'),
                FoodItem(name='Uvas', calories_per_100g=69, protein_per_100g=0.7, carbs_per_100g=18, fats_per_100g=0.2, category='Frutas'),
                FoodItem(name='Melancia / Melão', calories_per_100g=30, protein_per_100g=0.6, carbs_per_100g=8, fats_per_100g=0.2, category='Frutas'),
                FoodItem(name='Kiwi', calories_per_100g=61, protein_per_100g=1.1, carbs_per_100g=15, fats_per_100g=0.5, category='Frutas'),
                FoodItem(name='Manga / Ananás', calories_per_100g=60, protein_per_100g=0.8, carbs_per_100g=15, fats_per_100g=0.4, category='Frutas'),

                # -- REFEIÇÕES (Exemplos) --
                FoodItem(name='Papas de Aveia', calories_per_100g=68, protein_per_100g=2.4, carbs_per_100g=12, fats_per_100g=1.4, category='Refeições'),
                FoodItem(name='Ovos Mexidos', calories_per_100g=148, protein_per_100g=10, carbs_per_100g=1.6, fats_per_100g=11, category='Refeições'),
                FoodItem(name='Torradas', calories_per_100g=313, protein_per_100g=13, carbs_per_100g=56, fats_per_100g=4.3, category='Refeições'),
                FoodItem(name='Cereais', calories_per_100g=379, protein_per_100g=7, carbs_per_100g=84, fats_per_100g=1, category='Refeições'),
                FoodItem(name='Sopa de Legumes', calories_per_100g=35, protein_per_100g=1.5, carbs_per_100g=6, fats_per_100g=0.5, category='Refeições'),
                FoodItem(name='Salada Mista', calories_per_100g=17, protein_per_100g=1, carbs_per_100g=3.3, fats_per_100g=0.2, category='Refeições'),
                FoodItem(name='Grelhados (Misto)', calories_per_100g=200, protein_per_100g=25, carbs_per_100g=0, fats_per_100g=10, category='Refeições'),
                FoodItem(name='Assado no Forno', calories_per_100g=220, protein_per_100g=20, carbs_per_100g=5, fats_per_100g=12, category='Refeições'),
                FoodItem(name='Cozido à Portuguesa', calories_per_100g=180, protein_per_100g=15, carbs_per_100g=10, fats_per_100g=8, category='Refeições'),
            ]
            db.session.bulk_save_objects(foods)
            db.session.commit()
            print("Base de dados de alimentos populada com sucesso!")
        else:
            print("Base de dados já contém alimentos.")

if __name__ == '__main__':
    seed_foods()
