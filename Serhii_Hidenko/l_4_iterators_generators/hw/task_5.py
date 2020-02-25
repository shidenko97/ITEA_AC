def interleave(list_1, list_2) -> list:
    """
    Interleave two lists in one
    :param list_1: First list
    :param list_2: Second list
    :type list_1: list
    :type list_2: list
    :return: Interleaved list
    :rtype: list
    """

    result_list = []

    for el_1, el_2 in zip(list_1, list_2):
        result_list.extend([el_1, el_2])

    return result_list


if __name__ == "__main__":

    print(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
