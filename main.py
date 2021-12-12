"""
ITERTOOLS IMPLEMENTATION
"""




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
