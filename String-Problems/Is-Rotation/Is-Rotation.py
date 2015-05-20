def is_rotation(s, t):
    """
    Returns True iff s is a rotated version of t.
    """
    return len(s) == len(t) and s in t + t

if __name__ == "__main__":
    testStringPairs = [
        ("", ""),
        ("stackoverflow", "flowstackover"),
        ("12345", "5xy1234"),
        ("stackoverflaw", "overflowstack")
    ]
    for (index, pair) in enumerate(testStringPairs):
        s, t = pair
        print("Test String #{}:".format(index + 1))
        print("{} {} a rotated version of {}.".format(
            repr(s), "is" if is_rotation(s, t) else "is not", repr(t)
        ))