"""
ITERTOOLS IMPLEMENTATION
"""
def count(start=0, step=1):
    """
    Returns the iterator of an infinite loop on integers.
    (start, start+1*step, start+2*step, ...)
    >>> next(count(start=5, step=3))
    5
    """
    i = 0
    while True:
        yield start + i*step
        i += 1

def cycle(iterable):
    """
    Returns an infinite iterator on the iterator content cycle.
    """
    while True:
        for element in iterable:
            yield element

def repeat(value):
    """
    Returns an infinite iterator of duplicate values.
    """
    while True:
        yield value



def combinations_with_replacement(string_of_elements, amount_of_el):
    #Imploments an analogue of itertools combinations with replacement
    index_list = [0] * amount_of_el
    list_of_elements = tuple(string_of_elements)
    edge_of_elements = len(list_of_elements) - 1
    yield tuple(list_of_elements[i] for i in index_list)
    while index_list != [edge_of_elements] * amount_of_el:
        for index in range(amount_of_el - 1, -1, -1):
            if index_list[index] != edge_of_elements: break
        index_list[index:] = [index_list[index] + 1] * (amount_of_el - index)
        yield tuple(list_of_elements[i] for i in index_list)
