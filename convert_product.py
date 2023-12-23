from collections import defaultdict
import re

def combine_and_count_with_conversion(items, multiplier):
    fraction_map = {
        '½': 0.5,
        '⅓': 1/3,
        '⅔': 2/3,
        '¼': 0.25,
        '¾': 0.75
    }
    
    def convert_to_number(s, multiplier):
        for k, v in fraction_map.items():
            if k in s:
                # Находим значение дроби в строке
                fraction_value = v * multiplier
                # Заменяем дробь на числовое значение
                s = s.replace(k, str(fraction_value))
        
        match = re.match(r'(\d+\.?\d*)', s)
        if match:
            number = float(match.group(1)) * multiplier
            if number.is_integer():
                return int(number), s[len(match.group(1)):]
            else:
                return number, s[len(match.group(1)):]
        else:
            return None, ''  # Возвращаем None вместо строки
    
    counts = defaultdict(float)
    units = {}
    for item, amount in items:
        converted_amount, unit = convert_to_number(amount, multiplier)
        if isinstance(converted_amount, (int, float)):  # Проверяем, что значение конвертировано в число
            counts[item] += converted_amount
            units[item] = unit
    
    result = [(item, f"{int(count) if count.is_integer() else count} {units[item]}") for item, count in counts.items()]
    return result




#data = [('Пшеничная мука', '1 стакан'), ('Куриное яйцо', '2 штуки'), ('Молоко', '3 стакана'), ('Сахар', '½ столовые ложки'), ('Соль', '½ чайные ложки'), ('Молоко', '2 стакана')]
#your_multiplier = 2  # человек
#result = combine_and_count_with_conversion(data, your_multiplier)
#print(result)
