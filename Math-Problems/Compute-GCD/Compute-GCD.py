def gcd(a, b):
    if a == 0 and b == 0:
        return None
    a, b = abs(a), abs(b)
    if a < b:
        a, b = b, a
    while b:
        a, b = b, a % b
    return a

def main():
    test_pairs = [
        (0, 7),
        (0, 0),
        (30, 42),
        (123456, 987654),
        (97, 65),
        (48, 36),
        (832040, 1346269)
    ]
    for i, pair in enumerate(test_pairs):
        print("Test Case #{}:".format(i + 1))
        print("  gcd{} = {}".format(pair, gcd(*pair)))

if __name__ == "__main__":
    main()