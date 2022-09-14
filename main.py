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
                ingridients_list = {'ingridients_name': ingridients_name, 
                                    'quantyty': quantyty,
                                    'measure': measure.strip()}
                cook_book[dish_name].append(ingridients_list)
            recipe_name.readline()
    return cook_book


def get_shop_list_by_person(dishes, person_count, cook_book):
    cook_book = json.loads(cook_book)
    shop_ing = {}
    for dish in dishes:
        for ing in cook_book[dish]:
            measur_qty = {'measure': ing['measure'], 
                          'quantyty': int(ing['quantyty']) * person_count}
            if ing['ingridients_name'] not in shop_ing:
                shop_ing[ing['ingridients_name']] = measur_qty
            else:
                shop_ing[ing['ingridients_name']]['quantyty'] += measur_qty['quantyty']
    print(f'Для приготовления, таких блюд, как: {", ".join(dishes)}, понадобятся следующие ингредиенты')
    return json.dumps(shop_ing, indent=4, ensure_ascii=False)


def concat_file(file1, file2, file3):
    count_line = []
    name1 = file1
    name2 = file2
    name3 = file3
    with open(file1, encoding='utf8') as file_1:
        content_file1 = file_1.readlines()
        count_line.append([name1, len(content_file1), content_file1])
    with open(file2, encoding='utf8') as file_2:
        content_file2 = file_2.readlines()
        count_line.append([name2, len(content_file2), content_file2])
    with open(file3, encoding='utf8') as file_3:
        content_file3 = file_3.readlines()
        count_line.append([name3, len(content_file3), content_file3])

    for i in range(len(count_line) - 1):
        if count_line[i][1] > count_line[i+1][1]:
            count_line[i], count_line[i+1] = count_line[i+1], count_line[i]

    with open('4.txt', 'w', encoding='utf8') as file4:
        for file in count_line:
            res = f'{file[0]}\n{file[1]}\n{"".join(file[2])}\n'
            file4.writelines(res)

    with open('4.txt', 'r', encoding='utf8') as file4:
        content = file4.read()
        print(content)


cook_book = json.dumps(read_recipes('file.txt'), indent=4, ensure_ascii=False)
print(cook_book)
print('*' * 20)
print(get_shop_list_by_person(["Фахитос", "Омлет"], 2, cook_book))
print('*' * 20)
concat_file('1.txt', '2.txt', '3.txt')








