my_dic = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open("text_4.txt", "r", encoding="utf-8") as fileObg:
    pool_new = []
    list_file = [el.split(" - ") for el in fileObg.readlines()]
    for el in list_file:
        el[0] = my_dic[el[0]]
        pool_new.append(" - ".join(el))

with open('file_4_new.txt', 'w', encoding='utf-8') as file_obj_2:
    file_obj_2.writelines(pool_new)
