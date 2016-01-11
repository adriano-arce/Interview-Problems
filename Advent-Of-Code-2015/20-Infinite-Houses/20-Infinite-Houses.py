def is_prime(n):
    bases = [2, 7, 61]  # Works for all n < 4759123141.
    if n in bases:
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
        return False
    for r in range(s):
        if m == n - 1:
            return False
        m = (m * m) % n
    return True


def factorize(n):
    factors = []
    while n % 2 == 0:
        n >>= 1
        factors.append(2)

    i = 3
    while n > 1:
        if is_prime(n):
            i = n

        while n % i == 0:
            n //= i
            factors.append(i)
        i += 2
    return factors


def min_house(bound):
    best_house = -1
    largest_total = -1
    for house in range(2, bound + 1):
        total = 1
        factors = factorize(house)
        i = 0
        while i < len(factors):
            j = i
            factor = 1
            factor_sum = 1
            while j < len(factors) and factors[j] == factors[i]:
                factor *= factors[i]
                factor_sum += factor
                j += 1

            total *= factor_sum
            i = j

        if house % 10000 == 0:
            print('[%d]: %d, %d' % (house, best_house, largest_total))
        if total > largest_total:
            largest_total, best_house = total, house
        if total >= bound:
            print('[%d]: %d, %d' % (house, best_house, largest_total))
            return house
    return -1


def all_factors(n):
    return set(factor
               for pair in ((i, n//i)
                            for i in range(1, int(n**0.5) + 1)
                            if n % i == 0)
               for factor in pair)


def new_min_house(present_bound):
    best_house = -1
    largest_total = -1
    for house in range(2, present_bound + 1):
        min_factor = house / 50
        total = sum(11*factor
                    for factor in all_factors(house)
                    if factor >= min_factor)

        if house % 10000 == 0:
            print('[%d]: %d, %d' % (house, best_house, largest_total))
        if total > largest_total:
            largest_total, best_house = total, house
        if total >= present_bound:
            print('[%d]: %d, %d' % (house, best_house, largest_total))
            return house
    return -1


def main():
    present_bound = 29000000

    # house = min_house(present_bound // 10)
    # print('The lowest house number is %d.' % house)

    house = new_min_house(present_bound)
    print('In the new version, the lowest house number is %d.' % house)

if __name__ == '__main__':
    main()
