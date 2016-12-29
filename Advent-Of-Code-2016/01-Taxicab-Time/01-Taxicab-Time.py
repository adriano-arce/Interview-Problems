def main():
    with open('input.txt', 'r') as f:
        instructions = f.read().split(', ')

    previous_locations = {(0, 0)}
    target_location = None

    # Start from North, clockwise.
    directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
    curr_dir = 0

    x, y = 0, 0
    for instruction in instructions:
        orientation = instruction[0]
        steps = int(instruction[1:])

        if orientation == 'R':
            curr_dir += 1
        else:
            curr_dir -= 1
        curr_dir %= len(directions)

        dx, dy = directions[curr_dir]
        for step in range(steps):
            x += dx
            y += dy
            if not target_location and (x, y) in previous_locations:
                target_location = x, y
            else:
                previous_locations.add((x, y))

    taxicab_distance = x + y
    print('Easter Bunny HQ is %d blocks away.' % taxicab_distance)
    print('...actually, HQ is %d blocks away.' % sum(target_location))

if __name__ == '__main__':
    main()
