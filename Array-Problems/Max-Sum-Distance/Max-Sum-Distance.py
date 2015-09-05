def max_sum_distance(arr):
    """
    Computes M = max{arr[i] + arr[j] + (j - i) | 0 <= i < j <= n}.

    Intuition:
        Maximizing the separable bivariate objective function is equivalent to
        maximizing two univariate objective functions: just rewrite!
            M = max{arr[i] - i} + max{arr[j] + j}
    """
    n = len(arr)
    diff_part = max(arr[i] - i for i in range(n))
    sum_part = max(arr[j] + j for j in range(n))
    return diff_part + sum_part


if __name__ == "__main__":
    testCases = [
        [8, 2, 4, 9, 5, 8, 0, 3, 8, 2],
        [-5, -3, 2, 3, 1, 2, 5, 6],
        [100000],
        [1, 0, 0, 0, 2, 0, 0, 0, 1]
    ]
    for (index, testCase) in enumerate(testCases):
        print("Test Case #{}: {}".format(index + 1, testCase))
        print("    {}".format(max_sum_distance(testCase)))