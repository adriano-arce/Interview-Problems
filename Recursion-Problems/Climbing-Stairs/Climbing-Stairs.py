def climbing_stairs(n):
    """
    Returns a list of each way to climb n steps, where we can take either 1 step
    or 2 steps at a time.

    Intuition:
        The last leap can either be 1 step or 2 steps. This yields a recurrence
        relation that yields the Fibonacci numbers.
    """
    prev, curr = [[]], [[1]]
    if n == 0:
        return prev
    if n == 1:
        return curr
    for i in range(n - 1):
        prev, curr = curr, take_step(prev, 2) + take_step(curr, 1)
    return curr


def take_step(solutions, step):
    """
    Takes a step for each solution.
    """
    return [solution + [step] for solution in solutions]


def main():
    test_n = [
        0, 1, 2, 3, 4, 5, 6
    ]
    for i, n in enumerate(test_n):
        print("Test Case #{}:".format(i + 1))
        text = [str(n)]
        for solution in climbing_stairs(n):
            text.append(" + ".join(map(str, solution)))
        print("\n= ".join(text))
if __name__ == "__main__":
    main()