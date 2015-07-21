class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def find_merge(head1, head2):
    """
    Given the heads of two linked lists, returns the first node where they merge
    or None if no such node exists.

    INTUITION:
        If head1 and head2 happen to be equidistant from the merge node (that
        is, if both linked lists had equal length), then it's easy: just advance
        one-by-one until a match is found. Indeed, it would be easy if we could
        traverse both lists *backwards* from the tail. To reduce to this simpler
        problem, we adjust the head pointers until they are equidistant.
    """
    len1 = 0
    ptr1 = head1
    while ptr1:
        len1 += 1
        ptr1 = ptr1.next_node

    len2 = 0
    ptr2 = head2
    while ptr2:
        len2 += 1
        ptr2 = ptr2.next_node

    # Make each pointer equally far from the end.
    ptr1, ptr2 = head1, head2
    while len1 > len2:
        ptr1 = ptr1.next_node
        len1 -= 1
    while len2 > len1:
        ptr2 = ptr2.next_node
        len2 -= 1

    # Advance both pointers one-by-one until a match is found.
    while ptr1:
        if ptr1 == ptr2:
            return ptr1
        ptr1 = ptr1.next_node
        ptr2 = ptr2.next_node

    return None

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
        mergeNode = find_merge(*headPair)
        if mergeNode:
            print(mergeNode.data)
        else:
            print("No merge node detected.")