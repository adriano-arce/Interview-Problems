import hashlib


def part_one(door_id):
    print('Starting part one...')
    password = ['_'] * 8
    index = 0
    for i in range(len(password)):
        print('  [%7d] Password so far: %s' % (index, ''.join(password)))
        h = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
        index += 1
        while h[:5] != '00000':
            h = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
            index += 1
        password[i] = h[5]

    print('The part one password is: %s.' % ''.join(password))


def part_two(door_id):
    print('Starting part two...')
    password = ['_'] * 8
    index = 0
    for i in range(len(password)):
        print('  [%8d] Password so far: %s' % (index, ''.join(password)))
        h = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
        index += 1
        while (h[:5] != '00000' or h[5] not in '01234567'
               or password[int(h[5])] != '_'):
            h = hashlib.md5((door_id + str(index)).encode('utf-8')).hexdigest()
            index += 1
        password[int(h[5])] = h[6]

    print('The part two password is: %s.' % ''.join(password))


def main():
    door_id = 'abbhdwsy'
    part_one(door_id)
    part_two(door_id)

if __name__ == '__main__':
    main()
