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

 

def product(*args, repeat=1):
    """
    Return the cartesian product of input iterables. 
    >>> list(product('ABCD', 'xy', '12'))
    [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'y', '1'),\
 ('A', 'y', '2'), ('B', 'x', '1'), ('B', 'x', '2'),\
 ('B', 'y', '1'), ('B', 'y', '2'), ('C', 'x', '1'),\
 ('C', 'x', '2'), ('C', 'y', '1'), ('C', 'y', '2'),\
 ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'y', '1'),\
 ('D', 'y', '2')]
    >>> list(product(range(3), repeat=3))
    [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0),\
 (0, 1, 1), (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2),\
 (1, 0, 0), (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1),\
 (1, 1, 2), (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0),\
 (2, 0, 1), (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2),\
 (2, 2, 0), (2, 2, 1), (2, 2, 2)]
    >>> list(product('ABC', repeat=3))
    [('A', 'A', 'A'), ('A', 'A', 'B'), ('A', 'A', 'C'),\
 ('A', 'B', 'A'), ('A', 'B', 'B'), ('A', 'B', 'C'),\
 ('A', 'C', 'A'), ('A', 'C', 'B'), ('A', 'C', 'C'),\
 ('B', 'A', 'A'), ('B', 'A', 'B'), ('B', 'A', 'C'),\
 ('B', 'B', 'A'), ('B', 'B', 'B'), ('B', 'B', 'C'),\
 ('B', 'C', 'A'), ('B', 'C', 'B'), ('B', 'C', 'C'),\
 ('C', 'A', 'A'), ('C', 'A', 'B'), ('C', 'A', 'C'),\
 ('C', 'B', 'A'), ('C', 'B', 'B'), ('C', 'B', 'C'),\
 ('C', 'C', 'A'), ('C', 'C', 'B'), ('C', 'C', 'C')]
    """
    lst = []
    for rep in range(repeat):
        for i in args:
            lst.append(tuple(i))
    lst2 = [[]]
    for elem0 in lst:
        for elem1 in lst2:
            for elem2 in elem0:
                lst2 = lst2 + [elem1+[elem2]]
    new_lst = [elem3 for elem3 in lst2 if len(elem3) == (len(args)*repeat)]
    for elem4 in new_lst:
        yield tuple(elem4)



def combinations(iterable, r):
    """return generator with all combinations
    of r elemnets from iterable"""
    input_it=tuple(iterable)
    n=len(input_it)
    if r>n:
        return
    ourange=[i for i in range(r)]
    yield tuple(input_it[i] for i in ourange)
    while True:
        y=0
        for i in reversed(range(r)):
            if ourange[i] != i + n - r:
                y=1
                break
        if y==0:
            return
        ourange[i] += 1
        for j in range(i+1, r):
            ourange[j] = ourange[j-1] + 1
        yield tuple(input_it[i] for i in ourange)



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