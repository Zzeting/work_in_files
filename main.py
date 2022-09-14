import json


def read_recipes(file_name):
    with open(file_name, encoding='utf8') as recipe_name:
        cook_book = {}
        for line in recipe_name:
            dish_name = line.strip()
            cook_book[dish_name] = []
            ingridients_count = recipe_name.readline()
            for _ in range(int(ingridients_count)):
                ingridients = recipe_name.readline()
                ingridients_name, quantyty, measure = ingridients.split(' | ')
                ingridients_list = {'ingridients_name': ingridients_name, 'quantyty': quantyty,
                                    'measure': measure.strip()}
                cook_book[dish_name].append(ingridients_list)
            recipe_name.readline()
    return cook_book


def get_shop_list_by_person(dishes, person_count, cook_book):
    cook_book = json.loads(cook_book)
    shop_ing = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            measur_qty = {'measure': ing['measure'], 'quantyty': int(ing['quantyty']) * person_count}
            if ing['ingridients_name'] not in shop_ing:
                shop_ing[ing['ingridients_name']] = measur_qty
            else:
                shop_ing[ing['ingridients_name']]['quantyty'] += measur_qty['quantyty']
    return shop_ing


cook_book = json.dumps(read_recipes('file.txt'), indent=4, ensure_ascii=False)
print(cook_book)
print()
res = get_shop_list_by_person(["Фахитос", "Омлет"], 2, cook_book)
print(json.dumps(res, indent=4, ensure_ascii=False))
