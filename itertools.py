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

# def product(*args, repeat=1):
#     if repeat > 1:
#         if not isinstance(args, str):
#             for i in args:
#                 i = list(i)
#                 tuple_item = tuple([str(i[m]) for m in range(len(i))])
#             args = [tuple_item for rep in range(repeat)]
#         else:
#             args = [args[0] for rep in range(repeat)] 
#     lst = []
#     n = len(args)
#     while n > 1:
#         lst2 = []
#         for i in args:
#             lst.append(tuple(i))
#         for k in lst[0]:
#             for l in lst[1]:
#                 lst2.append(k+l)
#         lst.pop(0)
#         if len(args) < 3:
#             lst[0] = tuple(lst2)
#         else:
#             lst[0], lst[1] = tuple(lst2), lst[1]
#         n -= 1
#     yield lst[0]
# print(tuple(product('ABCD', 'xy', '12')))
# import itertools
# print(tuple(itertools.product('ABCD', 'xy', '12')))
# import itertools
# print(tuple(itertools.product('ABCD', 'xy', '12')))

# def product(*args, repeat=1):
#     lst = [tuple(i) for i in args]
#     lst1 = []
#     lst2 = [lst1]
#     return lst
# print(product('ABCD', 'xy', '12'))