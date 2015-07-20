def get_power_set(s):
    """
    Returns a list of all possible subsets of the given set s.
    """
    #---------------------------------------------------------------------------
    # Version 1: The input s is stored as a set. Recursive.
    #---------------------------------------------------------------------------
    # # Base Case: 2^0 = 1.
    # if not s:
    #     return [set()]
    #
    # # Inductive Step: 2^n = 2^{n - 1} * 2.
    # x = s.pop()
    # subsets = get_power_set(s)
    # subsets.extend([t | {x} for t in subsets])
    # return subsets

    #---------------------------------------------------------------------------
    # Version 2a: The input s is stored as a list. Recursive.
    #---------------------------------------------------------------------------
    # # Base Case: 2^0 = 1.
    # if not s:
    #     return [[]]
    #
    # # Inductive Step: 2^n = 2^{n - 1} * 2.
    # x = s.pop()
    # subsets = get_power_set(s)
    # subsets.extend([t + [x] for t in subsets])
    # return subsets

    #---------------------------------------------------------------------------
    # Version 2b: Iterative translation of 2a.
    #---------------------------------------------------------------------------
    # subsets = [[]]
    # for x in s:
    #     subsets.extend([t + [x] for t in subsets])  # Note: Square brackets.
    # return subsets

    #---------------------------------------------------------------------------
    # Version 2c: Using binary representation.
    #---------------------------------------------------------------------------
    subsets = []
    m = 1 << len(s)
    for i in range(m):
        subsets.append([s[j] for j in range(len(s)) if (i >> j) & 1 == 1])
    return subsets




def main():
    #---------------------------------------------------------------------------
    # For Version 1.
    #---------------------------------------------------------------------------
    # test_sets = [
    #     set(), {1}, {1, 2}, {1, 2, 3}, {1, 2, 3, 4}
    # ]
    test_sets = [
        [], [1], [1, 2], [1, 2, 3], [1, 2, 3, 4]
    ]

    for i, s in enumerate(test_sets):
        print("Test Case #{}: {}".format(i, s))
        print(get_power_set(s))

if __name__ == "__main__":
    main()