import re


def is_valid(s):
    # Must have a straight.
    has_straight = False
    for i in range(len(s) - 2):
        low, mid, high = ord(s[i]), ord(s[i + 1]), ord(s[i + 2])
        if high - mid == 1 and mid - low == 1:
            has_straight = True
            break
    if not has_straight:
        return False

    # Must not contain blacklisted letters.
    if 'i' in s or 'o' in s or 'l' in s:
        return False

    # Must contain two different non-overlapping pairs.
    pair_regex = re.compile(r'(.)\1')
    match = pair_regex.findall(s)
    has_pairs = match and len(set(match)) >= 2
    if not has_pairs:
        return False

    return True


def increment(password):
    nums = [ord(c) - ord('a') for c in password]
    for i in range(len(nums) - 1, -1, -1):
        nums[i] += 1
        if nums[i] == 26:
            nums[i] = 0
        else:
            break
    next_password = ''.join(chr(ord('a') + num) for num in nums)

    # Optimization for blacklisted characters.
    for bad_char in list('iol'):
        i = next_password.find(bad_char)
        if i > -1:
            next_char = chr(ord(bad_char) + 1)
            suffix_len = len(next_password) - (i + 1)
            next_password = next_password[:i] + next_char + ('a' * suffix_len)

    return next_password


def find_next_valid(password):
    password = increment(password)
    while not is_valid(password):
        password = increment(password)
    return password


def main():
    password = 'hxbxwxba'
    password = find_next_valid(password)
    print('Santa\'s next password is: %s.' % password)

    password = find_next_valid(password)
    print('After expiring again, Santa\'s next password is: %s.' % password)


if __name__ == '__main__':
    main()
