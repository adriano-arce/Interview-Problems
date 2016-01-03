def all_routes(cities, i=0):
    """Return all possible routes, where cities[i:] have been permuted.

    Args:
        cities (list of string):
            The cities that make up each route.

        i (int, optional):
            The starting index of the subarray of cities to be permuted.

    Returns:
        list of tuple of string: The list of all possible routes.
    """
    # Base Case: Routes should be immutable tuples, not mutable lists.
    if i >= len(cities) - 1:
        return [tuple(cities)]

    # Inductive Step: Swap in each possible starting city.
    routes = []
    for j in range(i, len(cities)):
        cities[i], cities[j] = cities[j], cities[i]
        routes.extend(all_routes(cities, i + 1))
        cities[i], cities[j] = cities[j], cities[i]

    return routes


def traverse(route, distances):
    return sum(distances[route[i]][route[i + 1]] for i in range(len(route) - 1))


def main():
    with open('input.txt', 'r') as f:
        rows = f.read().split('\n')

    distances = {}
    for row in rows:
        start, _, end, _, dist = row.split()
        if start in distances:
            distances[start][end] = int(dist)
        else:
            distances[start] = {end: int(dist)}
        if end in distances:
            distances[end][start] = int(dist)
        else:
            distances[end] = {start: int(dist)}

    routes = all_routes(list(distances))

    min_dist = min(traverse(route, distances) for route in routes)
    print('The distance of the shortest route is: %d.' % min_dist)

    max_dist = max(traverse(route, distances) for route in routes)
    print('The distance of the longest route is: %d.' % max_dist)


if __name__ == '__main__':
    main()
