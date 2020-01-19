import json


# удаляет по имени
def dict_remove(dictionaries, name):
    path = name.split(".")

    if not (type(dictionaries) is list):
        dictionaries = [dictionaries]

    for el in dictionaries:
        if not (type(el) is dict):
            continue

        if not (path[0] in el.keys()):
            continue

        if len(path) > 1:
            dict_remove(el[path[0]], ".".join(path[1:]))
        else:
            del el[path[0]]


# возвращает по имени
def dict_get(dictionaries, name):
    path = name.split(".")
    res = []

    if not (type(dictionaries) is list):
        dictionaries = [dictionaries]

    for el in dictionaries:
        if not (type(el) is dict):
            continue
        if not (path[0] in el.keys()):
            continue
        if len(path) > 1:
            res += dict_get(el[path[0]], ".".join(path[1:]))
        else:
            res += [el[path[0]]]

    return res


# поиск в глубину с изменением найденых значений
def dfs(dictionaries):
    if not (type(dictionaries) is list):
        dictionaries = [dictionaries]

    for el in dictionaries:
        if not (type(el) is dict):
            continue

        for key in el.keys():
            dfs(el[key])
            keys2rem = []
            if key == "table_columns":
                for x in el[key]:
                    if x["unit"] != "EUR": keys2rem.append(x)
                for x in keys2rem: el[key].remove(x)
            elif key == "metric_sums":
                for x in el[key]:
                    if x["unit_key"] != "EUR":  keys2rem.append(x)
                for x in keys2rem: el[key].remove(x)
            elif key == "report_name":
                el[key] = el[key].upper()
            elif key == "page_id":
                if el[key] == "(not set)":
                    el[key] = None


def ins_to_dict(dictionaries, key):
    res = {}
    for i in range(len(dictionaries)):
        if key not in dictionaries[i].keys():
            continue
        res[i if "id" not in dictionaries[i].keys() else dictionaries[i]["id"]] = dictionaries[i][key]
    return res


# считает сумму и среднее по заданному пути
def calculate(dictionaries, name):
    arr = dict_get(dictionaries, name)
    try:
        temp = []
        for x in arr: temp.append(int(x))
        return sum(temp), sum(temp) / len(temp)
    except Exception as e:
        print(e)


# сортирует по ключу первого уровня
def sort(dictionaries, key):
    res = []
    for el in dictionaries:
        if key in el.keys():
            res.append(el)
    res.sort(key=lambda x: x[key])
    for el in dictionaries:
        if key not in el.keys():
            res.append(el)
    return res


def save(dictionaries):
    with open('hw_out.json', 'w') as outfile:
        json.dump(dictionaries, outfile, ensure_ascii=False, indent=4)