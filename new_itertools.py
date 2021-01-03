def count(start, step):
    '''
    Returns infinitely values starting with start number and each next is 
    equel to previos one plus step.
    '''
    lst = []
    lst.append(start)
    index = 0
    while True:
        yield lst[index]
        lst.append(lst[index] + step)
        index += 1


def cycle(object):
    """
    This function creates an infinite list of elements in object.
    """
    try:
        # list to stop iteration if object is an empty list or string
        lst = []
        for i in object:
            yield i
            lst.append(i)
        # check whether list/string is empty
        while lst:
            for j in lst:
                yield j
    except TypeError:
        print('Not iterable')


def repeat(value, num):
    '''
    Make an iterator that returns value num times
    >>> print(list(repeat(3, 4)))
    [3, 3, 3]
    >>> print(list(repeat(3, 0)))
    []
    '''
    for _ in range(num):
        yield value


def product(*iterables):
    '''
    Return a carcesian product of given iterables.
    '''
    lst = []
    for item in iterables[0]:
        for element in iterables[1]:
            lst.append(str(item) + str(element))
    iterables = list(iterables)

    for _i in range(2):
        iterables.pop(0)
    iterables.insert(0, lst)

    if len(iterables) == 1:
        for prod in iterables[0]:
            prod = list(prod)
            yield tuple(prod)
    else:
        yield from product(*iterables)


def permutations_indices(indices: list, length: int) -> object:
    """
    Return generator of permutations for the indices of an iterable.
    Length - the quantity of the elements in each tuple.
    """
    yield indices[:length]
    n = len(indices)

    if indices == sorted(indices, reverse=True):
        return

    edge = length - 1
    j = length

    while j < n and indices[edge] >= indices[j]:
        j += 1

    if j < n:
        indices[edge], indices[j] = indices[j], indices[edge]

    else:
        indices[length:] = list(reversed(indices[length:]))
        i = edge-1
        while i >= 0 and indices[i] >= indices[i+1]:
            i -= 1

        if i < 0:
            return 0

        j = n-1
        while j > i and indices[i] >= indices[j]:
            j -= 1

        indices[i], indices[j] = indices[j], indices[i]
        indices[i+1:] = list(reversed(indices[i+1:]))

    yield from permutations_indices(indices, length)


def permutations(iterable: object, length=None) -> object:
    """
    Return generator of permutations for an iterable.
    Length - the quantity of the elements in each tuple.
    By default, length = len(iterable).
    permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    permutations(range(3)) --> 012 021 102 120 201 210
    """
    full_length = len(iterable)

    if length == None:
        length = full_length

    elif length > full_length:
        return None

    pool = tuple(iterable)
    indices = list(range(len(iterable)))
    row = permutations_indices(indices, length)

    for i in row:
        yield tuple(pool[ind] for ind in i)


def combinations_indices(n: int, r: int) -> object:
    """
    Return generator of combinations for the indices of an iterable.
    r - the quantity of the elements in each tuple.
    n - the quantity of all the elements.
    """
    indices = list(range(r))
    i = r - 1

    while indices[0] < n-r+1:

        while i > 0 and indices[i] == n - r + i:
            i -= 1

        yield tuple(indices)
        indices[i] += 1

        while i < (r-1):
            indices[i+1] = indices[i]+1
            i += 1


def combinations(n: object, r=None) -> object:
    """
    Return generator of combinations for an iterable object r.
    n - the quantity of the elements in each tuple.
    By default, r = len(n).
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    """
    full_length = len(n)

    if r == None:
        r = full_length

    elif r > full_length:
        return None

    row = combinations_indices(full_length, r)
    pool = tuple(n)

    for each_tuple in row:
        yield tuple(pool[ind] for ind in each_tuple)


def product_2(*arguments, repeat=1):
    """
    This function returns cartesian product of input iterables.
    >>> product('ABCD', 'xy')
    Ax Ay Bx By Cx Cy Dx Dy
    >>> product(range(2), repeat=3)
    000 001 010 011 100 101 110 111
    """
    if repeat != 1:
        for el in arguments:
            els = [tuple(el)] * repeat
        result = [[]]
        for el in els:
            lst = []
            for num in result:
                for num2 in el:
                    lst.append(num+[num2])
            result = lst
        for product in result:
            yield tuple(product)


def combinations_with_replacement(iterable, r):
    '''
    Return r length subsequences of elements from the input iterable.
    >>> print(list(combinations_with_replacement('AB', 2)))
    [('A', 'A'), ('A', 'B'), ('B', 'B')]
    >>> print(list(combinations_with_replacement('AB', -2)))
    [()]
    '''
    pool = tuple(iterable)
    n = len(pool)
    for indices in product_2(range(n), repeat=r):
        if sorted(indices) == list(indices):
            yield tuple(pool[i] for i in indices)
