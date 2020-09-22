import json

profit = {}
pr = {}
prof = 0
prof_aver = 0
average_profit = 0
i = 0
with open('text_7.txt', 'r', encoding='utf-8') as file:
    for line in file:
        profVal, firm, earning, damage = line.split()
        profit[profVal] = int(earning) - int(damage)
        if profit.setdefault(profVal) >= 0:
            prof = prof + profit.setdefault(profVal)
            i += 1
    if i != 0:
        average_profit = prof / i
        print(f'Прибыль средняя - {average_profit:.2f}')
    else:
        print(f'Прибыль средняя - отсутсвует. Все работают в убыток')

    pr['average_profit'] = round(average_profit)
    print(f'Прибыль каждой компании - {profit}')

with open('file_7.json', 'w', encoding='utf-8') as write_js:
    profit_json = [profit, pr]
    print(profit_json)
    json.dump(profit_json, write_js)

    js_str = json.dumps(profit_json, indent=4, sort_keys=True, ensure_ascii=False)
    print(f'Создан файл с расширением json со следующим содержимым: \n '
          f' {js_str}')
