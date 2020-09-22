def clearsrt(argsrt):
    list_pref = ['-', '(л)', '(пр)', '(лаб)']
    str_new = argsrt
    for el in list_pref:
        str_new = str_new.replace(el, "")
    return str_new


subj = {}
with open('text_6.txt', 'r', encoding='utf-8') as fileObj:
    for el in fileObj:
        list_line = clearsrt(el).split()
        key_dic = list_line.pop(0)
        sum_list = list(map(int, list_line))
        subj[key_dic] = sum(sum_list)

print(f"Общее количество часов по предметам \n {subj}")
