def main():
    with open('input.txt', 'r') as f:
        brackets = f.read()

    floor = 0
    position = -1
    for i, bracket in enumerate(brackets):
        if bracket == '(':
            floor += 1
        else:
            floor -= 1
        if position == -1 and floor == -1:
            position = i + 1

    print('Santa arrived at floor %d.' % floor)
    print('Santa first entered the basement at position %d.' % position)

if __name__ == '__main__':
    main()