class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def add_two_nums(head1, head2):
    tail = Node(1)
    head_sum = Node(2, tail)
    return head_sum


def print_num(head):
    ptr = head
    digits = []
    while ptr:
        digits.append(ptr.data)
        ptr = ptr.next_node
    print(digits)
    print("".join(map(str, reversed(digits))))

if __name__ == "__main__":
    testHeadPairs = []

    case1node5 = Node(5)
    case1node4 = Node(4, case1node5)
    case1node3 = Node(3, case1node4)
    case1head2 = Node(2, case1node3)
    case1head1 = Node(1, case1head2)
    testHeadPairs.append((case1head1, case1head2))

    case2node1 = Node(1, case1node3)
    case2head1 = Node(0, case2node1)
    testHeadPairs.append((case2head1, case1head2))

    case3node5 = Node(5)
    case3node4 = Node(4, case3node5)
    case3node3 = Node(3, case3node4)
    case3head1 = Node(2, case3node3)
    testHeadPairs.append((case3head1, case1head2))

    for (index, headPair) in enumerate(testHeadPairs):
        print("Test Pair #{}:".format(index + 1))
        print_num(add_two_nums(*headPair))