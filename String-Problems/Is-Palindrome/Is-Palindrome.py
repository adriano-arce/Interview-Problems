from string import punctuation


def is_palindrome(s):
    """
    Returns true iff the string s is a palindrome.
    Clarification to ask the interviewer:
    - Are whitespace, punctuation, and case considered important?
    - For this function, we assume that they are NOT important.
    """

    # Strip out all whitespace and punctuation, and ignore case.
    no_space_chars = list("".join(s.split()))
    no_punc_chars = [char for char in no_space_chars if char not in punctuation]
    stripped = "".join(no_punc_chars).lower()

    # Compare the first half of newS with the last half and return false
    # if any pair doesn't match. If len(newS) is odd, there is no need to look
    # at the middle character.
    # NOTE: Unlike '/', the '//' operator performs floor division.

    #---------------------------------------------------------------------------
    # Solution 1: Imperative.
    #---------------------------------------------------------------------------
    #    for i in range(len(stripped) // 2):
    #        if stripped[i] != stripped[len(stripped) - 1 - i]:
    #            return False
    #    return True
    #---------------------------------------------------------------------------
    # Solution 2: Declarative (negated quantifiers).
    #---------------------------------------------------------------------------
    #    return not any([stripped[i] != stripped[len(stripped) - 1 - i]
    #                    for i in range(len(stripped) // 2)])
    #---------------------------------------------------------------------------
    ## Solution 3: Declarative (normal quantifiers).
    #---------------------------------------------------------------------------
    return all([stripped[i] == stripped[len(stripped) - 1 - i]
                for i in range(len(stripped) // 2)])


if __name__ == "__main__":
    testStrings = [
        "",
        "#$%^%$#",
        "rAcecar",
        "racecar",
        "ricecar",
        "abba",
        "12344329",
        "a@@#  b C \n\t d Eedc b  A",
        "a@@#  b C \n\t d Eedc b  z",
        "A man, a plan, a canal, Panama!"
    ]
    for (index, s) in enumerate(testStrings):
        print(str.format("Test String #{0}:", index + 1))
        print(str.format("{0} {1} a palindrome.",
                         repr(s), "is" if is_palindrome(s) else "is not"))