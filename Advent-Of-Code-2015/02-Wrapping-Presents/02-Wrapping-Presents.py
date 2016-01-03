def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    total_paper = 0
    total_ribbon = 0
    for row in rows:
        l, w, h = (int(d) for d in row.split('x'))
        faces = l * w, w * h, h * l
        total_paper += 2 * sum(faces) + min(faces)

        sorted_dimensions = sorted((l, w, h))
        total_ribbon += 2 * sum(sorted_dimensions[:2]) + l * w * h

    print('Total required paper: %d square feet.' % total_paper)
    print('Total required ribbon: %d feet.' % total_ribbon)


if __name__ == '__main__':
    main()
