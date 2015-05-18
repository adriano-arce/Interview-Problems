def is_permutation(s, t):
    """
    Returns True iff s is a permutation of t.

    Clarifications to ask the interviewer:
    - How are the strings encoded? ASCII? Unicode?
    - What kinds of characters are used? Alphanumeric? Punctuation?

    Here, we assume that all strings are encoded with ASCII (256 chars). Recall
    that the ord() function takes as input an 8-bit ASCII string of length one
    and returns the integer value of the byte in [0, 255]. Otherwise, if the
    string is encoded with Unicode (2^16 = 65536 chars), then the ord() function
    will return the integer representing the Unicode code point of the character
    in [0, 65535].
    """

    #---------------------------------------------------------------------------
    # Algorithm 1: Cross off matching characters from strings.
    #              O(n^2) time, O(n) space.
    #---------------------------------------------------------------------------
    # Algorithm 2: Sort both strings and compare one-by-one.
    #              O(n log n) time, O(n) space.
    #---------------------------------------------------------------------------
    # Algorithm 3: Compare character counts (implemented below).
    #              O(n) time, O(n) space.
    #---------------------------------------------------------------------------

    MAX_CHARS = 256
    char_counts = [0] * MAX_CHARS
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
        ("abc123^&*", "a1^cb2&*3"),
        ("stackoverflaw", "overflowstack"),
        ("!!?!", "!?!")
    ]
    for (index, pair) in enumerate(testStringPairs):
        s, t = pair
        print("Test String #{}:".format(index + 1))
        print("{} {} a permutation of {}.".format(
            repr(s), "is" if is_permutation(s, t) else "is not", repr(t)
        ))