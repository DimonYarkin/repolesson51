try:
    with open('file_5.txt', 'w+') as file_obj:
        line = input('Введите набор цифр разделенных пробелами')
        file_obj.writelines(line)
        my_numb = line.split()

except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Неправильно набран номер. Ошибка ввода-вывода')

try:
    with open('file_5.txt', 'r') as file_obj:
        list_file = [sum(map(int, el.split())) for el in file_obj.readlines()]
        print(sum(list_file))
except IOError:
    print('Ошибка в файле')
except ValueError:
    print('Ошибка преобразования в файле не только цыфры')
