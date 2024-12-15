import os

#1 Задача

with open('recipes.txt') as file:
    cook_book = {}
    for i in file:
        recipe_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            product, quantity, word = recipe
            ingredients.append({'ingredient name': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recipe_name] = ingredients
# print(cook_book)


#2 Задача

def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient name'] in result:
                    result[consist['ingredient name']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['ingredient name']] = {'measure': consist['measure'], 'quantity': (int(consist['quantity']) * person_count)}
        else:
            print('Такого блюда нет в книге')
    # print(result)


get_shop_list_by_dishes(['Омлет', 'Запеченный картофель'], 3)

#3 Задача

count = 0
count_list = []
mlist = ('1.txt', '2.txt', '3.txt')
f_list = []
for t in mlist:
    with open(t) as f:
        for line in f:
            count += 1
    count_list.append(count)
    count = 0
print(count_list)
print(sorted(count_list))
print(f_list)


# file_path = os.path.join(os.getcwd(), '1.txt')
# print(file_path)
# with open('main.txt', 'w') as f:
#     f.write('1.txt'.read())