def clearsrt(argsrt):
    list_pref = ['-', '(л)', '(пр)', '(лаб)']
    str_new = argsrt
    for el in list_pref:
        str_new = str_new.replace(el, "")
    return str_new


subj = {}
with open('text_6.txt', 'r') as fileObj:
    for el in fileObj:
        print(clearsrt(el))
