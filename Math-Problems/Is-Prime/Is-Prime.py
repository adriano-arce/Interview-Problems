import math


def is_prime(n):
    #---------------------------------------------------------------------------
    # Method 1: The naive way.
    #---------------------------------------------------------------------------
    # mid = int(math.sqrt(n))
    # for i in range(2, mid + 1):
    #     if n % i == 0:
    #         return False
    # return True

    #---------------------------------------------------------------------------
    # Method 2: Skip by 6's.
    #---------------------------------------------------------------------------
    # if n in {2, 3}:
    #     return True
    # if n % 2 == 0 or n % 3 == 0:
    #     return False
    # mid = int(math.sqrt(n))
    # for i in range(7, mid + 1, 6):
    #     if n % (i - 2) == 0 or n % i == 0:
    #         return False
    # return True

    #---------------------------------------------------------------------------
    # Method 3: Miller-Rabin.
    #---------------------------------------------------------------------------
    if n == 2:
        print("  2 is the only even prime.")
        return True
    if n % 2 == 0:
        print("  {} > 2 is even.".format(n))
        return False
    bases = [2, 7, 61]  # Works for all n < 4759123141.
    for b in bases:
        if is_definitely_composite(n, b):
            return False
    return True


def is_definitely_composite(n, b):
    """
    Let n = d*2^s + 1 for some odd d. If b^d != 1 (mod n) and b^{d*2^r} != n - 1
    (mod n) for all r in [0, s), then n is definitely composite. Otherwise, n is
    probably prime.
    """
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    m = pow(b, d, n)
    if m == 1:
        print("  Prime? {}^{} mod {} = 1.".format(b, d, n))
        return False
    for r in range(s):
        if m == n - 1:
            print("  Prime? {}^({}*2^{}) mod {} = {}.".format(b, d, r, n, m))
            return False
        m = (m * m) % n
    print("  Using {}, {} is definitely composite.".format(b, n))
    return True


def main():
    test_nums = [
        2, 12, 25, 91, 97, 2047, 314821, 2 ** 31 - 3, 2 ** 31 - 1
    ]
    for i, n in enumerate(test_nums):
        print("Test Case #{}:".format(i + 1))
        prime = "is" if is_prime(n) else "is not"
        print("    {} {} prime.".format(n, prime))

if __name__ == "__main__":
    main()