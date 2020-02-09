def series_generator(low, high):
    while low <= high:
        yield low
        low += 1


n_list = []
for num in series_generator(1, 10):
    n_list.append(num)

print(n_list)
