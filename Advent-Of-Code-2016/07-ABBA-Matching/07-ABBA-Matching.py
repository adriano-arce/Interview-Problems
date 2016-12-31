import re


def has_abba(s):
    for i in range(len(s) - 4 + 1):
        abba = s[i:i+4]
        if abba[0] == abba[3] and abba[1] == abba[2] and abba[0] != abba[1]:
            return True
    return False


def part_one(rows):
    hypernet_regex = re.compile(r'\[([a-z]+)\]')
    delimiter = ','
    tls_ips = []
    parsed_rows = []
    for row in rows:
        hypernets = hypernet_regex.findall(row)
        supernets = hypernet_regex.sub(delimiter, row).split(delimiter)
        if (all(not has_abba(hypernet) for hypernet in hypernets) and
                any(has_abba(supernet) for supernet in supernets)):
            tls_ips.append(row)
        parsed_rows.append((row, hypernets, supernets))

    print('There are a total of %d IPs that support TLS.' % len(tls_ips))
    return parsed_rows


def get_aba_set(s, reverse=False):
    aba_set = set()
    for i in range(len(s) - 3 + 1):
        aba = s[i:i+3]
        if aba[0] == aba[2] and aba[0] != aba[1]:
            a, b = aba[0], aba[1]
            if reverse:
                a, b = b, a
            aba_set.add((a, b))
    return aba_set


def part_two(parsed_rows):
    ssl_ips = []
    for ip, hypernets, supernets in parsed_rows:
        aba_set = set.union(*(get_aba_set(s) for s in supernets))
        bab_set = set.union(*(get_aba_set(h, True) for h in hypernets))
        if aba_set.intersection(bab_set):
            ssl_ips.append(ip)

    print('There are a total of %d IPs that support SSL.' % len(ssl_ips))


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    parsed_rows = part_one(rows)
    part_two(parsed_rows)

if __name__ == '__main__':
    main()
