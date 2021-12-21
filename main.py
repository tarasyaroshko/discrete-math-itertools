"""
ITERTOOLS IMPLEMENTATION
"""

def count(start=0, step=1):
    """
    Returns the iterator of an infinite loop on integers.
    (start, start+1*step, start+2*step, ...)
    >>> next(count(start=5, step=3))
    5
    >>> gen = count(1, 2)
    >>> list(next(gen) for _ in range(5))
    [1, 3, 5, 7, 9]
    """
    i = 0
    while True:
        yield start + i*step
        i += 1

def cycle(iterable):
    """
    Returns an infinite iterator on the iterator content cycle.
    >>> gen = cycle("ABC")
    >>> list(next(gen) for _ in range(6))
    ['A', 'B', 'C', 'A', 'B', 'C']
    """
    while True:
        for element in iterable:
            yield element

def repeat(value):
    """
    Returns an infinite iterator of duplicate values.
    >>> gen = repeat("hello")
    >>> list(next(gen) for _ in range(3))
    ['hello', 'hello', 'hello']
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
    >>> list(product(range(3), range(3), range(3)))
    [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1),\
 (0, 1, 2), (0, 2, 0), (0, 2, 1), (0, 2, 2), (1, 0, 0),\
 (1, 0, 1), (1, 0, 2), (1, 1, 0), (1, 1, 1), (1, 1, 2),\
 (1, 2, 0), (1, 2, 1), (1, 2, 2), (2, 0, 0), (2, 0, 1),\
 (2, 0, 2), (2, 1, 0), (2, 1, 1), (2, 1, 2), (2, 2, 0),\
 (2, 2, 1), (2, 2, 2)]
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

def permutations(iterable, length=None):
    """
    Return r length subsequences of elements from the input iterable
    >>> list(permutations('ABCD', 2))
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('B', 'A'), ('B', 'C'), \
('B', 'D'), ('C', 'A'), ('C', 'B'), ('C', 'D'), ('D', 'A'), ('D', 'B'), ('D', 'C')]
    """
    if length is None:                  # If length is not specified,
        # we assign it as length of our iterable
        length = len(tuple(iterable))
    if length > len(tuple(iterable)):
        # print "Your r cannot be longer than length of the iterable"
        return  # If the length is longer length of our iterable, it is a mistake
        # so we return nothing
    # Getting the list of indices starting from zero
    list_of_index = list(range(len(list(iterable))))
    # Getting the list of cycles which is in reversed order from
    # the length of the iterable with the step of -1 with
    # length amount of times
    list_of_cycles = list(
        range(len(list(iterable)), len(list(iterable))-length, -1))
    yield(tuple(list(iterable)[i] for i in list_of_index[:length]))
    # Yielding the first tuple of possible permutations,
    # which will be output in a correct order as it is only our first
    # return and we are not changing the order so far
    while len(list(iterable)):
        # Reversing the range(length) to iterate from the highest number
        for i in reversed(range(length)):
            # But before our next examination, we are a having a different
            # list of cycles
            list_of_cycles[i] -= 1
            if list_of_cycles[i] == 0:
                # Puts the ith item of indices at the end,
                # Shifts all following items of indices one to the left, and indicates that the next time we come to this item of cycles
                # we are be swapping the new ith item of indices (from the left) with the n - ith one (from the right)
                list_of_index[i:] = list_of_index[i+1:] + list_of_index[i:i+1]
                list_of_cycles[i] = len(list(iterable)) - i
            else:
                # If cycles[i] is j, this means that the next update to the indices is to swap the i-th one (from the left)
                # with the j-th one from the right (if j is 1, then the last element of indices is being swapped -- indices[-1])
                j = list_of_cycles[i]
                list_of_index[i], list_of_index[-j] = list_of_index[-j], list_of_index[i]
                yield(tuple(list(iterable)[i] for i in list_of_index[:length]))
                break
        else:
            return



def combinations(r, n):
    """return generator with all combinations
    of r elemnets from range(n)
    >>> for i in combinations(3,4):
    ...     print(i)
    (0, 1, 2)
    (0, 1, 3)
    (0, 2, 3)
    (1, 2, 3)
    >>> for i in combinations(5,7):
    ...     print(i)
    (0, 1, 2, 3, 4)
    (0, 1, 2, 3, 5)
    (0, 1, 2, 3, 6)
    (0, 1, 2, 4, 5)
    (0, 1, 2, 4, 6)
    (0, 1, 2, 5, 6)
    (0, 1, 3, 4, 5)
    (0, 1, 3, 4, 6)
    (0, 1, 3, 5, 6)
    (0, 1, 4, 5, 6)
    (0, 2, 3, 4, 5)
    (0, 2, 3, 4, 6)
    (0, 2, 3, 5, 6)
    (0, 2, 4, 5, 6)
    (0, 3, 4, 5, 6)
    (1, 2, 3, 4, 5)
    (1, 2, 3, 4, 6)
    (1, 2, 3, 5, 6)
    (1, 2, 4, 5, 6)
    (1, 3, 4, 5, 6)
    (2, 3, 4, 5, 6)"""
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
    """
    Implements an analogue of itertools combinations with replacement
    """
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
