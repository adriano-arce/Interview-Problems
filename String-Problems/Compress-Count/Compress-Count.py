def compress_count(s):
    if not s:
        return s
    compressed = []
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        # ASSERT: s[i:j] is a run.
        compressed.append(s[i])
        compressed.append(str(j - i))
        i = j
    return min(s, "".join(compressed), key=len)


def decompress_count(s):
    if not s or len(s) < 2 or not s[1].isdigit():
        return s
    # ASSERT: s really needs to be decompressed.
    decompressed = []
    i = 0
    while i < len(s):
        j = i + 1
        while j < len(s) and s[j].isdigit():
            j += 1
        # ASSERT: s[i+1 : j] can be converted to an integer.
        count = int(s[i+1 : j])
        for __ in range(count):
            decompressed.append(s[i])
        i = j
    return "".join(decompressed)


if __name__ == "__main__":
    test_strings = [
        "aabcccccaaa",
        "",
        "p",
        "pq",
        None,
        "abcde",
        "bbbc",
        "bbbcc",
        "aaaaaaaaaaaaabbbbccc"
    ]
    for index, test_string in enumerate(test_strings):
        compressed = compress_count(test_string)
        decompressed = decompress_count(compressed)
        print("Test Case #{}: {} -> {} -> {}".format(
            index + 1, repr(test_string), repr(compressed), repr(decompressed)
        ))