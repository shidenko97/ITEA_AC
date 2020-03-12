import collections

d = collections.OrderedDict(one=1, two=2, three=3)

d
# OrderedDict([('one', 1), ('two', 2), ('three', 3)])

d["four"] = 4
d
# OrderedDict([('one', 1), ('two', 2), ('three', 3), ('four', 4)])

d.keys()
# odict_keys(['one', 'two', 'three', 'four'])

# collections.OrderedDict(**d, **collections.OrderedDict(four=5))
# collections.OrderedDict(**d, **collections.OrderedDict(five=5))
