from functools import partial, reduce
from typing import Dict


class Node(object):
    def __init__(self):
        self.dependencies = []
        self._value = None

    def value(self):
        return self._value


class Bot(Node):
    def value(self):
        if self._value is None:
            a, b = (d() for d in self.dependencies)
            if a < b:
                self._value = a, b
            else:
                self._value = b, a
        return super(Bot, self).value()


class Output(Node):
    def value(self):
        if self._value is None:
            self._value = self.dependencies[0]()
        return super(Output, self).value()


def update_node(nodes, node_type, node_id, func):
    factory = {'bot': Bot, 'output': Output}
    if node_id not in nodes[node_type]:
        nodes[node_type][node_id] = factory[node_type]()
    nodes[node_type][node_id].dependencies.append(func)


def part_one(instructions):
    nodes: Dict[str, Dict[int, Node]] = {'bot': {}, 'output': {}}
    for instruction in instructions:
        words = instruction.split()
        if words[0] == 'value':
            value, node_type, node_id = int(words[1]), words[4], int(words[5])

            def value_func(v=value):
                return v

            update_node(nodes, node_type, node_id, value_func)
        else:
            giver_type, giver_id = words[0], int(words[1])
            low_type, low_id = words[5], int(words[6])
            high_type, high_id = words[10], int(words[11])

            def giver_func(j, t=giver_type, i=giver_id):
                return nodes[t][i].value()[j]

            update_node(nodes, low_type, low_id, partial(giver_func, 0))
            update_node(nodes, high_type, high_id, partial(giver_func, 1))

    # for node_type in sorted(nodes):
    #     for node_id in sorted(nodes[node_type]):
    #         value = nodes[node_type][node_id].value()
    #         print('The value of %s %s is %s.' % (node_type, node_id, value))

    for bot_id, node in nodes['bot'].items():
        if node.value() == (17, 61):
            print('Bot %d is responsible for comparing 17 with 61.' % bot_id)

    return nodes


def part_two(nodes):
    node_values = (nodes['output'][output_id].value() for output_id in range(3))
    product = reduce(lambda x, y: x * y, node_values)
    print('The product of the first 3 outputs is: %d' % product)


def main():
    with open('input.txt', 'r') as f:
        instructions = f.read().split('\n')

    nodes = part_one(instructions)
    part_two(nodes)


if __name__ == '__main__':
    main()
