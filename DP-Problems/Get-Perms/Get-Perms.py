def get_perms(s):
    """
    Returns all (len(s))! permutations of s.
    """
    return get_prefixed_perms(list(s), 0)


def get_prefixed_perms(s, i):
    """
    Returns all (len(s) - i)! permutations t of s such that t[:i] = s[:i].
    """
    # Base Case: 0! = 1! = 1.
    # Store the only permutation as an immutable string, not a mutable list.
    if i >= len(s) - 1:
        return ["".join(s)]

    # Inductive Step: (len(s) - i)! = (len(s) - i) * (len(s) - i - 1)!
    # Swap in each suffix character to be at the beginning of the suffix.
    prefixed_perms = get_prefixed_perms(s, i + 1)
    for j in range(i + 1, len(s)):
        s[i], s[j] = s[j], s[i]
        prefixed_perms.extend(get_prefixed_perms(s, i + 1))
        s[i], s[j] = s[j], s[i]
    return prefixed_perms


def main():
    test_strs = [
        "", "a", "qw", "abc", "1234"
    ]
    for i, s in enumerate(test_strs):
        print("Test Case #{}: {}".format(i + 1, repr(s)))
        print(get_perms(s))

if __name__ == "__main__":
    main()