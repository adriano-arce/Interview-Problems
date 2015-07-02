class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    @staticmethod
    def list_to_LL(L):
        """
        Converts the given Python list into a linked list.
        """
        head = None
        for i in range(len(L) - 1, -1, -1):
            head = Node(L[i], head)
        return head


def print_list(head):
    """
    Prints the number corresponding to the given linked list.
    """
    ptr = head
    nums = []
    while ptr:
        nums.append(ptr.data)
        ptr = ptr.next_node
    print("[" + ", ".join(map(str, nums)) + "]")


def reverse_list(head):
    #---------------------------------------------------------------------------
    # Method 1: Recursive.
    #---------------------------------------------------------------------------
    if head:
        new_head = reverse_list(head.next_node)
        # Right now, head.next_node is the tail of the sublist.
        # We need the sublist's tail to be the (old) head instead.
        if new_head:
            head.next_node.next_node = head
            head.next_node = None
            return new_head
        return head  # Linked list is just one node.
    return None  # Linked list is empty.

    #---------------------------------------------------------------------------
    # Method 2: Tail recursive (the recursive call is at the end).
    # In languages other than Python, the compiler uses tail call optimization.
    # In the next recursive call, we can simply reuse the current stack frame.
    # It's also easy to convert this to iterative.
    #---------------------------------------------------------------------------

    #---------------------------------------------------------------------------
    # Method 3: Iterative.
    #---------------------------------------------------------------------------


if __name__ == "__main__":
    testHeads = [
        Node.list_to_LL([]),
        Node.list_to_LL([1]),
        Node.list_to_LL([1, 2]),
        Node.list_to_LL([1, 2, 3]),
        Node.list_to_LL([1, 2, 3, 4])
    ]

    for (index, head) in enumerate(testHeads):
        print("Test List #{}:".format(index + 1))
        print_list(head)
        head = reverse_list(head)
        print_list(head)