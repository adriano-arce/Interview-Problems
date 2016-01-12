def simulate(registers, instructions):
    i = 0
    while i < len(instructions):
        args = instructions[i].split()
        if args[0] == 'hlf':
            registers[args[1]] //= 2
            i += 1
        elif args[0] == 'tpl':
            registers[args[1]] *= 3
            i += 1
        elif args[0] == 'inc':
            registers[args[1]] += 1
            i += 1
        elif args[0] == 'jmp':
            sign = 1 if args[1][0] == '+' else -1
            i += sign * int(args[1][1:])
        elif args[0] == 'jie':
            if registers[args[1][:-1]] % 2 == 0:
                sign = 1 if args[2][0] == '+' else -1
                i += sign * int(args[2][1:])
            else:
                i += 1
        elif args[0] == 'jio':
            if registers[args[1][:-1]] == 1:
                sign = 1 if args[2][0] == '+' else -1
                i += sign * int(args[2][1:])
            else:
                i += 1
        else:
            print('Unrecognized instruction.')


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().strip().split('\n')

    registers = {'a': 0, 'b': 0}
    simulate(registers, rows)
    print('Starting both at 0, b ends up with: %d.' % registers['b'])

    registers = {'a': 1, 'b': 0}
    simulate(registers, rows)
    print('Starting a at 1, b ends up with: %d.' % registers['b'])


if __name__ == '__main__':
    main()
