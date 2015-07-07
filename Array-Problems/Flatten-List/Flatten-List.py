def flatten_list(L):
    """
    Flattens the given list.

    Remark:
        If we want to allow for tuples, use:
            if isinstance(element, (list, tuple)):
        If we don't want to allow for inherited subclasses of list, use:
            if type(element) == list
    """
    flattened = []
    for element in L:
        if isinstance(element, list):
            flattened.extend(flatten_list(element))
        else:
            flattened.append(element)
    return flattened


def main():
    test_lists = [
        [],
        [1, [2, 3, 4], [], [5, [6, 7]]],
        [[[[[1]]]]],
        [[[[1, 2], 3, 4], [5, 6]], 7, [8, [9]]],
        [1, 2, [3, 4, 5, [6, 7, [], [[8, 9]]]]]
    ]
    for i, L in enumerate(test_lists):
        print("Test Case #{}:".format(i + 1))
        print("    BEFORE:", L)
        print("     AFTER:", flatten_list(L))

if __name__ == "__main__":
    main()