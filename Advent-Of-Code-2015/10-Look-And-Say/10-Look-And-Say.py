def look_and_say(s):
    output = []
    i = 0
    while i < len(s):
        # Find a run of the form s[i:j] of length j - i > 0.
        j = i + 1
        while j < len(s) and s[j] == s[i]:
            j += 1
        output.append(str(j - i))
        output.append(s[i])
        i = j
    return ''.join(output)


def main():
    seed = '1113122113'

    for i in range(40):
        seed = look_and_say(seed)
    print('After 40 iterations, the result has length %s.' % len(seed))

    for i in range(10):
        seed = look_and_say(seed)
    print('After 50 iterations, the result has length %s.' % len(seed))

if __name__ == '__main__':
    main()