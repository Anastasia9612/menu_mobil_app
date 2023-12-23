import sqlite3
from flask import Flask, g, render_template, request

DATABASE = '/C:/Users/Anastasia/fproject/receipts_database'

breakfast = "('Завтрак')"
lunch = "('Основные блюда', 'Закуски')"
dinner = "('Основные блюда', 'Закуски')"
snack = "('Салаты')"



def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db


#генерация списка блюд с учетом запрещенных продуктов и приема пищи
def generate_meal_query(meal, count, forbidden_ingredients):#count 14 - на всю неделю, 1  - для замены

    forbidden_ingredients_str = ', '.join([f"'{ingredient}'" for ingredient in forbidden_ingredients])
    query1 = f"""
    SELECT d.id
    FROM (SELECT * FROM dishes WHERE category IN {meal} ORDER BY RANDOM() LIMIT 100) d
    WHERE d.id IN (
        SELECT r.dish_id
        FROM recipes r
        JOIN ingredients i ON r.ingredient = i.id
        WHERE i.name NOT IN ({forbidden_ingredients_str})
        GROUP BY r.dish_id
    )
    AND NOT EXISTS (
        SELECT *
        FROM recipes r2
        JOIN ingredients i2 ON r2.ingredient = i2.id
        WHERE r2.dish_id = d.id
        AND i2.name IN ({forbidden_ingredients_str})
    )
    LIMIT {count};
    """
    return query1


#список продуктов и мер по индексам блюд
def generate_product_query(dish_list):
    query2 = f"""
    SELECT i.name AS ingredient_name, r.amount
    FROM recipes r
    JOIN ingredients i ON r.ingredient = i.id
    WHERE r.dish_id IN ({dish_list})
    """
    return query2

#список названий блюд
def generate_name_query(dish_list):
    query3 = f"""
    SELECT id, name 
    FROM dishes 
    WHERE id IN ({dish_list});
    """
    return query3



