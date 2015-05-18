def is_balanced(s):
    """
    Returns True iff all types of brackets in s are balanced.
    """

    bracket_dict = {"(": ")", "[": "]", "{": "}"}
    right_bracket_set = {")", "]", "}"}
    right_bracket_stack = []
    for char in s:
        # If char is a left bracket, then add it to the stack.
        right_bracket = bracket_dict.get(char)
        if right_bracket:
            right_bracket_stack.append(right_bracket)
        # If char is a right bracket, then try popping it from the stack.
        elif char in right_bracket_set:
            if right_bracket_stack and char == right_bracket_stack[-1]:
                right_bracket_stack.pop()
            else:
                return False
    return not right_bracket_stack


if __name__ == "__main__":
    testStrings = [
        "(2 + y) - e^{2x + 3} * [7x] / [sin(2e^{7x})]",
        "5(2 + x]",
        "4)x + 3(",
        "[[[(({})[])]]{()}]"
    ]
    for (index, s) in enumerate(testStrings):
        print("Test String #{}:".format(index + 1))
        print("{} {} balanced.".format(
            repr(s), "is" if is_balanced(s) else "is not"
        ))