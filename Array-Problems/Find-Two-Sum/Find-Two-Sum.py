def find_two_sum(arr, target):
    """
    Finds the two (not necessarily distinct) indices of the first two integers
    in arr that sum to target, in sorted ascending order (or returns None if no
    such pair exists).
    """
    prev_map = {}  # Maps (target - arr[i]) -> i.
    for curr_idx, num in enumerate(arr):
        # Putting this block *before* the next block allows for the possibility
        # that prev_idx == curr_idx. If this isn't desired, then put it after.
        comp = target - num
        if comp not in prev_map:  # Don't overwrite the previous mapping.
            prev_map[comp] = curr_idx
        # Check if arr[curr_idx] matches some (target - arr[prev_idx]).
        if num in prev_map:
            prev_idx = prev_map[num]
            return prev_idx, curr_idx
    return None  # No such pair exists.


def count_pairs(arr, target):
    """
    Counts the number of ordered pairs of integers in arr that sum to target.
    """
    comp_count = {}  # Counts the number of times each complement occurs in arr.
    for num in arr:
        comp = target - num
        comp_count[comp] = comp_count.get(comp, 0) + 1
    return sum(comp_count.get(num, 0) for num in arr)


def count_pairs_distinct_unordered(arr, target):
    """
    Counts the unordered pairs of distinct integers in arr that sum to target.
    """
    comp_count = {}  # Counts the number of times each complement occurs in arr.
    for num in arr:
        comp = target - num
        comp_count[comp] = comp_count.get(comp, 0) + 1

    count = 0
    for num in comp_count:
        comp = target - num
        # Forcing num < comp ensures that we don't double count.
        # Since num != comp, we also ensure that they are distinct.
        if num < comp and comp in comp_count:
            count += comp_count[num] * comp_count[comp]
    return count


if __name__ == "__main__":
    testCases = [
        ([8, 5, 6, 7], 13),
        ([3, 9, 6, 2, 1, 5], 10),
        ([3, 4, 5, 6], 12),
        ([4, 4, 4, 4, 4], 8),
        ([3, 3, 3, 5, 5, 5, 5, 5, 4, 4], 8),
        ([7, 3, 4, 1], 9)
    ]
    for index, testCase in enumerate(testCases):
        print("Test Case #{}: {}".format(index + 1, testCase))
        print("    First: {}".format(find_two_sum(*testCase)))
        print("    Count: {}".format(count_pairs(*testCase)))
        print("    Other: {}".format(count_pairs_distinct_unordered(*testCase)))