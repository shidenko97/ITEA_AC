from collections import ChainMap

baseline = {"music": "bach", "art": "rembrandt"}
adjustments = {"art": "van gogh", "opera": "carmen"}
list(ChainMap(adjustments, baseline))

{**baseline, **adjustments}
dict1 = {"one": 1, "two": 2}
dict2 = {"three": 3, "four": 4}
chain = ChainMap(dict1, dict2)

chain
# ChainMap({'one': 1, 'two': 2}, {'three': 3, 'four': 4})

# ChainMap searches each collection in the chain
# from left to right until it finds the key (or fails):
chain["three"]
# 3
chain["one"]
# 1
chain["missing"]
