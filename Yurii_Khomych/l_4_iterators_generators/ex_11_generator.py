def countdown(num):
    print("Starting")
    while num > 0:
        yield num
        num -= 1


val = countdown(5)

num_1 = next(val)
num_2 = next(val)
next(val)
next(val)
next(val)
# next(val)

my_list = ["a", "b", "c", "d"]
gen_obj = (x for x in my_list)
for val in gen_obj:
    print(val)


import sys

g = (i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0)
print(sys.getsizeof(g))

l = [i * 2 for i in range(10000) if i % 3 == 0 or i % 5 == 0]
print(sys.getsizeof(l))
