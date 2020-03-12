class Series:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

    # def my_rules_iter(self):
    #     for x in range(self.current, self.high):
    #


n_list = Series(1, 10)
# series_iterator = iter(n_list)
# next(series_iterator)
# next(series_iterator)
# next(series_iterator)
for x in n_list:
    print(x)
for x in n_list:
    print(x)

print(list(n_list))
a = [1, 2, 3]
gen_comp = (x for x in range(3))
list_compr = [x for x in range(3)]
next(a)
a_iter = iter(a)
next(a_iter)


a = ["foo", "bar", "baz"]
itr = iter(a)
list(itr)
