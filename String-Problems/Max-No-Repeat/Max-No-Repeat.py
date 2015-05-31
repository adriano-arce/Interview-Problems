def max_no_repeat(s):
    """
    Returns the first longest substring of s containing no repeated characters.
    """
    max_start = -1
    max_end = -1
    max_len = -1
    char_set = set()  # {} initializes an empty dict instead of an empty set.
    curr_start = 0
    for curr_end in range(len(s)):
        char = s[curr_end]
        if char in char_set:
            curr_len = curr_end - curr_start
            if curr_len > max_len:
                max_start, max_end, max_len = curr_start, curr_end, curr_len

            # Throw out the characters that came before the match.
            while s[curr_start] != char:
                char_set.remove(s[curr_start])
                curr_start += 1
            curr_start += 1
        else:
            char_set.add(char)
    curr_len = len(s) - curr_start
    if curr_len > max_len:
        max_start, max_end, max_len = curr_start, len(s), curr_len

    return s[max_start:max_end]


if __name__ == "__main__":
    testStrings = [
        "hello! hello.",
        "abcdcbad",
        "permutation",
        "",
        "bananaphone",
        "12324523445125345345"
    ]
    for (index, s) in enumerate(testStrings):
        print("Test String #{}:".format(index + 1))
        print("max_no_repeat({}) = {}".format(
            repr(s), repr(max_no_repeat(s))
        ))