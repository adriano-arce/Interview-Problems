def part_one(s):
    segments = []
    i = 0
    while i < len(s):
        left = s.find('(', i)
        if left == -1:
            segments.append(s[i:])
            break
        else:
            segments.append(s[i:left])

        mid = s.find('x', left + 2)
        right = s.find(')', mid + 2)

        offset, rep = int(s[left+1:mid]), int(s[mid+1:right])
        data = s[right+1:right+1+offset]
        segments.append(data * rep)

        i = right + 1 + offset

    decompressed = ''.join(segments)
    print('The total decompressed length is: %d' % len(decompressed))
    return decompressed


def part_two(s, tab=0):
    length = 0
    i = 0
    while i < len(s):
        left = s.find('(', i)
        if left == -1:
            length += len(s[i:])
            break
        else:
            length += len(s[i:left])

        mid = s.find('x', left + 2)
        right = s.find(')', mid + 2)

        offset, rep = int(s[left+1:mid]), int(s[mid+1:right])
        data = s[right+1:right+1+offset]
        length += part_two(data, tab + 1) * rep

        i = right + 1 + offset

    print('%sNew unzip length from %d to %d.' % ('  '*tab, len(s), length))
    return length


def main():
    with open('input.txt', 'r') as f:
        compressed = f.read()

    decompressed = part_one(compressed)
    part_two(decompressed)

if __name__ == '__main__':
    main()
