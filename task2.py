with open("text1.txt", "r", encoding="utf-8") as fileObg:
    countStr = sum(el.count('\n') for el in iter(lambda: fileObg.read(), ''))
    print(f"Количество строк в файле = {countStr}")
    fileObg.seek(0)
    n = 0
    for el in fileObg.readlines():
        n += 1
        print(f"Количество слов в строке № {n} = {len(el.split())}")
