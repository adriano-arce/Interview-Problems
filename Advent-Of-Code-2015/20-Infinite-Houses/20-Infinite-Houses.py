# from math import sqrt
#
# def is_prime(n):
#     bases = [2, 7, 61]  # Works for all n < 4759123141.
#     if n in bases:
#         return True
#
#     for b in bases:
#         if is_definitely_composite(n, b):
#             return False
#     return True
#
#
# def is_definitely_composite(n, b):
#     """
#     Let n = d*2^s + 1 for some odd d. If b^d != 1 (mod n) and b^{d*2^r} != n - 1
#     (mod n) for all r in [0, s), then n is definitely composite. Otherwise, n is
#     probably prime.
#     """
#     s, d = 0, n - 1
#     while d % 2 == 0:
#         s += 1
#         d //= 2
#     m = pow(b, d, n)
#     if m == 1:
#         return False
#     for r in range(s):
#         if m == n - 1:
#             return False
#         m = (m * m) % n
#     return True
#
#
# def factorize(n):
#     if is_prime(n):
#         return [n]
#
#     factors = []
#     while n % 2 == 0:
#         n >>= 1
#         factors.append(2)
#     if n == 1:
#         return factors
#
#     bound = sqrt(n) + 1
#     i = 3
#     while i < bound:
#         while n % i == 0:
#             n //= i
#             factors.append(i)
#             if n == 1:
#                 return factors
#             if is_prime(n):
#                 factors.append(n)
#                 return factors
#             i += 2
#     return []
#
#
# def min_house(bound):
#     for house in range(2, bound + 1):
#         total = 1
#         factors = factorize(house)
#         i = 0
#         while i < len(factors):
#             j = i
#             factor = 1
#             factor_sum = 1
#             while j < len(factors) and factors[j] == factors[i]:
#                 factor *= factors[i]
#                 factor_sum += factor
#                 j += 1
#
#             total *= factor_sum
#             i = j + 1
#
#         print(house, total)
#         if total >= bound:
#             return total
#     return None
#
#
# def main():
#     present_bound = 29000000
#     house = min_house(present_bound // 10)
#     print('The lowest house number is %d.' % house)
#
#
# if __name__ == '__main__':
#     main()
