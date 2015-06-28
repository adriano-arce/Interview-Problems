class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def python_2_linked(python_list):
    """
    Converts the given Python list into a linked list.
    """
    head = None
    for i in range(len(python_list) - 1, -1, -1):
        head = Node(python_list[i], head)
    return head


def print_list(head):
    """
    Prints the number corresponding to the given linked list.
    """
    ptr = head
    digits = []
    while ptr:
        digits.append(ptr.data)
        ptr = ptr.next_node
    print("".join(map(str, digits)))


def reverse_list(head):
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
    return None


if __name__ == "__main__":
    testHeads = [
        python_2_linked([1, 2, 3, 4])
    ]

    for (index, head) in enumerate(testHeads):
        print("Test List #{}:".format(index + 1))
        print_list(head)
        reverse_list(head)
        print_list(head)