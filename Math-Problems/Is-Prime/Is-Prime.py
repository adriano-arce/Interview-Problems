import math
import sys, os


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
    bases = [2, 7, 61]  # Works for all n < 4759123141.
    if n in bases:
        print("  {} is one of the base primes.".format(n))
        return True

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


def get_all_primes(n):
    """
    Returns a list of all primes 2 <= p <= n.
    """
    #---------------------------------------------------------------------------
    # Method 1: Reuse the is_prime() function.
    #---------------------------------------------------------------------------
    # primes = []
    # for i in range(2, n + 1):
    #     if is_prime(i):
    #         primes.append(i)
    # return primes

    #---------------------------------------------------------------------------
    # Method 2: Use the Sieve of Eratosthenes.
    #---------------------------------------------------------------------------
    i_is_prime = [True] * (n + 1)
    i_is_prime[0], i_is_prime[1] = False, False
    mid = int(math.sqrt(n))
    for i in range(2, mid + 1):
        if i_is_prime[i]:
            for j in range(i*i, n + 1, i):
                i_is_prime[j] = False
    return [i for i in range(n + 1) if i_is_prime[i]]


def main():
    test_nums = [
        2, 12, 25, 61, 91, 97, 2047, 314821, 2 ** 31 - 3, 2 ** 31 - 1
    ]
    for i, n in enumerate(test_nums):
        print("Test Case #{}:".format(i + 1))
        prime = "is" if is_prime(n) else "is not"
        print("    {} {} prime.".format(n, prime))

    n = 229
    print(get_all_primes(n))
    with open(os.devnull, "w") as devnull:
        old_stdout, sys.stdout = sys.stdout, devnull
        rabin_miller_primes = [i for i in range(2, n + 1) if is_prime(i)]
    sys.stdout = old_stdout
    print(rabin_miller_primes)

if __name__ == "__main__":
    main()