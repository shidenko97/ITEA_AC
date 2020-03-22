import pickle


def my_func(x):
    return x


my_list = ["hello", 3, "ten", 10, "nice day today", {"my_func": my_func}]

with open("my_file.pcl", "wb") as my_file:
    pickle.dump(my_list, my_file)

with open("my_file.pcl", "rb") as my_file:
    data = pickle.load(my_file)
    pass
