def find_fixed_point(arr):
    """
    Returns i such that arr[i] = i (or -1, if no such i exists).
    """
    #---------------------------------------------------------------------------
    # Easier Version: Assume that all integers are distinct (binary search).
    #---------------------------------------------------------------------------
    # low, high = 0, len(arr) - 1
    # while low <= high:
    #     mid = low + (high - low) // 2
    #     if arr[mid] == mid:
    #         return mid
    #     elif arr[mid] < mid:
    #         low = mid + 1
    #     else:
    #         high = mid - 1
    # return -1

    #---------------------------------------------------------------------------
    # General Version: Assume that integers may be repeated.
    #---------------------------------------------------------------------------
    stack = []
    push(stack, 0, len(arr) - 1)
    while stack:
        low, high = stack.pop()  # ASSERT: low <= high.
        mid = low + (high - low) // 2
        if arr[mid] == mid:
            return mid
        elif arr[mid] < mid:
            push(stack, low, arr[mid])
            push(stack, mid + 1, high)
        else:
            push(stack, low, mid - 1)
            push(stack, arr[mid], high)
    return -1


def push(stack, low, high):
    if low <= high:
        stack.append((low, high))


def main():
    test_arrays = [
        [],
        [-1, 1],
        [-3, -2, 0, 5, 6, 7],
        [-3, -1, 1, 3, 5, 6],
        [0, 2, 3, 4, 5, 6, 7, 8, 9],
        [-1, 2, 3, 4, 4, 4, 5, 7, 8],
        [-2, -2, 1, 3, 4, 5, 5, 6, 8],
        [-3, -2, 1, 1, 2, 4, 7, 9, 10]
    ]
    for i, arr in enumerate(test_arrays):
        print("Test Case #{}: {}".format(i + 1, arr))
        print("    Fixed Point: {}".format(find_fixed_point(arr)))

if __name__ == "__main__":
    main()