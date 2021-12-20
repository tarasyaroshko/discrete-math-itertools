"""
ITERTOOLS IMPLEMENTATION
"""


def permutations(iterable, length=None):
    if length is None:
        length = len(list(iterable))
    if length > len(list(iterable)):
        # print "Your r cannot be longer than length of the iterable"
        return
    list_of_index = list(range(len(list(iterable))))
    list_of_cycles = list(
        range(len(list(iterable)), len(list(iterable))-length, -1))
    yield(tuple(list(iterable)[i] for i in list_of_index[:length]))
    while len(list(iterable)):
        for i in reversed(range(length)):
            list_of_cycles[i] -= 1
            if list_of_cycles[i] == 0:
                list_of_index[i:] = list_of_index[i+1:] + list_of_index[i:i+1]
                list_of_cycles[i] = len(list(iterable)) - i
            else:
                j = list_of_cycles[i]
                list_of_index[i], list_of_index[-j] = list_of_index[-j], list_of_index[i]
                yield(tuple(list(iterable)[i] for i in list_of_index[:length]))
                break
        else:
            return


def combinations_with_replacement(string_of_elements, amount_of_el):
    # Imploments an analogue of itertools combinations with replacement
    index_list = [0] * amount_of_el
    list_of_elements = tuple(string_of_elements)
    edge_of_elements = len(list_of_elements) - 1
    yield tuple(list_of_elements[i] for i in index_list)
    while index_list != [edge_of_elements] * amount_of_el:
        for index in range(amount_of_el - 1, -1, -1):
            if index_list[index] != edge_of_elements:
                break
        index_list[index:] = [index_list[index] + 1] * (amount_of_el - index)
        yield tuple(list_of_elements[i] for i in index_list)
