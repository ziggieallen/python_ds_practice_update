def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """

    # for x in lst:
    #     if x == True:
    #         return x

    return [val for val in lst if val]        