def isPalindrome(s):
    """
    Returns true iff the string s is a palindrome.
    """
    # Compare the first half of s with the last half.
    # If len(s) is odd, there is no need to look at the middle char.
    # NOTE: Unlike '/', the '//' operator performs floor division.
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - 1 - i]:
            return False
    return True

if __name__ == "__main__":
    testStrings = [
        "",
        "#$%^%$#",
        "ricecar",
        "racecar",
        "abba",
        "12344391"
    ]
    for (index, s) in enumerate(testStrings):
        print(str.format("Test String #{0}:", index + 1))
        print(str.format("'{0}' {1} a palindrome.",
                         s, "is" if isPalindrome(s) else "is not"))
