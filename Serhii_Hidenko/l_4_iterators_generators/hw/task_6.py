def generator_squared_interleave(list_1, list_2) -> object:
    """
    Generator of squared interleave two lists in one
    :param list_1: First list
    :param list_2: Second list
    :type list_1: list
    :type list_2: list
    :return: Generator of squared list
    :rtype: object
    """

    return (el_1 ** el_2 for el_1, el_2 in zip(list_1, list_2))


if __name__ == "__main__":

    print(generator_squared_interleave([1, 2, 3, 4], [5, 6, 7, 8]))
