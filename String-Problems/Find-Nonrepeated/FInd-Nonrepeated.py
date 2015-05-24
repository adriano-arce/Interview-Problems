def find_nonrepeated(s):
    """
    Returns the first nonrepeated character in s (or None if it doesn't exist).
    """
    char_dict = {}
    for char in s:
        char_dict[char] = char_dict.get(char, 0) + 1
    for char in s:
        if char_dict[char] < 2:
            return char
    return None


if __name__ == "__main__":
    testStrings = [
        "hello! hello.",
        "abcdcbad",
        "teeter"
    ]
    for (index, s) in enumerate(testStrings):
        print("Test String #{}:".format(index + 1))
        print("The first non repeated char in {} is {}.".format(
            repr(s), find_nonrepeated(s)
        ))