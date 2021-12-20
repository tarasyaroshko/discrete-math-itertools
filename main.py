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

 

def product(*args):
    """
    Return the cartesian product of input iterables. 
    >>> list(product('ABCD', 'xy', '12'))
    [('A', 'x', '1'), ('A', 'x', '2'), ('A', 'y', '1'),\
 ('A', 'y', '2'), ('B', 'x', '1'), ('B', 'x', '2'),\
 ('B', 'y', '1'), ('B', 'y', '2'), ('C', 'x', '1'),\
 ('C', 'x', '2'), ('C', 'y', '1'), ('C', 'y', '2'),\
 ('D', 'x', '1'), ('D', 'x', '2'), ('D', 'y', '1'),\
 ('D', 'y', '2')]
    """
    lst = []
    for i in args:
        lst.append(tuple(i))
    lst2 = [[]]
    for elem0 in lst:
        for elem1 in lst2:
            for elem2 in elem0:
                lst2 = lst2 + [elem1+[elem2]]
    new_lst = [elem3 for elem3 in lst2 if len(elem3) == (len(args))]
    for elem4 in new_lst:
        yield tuple(elem4)



def combinations(r, n):
    """return generator with all combinations
    of r elemnets from range(n)"""
    if r>n:
        return
    ourange=[i for i in range(r)]
    yield tuple(i for i in ourange)
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
        yield tuple(i for i in ourange)


def combinations_with_replacement(string_of_elements, amount_of_el):
    '''
    Implements an analogue of itertools combinations with replacement
    '''
    index_list = [0] * amount_of_el # making an empty list to make combinations easily
    list_of_elements = tuple(string_of_elements) # splitting elements to make combinations with them
    edge_of_elements = len(list_of_elements) - 1 # the last index of the list string_of_elements
    yield tuple(list_of_elements[i] for i in index_list)    # records the first combination
    while index_list != [edge_of_elements] * amount_of_el:  # while we didn't reach the last element of
                                                            # string_of_elements to make combinations with them
        for index in range(amount_of_el - 1, -1, -1): # iterating in reversed index_list and if...
            if index_list[index] != edge_of_elements: break # an element with a particular
                                                            # index isn't out of range...
        index_list[index:] = [index_list[index] + 1] * (amount_of_el - index) # we make a combination on that position
                                                            # and if an element is out of range, we move on to the next
                                                            # element in a reversed index_list 
        yield tuple(list_of_elements[i] for i in index_list) # records each combination
