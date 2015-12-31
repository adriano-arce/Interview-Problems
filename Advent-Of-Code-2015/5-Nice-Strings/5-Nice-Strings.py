import re


def old_is_nice(s):
    # Must contain at least 3 vowels.
    if sum(c in 'aeiou' for c in s) < 3:
        return False

    # Must have a double letter.
    #
    # Remark: Fancier methods include...
    # - Using a regex: r'(.)\1'
    # - Using a groupby: groupby(s)
    has_double = False
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            has_double = True
    if not has_double:
        return False

    # Must not contain blacklisted substrings.
    for bad_substring in ('ab', 'cd', 'pq', 'xy'):
        if bad_substring in s:
            return False

    return True


def new_is_nice(s):
    # Must contain a pair of 2 letters that appear twice without overlapping.
    pair_regex = re.compile(r'(..).*\1')
    if not pair_regex.search(s):
        return False

    # Must contain a letter which repeats with exactly one letter between them.
    between_regex = re.compile(r'(.).\1')
    if not between_regex.search(s):
        return False

    return True


def main():
    with open('input.txt', 'r') as f:
        strings = f.read().split('\n')

    new_nice_count = sum(old_is_nice(s) for s in strings)
    print('Before, there are %d nice strings.' % new_nice_count)

    new_nice_count = sum(new_is_nice(s) for s in strings)
    print('Now, there are %d nice strings.' % new_nice_count)

if __name__ == '__main__':
    main()