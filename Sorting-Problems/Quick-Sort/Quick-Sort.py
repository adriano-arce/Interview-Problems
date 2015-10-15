from random import choice


def quick_sort(A, low=0, high=None):
    """Quick sorts A[low : high+1]."""
    if high is None:
        high = len(A) - 1
    if high - low <= 0:  # Base Case: Length pf subarray is 1 or less.
        return

    i, j = low, high
    pivot = choice(A[i : j+1])
    while i <= j:
        # Move i and j closer together until they get converge on the pivot.
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:  # Protect the next line.
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1

    quick_sort(A, low, j)
    quick_sort(A, i, high)


def main():
    arrays = [
        [],
        [5, 7, 6, 2, 4, 1, 2, 4, 5, 5],
        [1, 2, 3, 4],
        [5, 4, 3, 2]
    ]
    for i, A in enumerate(arrays):
        print('Test Case #{}: {}'.format(i + 1, A))
        quick_sort(A)
        print('    {}'.format(A))

if __name__ == '__main__':
    main()