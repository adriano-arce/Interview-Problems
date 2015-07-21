class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        p = self
        nums = []
        while p:
            nums.append(p.data)
            p = p.next_node
        return "[" + ", ".join(map(str, nums)) + "]"

    @staticmethod
    def list_to_LL(L):
        """
        Converts the given Python list into a linked list.
        """
        head = None
        for i in range(len(L) - 1, -1, -1):
            head = Node(L[i], head)
        return head


def reverse_list(head):
    #---------------------------------------------------------------------------
    # Method 1: Recursive.
    #---------------------------------------------------------------------------
    # if head:
    #     new_head = reverse_list(head.next_node)
    #     # Right now, head.next_node is the tail of the sublist.
    #     # We need the sublist's tail to be the (old) head instead.
    #     if new_head:
    #         head.next_node.next_node = head
    #         head.next_node = None
    #         return new_head
    #     return head  # Linked list is just one node.
    # return None  # Linked list is empty.

    #---------------------------------------------------------------------------
    # Method 2: Tail recursive (the recursive call is at the end).
    #---------------------------------------------------------------------------
    # In languages other than Python, the compiler uses tail call optimization.
    # So for each recursive call, we can simply reuse the current stack frame.
    # It's also easy to convert tail recursive to iterative.
    #---------------------------------------------------------------------------
    # return tail_recurse(None, head)

    #---------------------------------------------------------------------------
    # Method 3: Iterative.
    #---------------------------------------------------------------------------
    prev = None
    while head:
        head.next_node, prev, head = prev, head, head.next_node
    return prev


def tail_recurse(prev, curr):
    """
    Using tail recursion, reverses the linked list starting at curr, then joins
    the end of this linked list to the linked list starting at prev.
    """
    if curr:
        new_curr = curr.next_node
        if new_curr:
            curr.next_node = prev
            return tail_recurse(curr, new_curr)
        # We've reached the end.
        curr.next_node = prev
        return curr
    return None  # Linked list is empty/

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
        print("    BEFORE: {}".format(head))

        head = reverse_list(head)

        print("     AFTER: {}".format(head))