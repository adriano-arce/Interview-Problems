from ast import literal_eval  # The inverse repr function.
import re  # Useful for chomping.


def inv_repr(s):
    return literal_eval(s)

    # chomp_regex = re.compile(r'(\\x[0-9a-f]{2}|\\\\|\\\"|.)')
    # match = chomp_regex.findall(s[1:-1])
    # return ''.join(match)  # Almost works. Could get length at least.

    # output = []
    # i = 1
    # while i < len(s) - 1:
    #     if s[i] == '\\':
    #         if s[i + 1] == '\\':
    #             c = '\\'
    #             i += 1
    #         elif s[i + 1] == '"':
    #             c = '"'
    #             i += 1
    #         elif s[i + 1] == 'x':
    #             c = chr(int(s[i + 2 : i + 4], 16))
    #             i += 3
    #         else:
    #             print('ERROR')
    #             c = ''
    #     else:
    #         c = s[i]
    #     output.append(c)
    #     i += 1
    # return ''.join(output)


def encode(s):
    output = s.replace('\\', '\\\\')
    output = output.replace('"', '\\"')
    return '"' + output + '"'


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    diff = sum(len(row) - len(inv_repr(row)) for row in rows)
    print('Original minus decoded is: %d.' % diff)

    diff = sum(len(encode(row)) - len(row) for row in rows)
    print('Encoded minus original is: %d.' % diff)

if __name__ == '__main__':
    main()