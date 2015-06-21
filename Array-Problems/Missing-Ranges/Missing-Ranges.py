def missing_ranges(nums):
    LOW, HIGH = 0, 100
    nums.append(HIGH)
    ranges = []
    low = LOW
    for num in nums:
        if num == low + 1:
            ranges.append(str(num - 1))
        elif num > low + 1:
            ranges.append("{}->{}".format(low, num - 1))
        low = num + 1
    return ranges

if __name__ == "__main__":
    test_arrs = [
        [0, 1, 3, 50, 75],
        [20, 37, 55],
        [],
        list(range(100)),
        list(range(0, 100, 2))
    ]
    for index, test_arr in enumerate(test_arrs):
        print("Test Case #{}: {}".format(index + 1, missing_ranges(test_arr)))