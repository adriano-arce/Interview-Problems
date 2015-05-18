def is_permutation(s, t):
    """
    Returns True iff s is a permutation of t.

    Clarifications for interviewer:
    - How are the strings encoded? ASCII? Unicode?
    - What kinds of characters are used? Alphanumeric? Punctuation?

    Here, we assume that all strings are encoded with ASCII (256 chars).
    """

    #---------------------------------------------------------------------------
    # Algorithm 1: Cross off matching characters from strings.
    #              O(n^2) time, O(n) space.
    # Algorithm 2: Sort both strings and compare one-by-one.
    #              O(n log n) time, O(n) space.
    # Algorithm 3: Compare character counts (implemented below).
    #              O(n) time, O(n) space.
    #---------------------------------------------------------------------------

    char_counts = [0] * 256
    for c in s:
        char_counts[ord(c)] += 1
    for c in t:
        char_counts[ord(c)] -= 1
    return not any(char_counts)  # True iff all zeroes.

if __name__ == "__main__":
    testStringPairs = [
        ("", ""),
        ("stackoverflow", "flowstackover"),
        ("12345", "5xy1234"),
        ("stackoverflaw", "overflowstack"),
        ("!!?!", "!?!")
    ]
    for (index, pair) in enumerate(testStringPairs):
        s, t = pair
        print("Test String #{}:".format(index + 1))
        print("{} {} a permutation of {}.".format(
            repr(s), "is" if is_permutation(s, t) else "is not", repr(t)
        ))