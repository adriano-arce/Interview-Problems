class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


def add_recurse(head1, head2, carry):
    """
    Recursively adds the two given numbers with carry.
    """
    # Base Cases: Both heads are None.
    if not head1 and not head2:
        if carry:
            return Node(carry)
        return None

    # Recursive Step: Add the heads and recurse on the tails.
    BASE = 10
    digit1 = head1.data if head1 else 0
    digit2 = head2.data if head2 else 0
    next1 = head1.next_node if head1 else None
    next2 = head2.next_node if head2 else None
    carry, digit = divmod(digit1 + digit2 + carry, BASE)
    tail = add_recurse(next1, next2, carry)
    return Node(digit, tail)


def add_two_nums(head1, head2):
    """
    Adds the two given numbers (stored as linked lists).
    """
    #---------------------------------------------------------------------------
    # Solution 1: Iteration.
    #---------------------------------------------------------------------------
    # BASE = 10
    # head = None
    # prev, tail = None, head
    # carry = 0
    # ptr1, ptr2 = head1, head2
    # while ptr1 or ptr2:
    #     # Add the digits and extend the linked list.
    #     digit1 = ptr1.data if ptr1 else 0
    #     digit2 = ptr2.data if ptr2 else 0
    #     carry, digit = divmod(digit1 + digit2 + carry, BASE)
    #     tail = Node(digit)
    #     if head:  # A previous node exists.
    #         prev.next_node = tail
    #     else:  # This is the first node.
    #         head = tail
    #
    #     # Update for the next iteration.
    #     prev = tail
    #     if ptr1:
    #         ptr1 = ptr1.next_node
    #     if ptr2:
    #         ptr2 = ptr2.next_node
    # if carry:
    #     tail = Node(carry)
    #     prev.next_node = tail  # prev must exist if carry is nonzero
    #
    # return head
    #---------------------------------------------------------------------------
    # Solution 2: Recursion.
    #---------------------------------------------------------------------------
    return add_recurse(head1, head2, 0)


def print_num(head):
    """
    Prints the number corresponding to the given linked list.
    """
    ptr = head
    digits = []
    while ptr:
        digits.append(ptr.data)
        ptr = ptr.next_node
    print("".join(map(str, reversed(digits))))


def python_2_linked(python_list):
    """
    Converts the given Python list into a linked list.
    """
    head = None
    for i in range(len(python_list) - 1, -1, -1):
        head = Node(python_list[i], head)
    return head


if __name__ == "__main__":
    testHeadPairs = [
        (python_2_linked([2, 1]), python_2_linked([4, 3])),
        (python_2_linked([5]), python_2_linked([7])),
        (python_2_linked([9, 8, 7]), python_2_linked([8, 7, 6])),
        (python_2_linked([1]), python_2_linked([9, 9, 9, 9])),
        (python_2_linked([0, 0, 0, 1]), python_2_linked([2]))
    ]
    for (index, headPair) in enumerate(testHeadPairs):
        print("Test Pair #{}:".format(index + 1))
        print_num(add_two_nums(*headPair))