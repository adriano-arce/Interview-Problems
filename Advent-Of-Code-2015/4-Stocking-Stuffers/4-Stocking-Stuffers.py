import hashlib


def find_suffix(length):
    required_prefix = '0' * length

    secret_key = 'bgvyzdsv'
    for suffix in range(int(1e10)):
        raw_input = secret_key + str(suffix)
        hash_input = raw_input.encode('utf8')

        hash_obj = hashlib.md5()
        hash_obj.update(hash_input)
        secure_hash = hash_obj.hexdigest()
        if secure_hash.startswith(required_prefix):
            print('For length %d, the lowest suffix is: %d.' % (length, suffix))
            return


def main():
    find_suffix(5)
    find_suffix(6)


if __name__ == '__main__':
    main()
