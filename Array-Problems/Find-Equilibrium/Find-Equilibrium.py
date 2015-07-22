def find_equilibrium(arr):
    left_sum = 0
    right_sum = sum(arr[1:])  # List slicing copies references to each value.
    if left_sum == right_sum and arr:  # Don't return 0 if arr is empty.
        return 0
    for i in range(1, len(arr)):
        left_sum += arr[i - 1]
        right_sum -= arr[i]
        if left_sum == right_sum:
            return i
    return -1


def main():
    test_arrs = [
        [],
        [-7, 1, 5, 2, -4, 3, 0],
        [1, 2, 3, 4, 5],
        [3, 1, 2, 9, 4, 2],
        [9, 2, -3, 1],
        [7, 6, -5, -8, 9]
    ]
    for i, test_arr in enumerate(test_arrs):
        print("Test Case #{}: {}".format(i + 1, test_arr))
        print("    Equilibrium Index: {}".format(find_equilibrium(test_arr)))

if __name__ == "__main__":
    main()