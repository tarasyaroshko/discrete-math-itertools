def permutations(iterable, length=None):
    if length is None:
        length = len(tuple(iterable))
    if length > len(tuple(iterable)):
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
