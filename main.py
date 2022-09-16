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
    return json.dumps(cook_book, indent=4, ensure_ascii=False)


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


# def concat_file(file1, file2, file3):
#     count_line = []
#     for file in (file1, file2, file3):
#         name = file
#         with open(file, encoding='utf8') as files:
#             content_file = files.readlines()
#             count_line.append([name, content_file])
#
#     for i in range(len(count_line) - 1):
#         if len(count_line[i][1]) > len(count_line[i+1][1]):
#             count_line[i], count_line[i+1] = count_line[i+1], count_line[i]
#
#     with open('4.txt', 'w', encoding='utf8') as files:
#         for file in count_line:
#             res = f'{file[0]}\n{len(file[1])}\n{"".join(file[1])}\n'
#             files.writelines(res)
#
#     with open('4.txt', 'r', encoding='utf8') as files:
#         content = files.read()
#         print(content)


def concat_file(file1, file2, file3):
    count_line = []
    for file in (file1, file2, file3):
        name = file
        with open(file, encoding='utf8') as files:
            content_file = files.readlines()
            count_line.append([name, content_file])

    count_line.sort(key=lambda x: len(x[1]))

    with open('4.txt', 'w', encoding='utf8') as files:
        for file in count_line:
            res = f'{file[0]}\n{len(file[1])}\n{"".join(file[1])}\n'
            files.writelines(res)

    with open('4.txt', 'r', encoding='utf8') as files:
        content = files.read()
        print(content)


cook_book = read_recipes('file.txt')
print(cook_book)
print('*' * 20)
print(get_shop_list_by_person(["Фахитос", "Омлет"], 2, cook_book))
print('*' * 20)
concat_file('1.txt', '2.txt', '3.txt')








