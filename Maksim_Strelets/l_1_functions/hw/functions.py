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


def elem_get(el, key):
    if type(key) is not str:
        return None
    path = key.split(".")

    if type(el) is list:
        res = [elem_get(x, key) for x in el]
        return res

    if path[0] not in el.keys():
        return None

    if len(path) > 1:
        return elem_get(el[path[0]], ".".join(path[1:]))
    else:
        return el[key]


# возвращает по имени
def dict_get(dictionaries, name):
    path = name.split(".")
    res = []

    if not (type(dictionaries) is list):
        dictionaries = [dictionaries]

    for el in dictionaries:
        temp = elem_get(el, name)
        if temp:
            res += temp

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
                if el[key] == "device":
                    el[key] = el[key].upper()
            elif key == "page_id":
                if el[key] == "(not set)":
                    el[key] = None


def ins_to_dict(dictionaries, key, val=""):
    if not val:
        val = key
    res = {}
    for i in range(len(dictionaries)):
        if key not in dictionaries[i].keys() or val not in dictionaries[i].keys():
            continue
        res[i if key not in dictionaries[i].keys() else dictionaries[i][key]] = dictionaries[i][val]
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


def summary(period, api, summ, sum_level, sum_general):
    if period > 4 or period is None:
        period = 7
    if sum_general == 0:
        return None
    formula = {
        1: lambda: (summ * sum_level / sum_general) / period,
        2: lambda: (summ * sum_level ^ 2 / sum_general) / period,
        3: lambda: (sum_level / sum_general) / period,
        4: lambda: (sum_level * 100) / period
    }
    return formula[api]()


def calc_by_formula(dictionaries):
    keys = ["period", "api", "metric_sums.sum", "metric_sums.sum_level", "metric_sums.sum_general"]
    res = []
    for el in dictionaries:
        temp = {}
        for key in keys:
            temp[key] = elem_get(el, key)
        if None in temp.values():
            continue

        for i in range(len(temp["metric_sums.sum"])):
            val = summary(period=int(temp["period"]), api=int(temp["api"]),
                          summ=int(temp["metric_sums.sum"][i]),
                          sum_level=int(temp["metric_sums.sum_level"][i]),
                          sum_general=int(temp["metric_sums.sum_general"][i]))
            if val:
                res.append(val)
    return res


def save(dictionaries):
    with open('hw_out.json', 'w') as outfile:
        json.dump(dictionaries, outfile, ensure_ascii=False, indent=4)