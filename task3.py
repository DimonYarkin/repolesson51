with open("text_3.txt", "r", encoding="utf-8") as fileObg:
    list_file = [el.split() for el in fileObg.readlines() if float(el.split()[1]) < 20000]
    summ_sal = 0
    for el in list_file:
        summ_sal += float(el[1])
        print(f"Сотрудник: {el[0]} оклад {el[1]}")
    print(
        f"Количество сотрудников = {len(list_file)} итого заработная плата = {summ_sal} средний заработок = {summ_sal / len(list_file):.2f}")
