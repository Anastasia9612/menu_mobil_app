from flask import Flask, g, render_template, request, jsonify
from db import get_db, generate_meal_query, generate_product_query, breakfast, lunch, dinner, snack, generate_name_query
from convert_product import combine_and_count_with_conversion
import json
import re

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

peopleCount = 1

  
@app.route('/', methods=['GET', 'POST'])
def main_screen():
    global peopleCount 
    forbiddenProducts = []
    if request.method == 'POST':
        data = request.get_json  # Получаем JSON-данные из запроса
        forbiddenProducts = data.get('forbiddenProducts', [])
        peopleCount = data.get('peopleCount')


    cur = get_db().execute(generate_meal_query(breakfast, 14, forbiddenProducts))
    br = cur.fetchall()
    
    cur = get_db().execute(generate_meal_query(lunch, 14, forbiddenProducts))
    lun = cur.fetchall()
    
    cur = get_db().execute(generate_meal_query(dinner, 14, forbiddenProducts))
    din = cur.fetchall()
    
    cur = get_db().execute(generate_meal_query(snack, 14, forbiddenProducts))
    sn = cur.fetchall()

    cur.close()
    
    return render_template('mainScreen.html', breakfast = br, lunch = lun,
                           dinner = din, snack = sn)


    
@app.route('/shopping_list', methods=['GET', 'POST'])
def shopping_list():
    global peopleCount
    peopleCount = int(peopleCount)
    
    breakfastMenu = str(1)
    lunchMenu = str(1)
    dinnerMenu = str(1)
    snackMenu = str(1)
   
    if request.method == 'POST':
        data = request.json  # Получаем JSON-данные из запроса
        breakfastMenu = data.get('breakfastMenu')  # Получаем данные из объекта JSON
        lunchMenu = data.get('lunchMenu')
        dinnerMenu = data.get('dinnerMenu')
        snackMenu = data.get('snackMenu')


    numbers = re.findall(r'\b\d+\b', breakfastMenu)
    result = ', '.join(numbers)

    cur = get_db().execute(generate_product_query(result))
    pr = cur.fetchall()
    print(pr)
    print("********************************************")
    pm = combine_and_count_with_conversion(pr, peopleCount)
    print(pm)
    return render_template('shopping_list.html')


@app.route('/menu', methods=['GET', 'POST'])
def menu():

   
    if request.method == 'POST':

        data = request.get_json()  # Получаем JSON-данные из запроса
        breakfastMenu = data.get('breakfastMenu')  # Получаем данные из объекта JSON
        lunchMenu = data.get('lunchMenu')
        dinnerMenu = data.get('dinnerMenu')
        snackMenu = data.get('snackMenu')
        
      
        numbers = re.findall(r'\b\d+\b', breakfastMenu)
        result = ', '.join(numbers)
        cur = get_db().execute(generate_name_query(result))
        breakfastMenu = cur.fetchall()
            
        numbers = re.findall(r'\b\d+\b', lunchMenu)
        result = ', '.join(numbers)
        cur = get_db().execute(generate_name_query(result))
        lunchMenu = cur.fetchall()

        numbers = re.findall(r'\b\d+\b', dinnerMenu)
        result = ', '.join(numbers)
        cur = get_db().execute(generate_name_query(result))
        dinnerMenu = cur.fetchall()

        numbers = re.findall(r'\b\d+\b', snackMenu)
        result = ', '.join(numbers)
        cur = get_db().execute(generate_name_query(result))
        snackMenu = cur.fetchall()
            
        cur.close()
        print(breakfastMenu)
        print(lunchMenu)
        print(dinnerMenu)
        print(snackMenu)

        #breakfastMenu = "1"
        #lunchMenu = "1"
        #dinnerMenu = "1"
        #snackMenu = "1"
        
        return render_template('menu.html', breakfast = breakfastMenu, lunch = lunchMenu,
                                   dinner = dinnerMenu, snack = snackMenu)
    else:
         return render_template('menu.html')

if __name__ == '__main__':
     app.run(debug=True,host='0.0.0.0')


'''

'''
