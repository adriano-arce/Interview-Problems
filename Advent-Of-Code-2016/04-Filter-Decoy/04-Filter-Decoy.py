import re


def part_one(rows):
    name_regex = re.compile(r"([a-z-]+)-(\d+)\[([a-z]+)\]")
    total = 0
    real_data = []
    for row in rows:
        match = name_regex.match(row)
        name, sector_id, checksum = match.groups()

        char_counts = {}
        for char in name:
            if char != '-':
                char_counts[char] = char_counts.get(char, 0) + 1
        sorted_chars = sorted(char_counts, key=lambda c: (-char_counts[c], c))

        if ''.join(sorted_chars[:5]) == checksum:
            total += int(sector_id)
            real_data.append((name, int(sector_id)))

    print('The sum of the sector IDs for the real rooms is: %d.' % total)
    return real_data


def part_two(real_data):
    print('The candidate decrypted names and sector IDs are:')
    for encrypted, sid in real_data:
        decrypted = ''.join(
            chr((ord(c) - ord('a') + sid) % 26 + ord('a')) if c != '-' else '-'
            for c in encrypted)

        if 'north' in decrypted:
            print('  (%s, %d)' % (decrypted, sid))


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    real_data = part_one(rows)
    part_two(real_data)

if __name__ == '__main__':
    main()
