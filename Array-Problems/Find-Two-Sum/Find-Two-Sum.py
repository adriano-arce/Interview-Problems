def find_two_sum(arr, target):
    """
    Finds the two indices of some two integers in arr that sum to target, in
    sorted ascending order (or returns None if no such pair exists).
    """
    sum_dict = {}
    for (curr_idx, num) in enumerate(arr):
        if num in sum_dict:
            prev_idx = sum_dict[num]
            return prev_idx, curr_idx
        sum_dict[target - num] = curr_idx
    return None  # No such pair exists.


if __name__ == "__main__":
    testCases = [
        ([8, 5, 6, 7], 13),
        ([3, 9, 6, 2, 1, 5], 10),
        ([3, 4, 5, 6], 12)
    ]
    for (index, testCase) in enumerate(testCases):
        print("Test Case #{}:".format(index + 1))
        print(find_two_sum(*testCase))