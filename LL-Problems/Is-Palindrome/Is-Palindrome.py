class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return Node.pretty_string(self)

    @staticmethod
    def list_to_LL(L):
        """
        Converts the given Python list into a linked list.
        """
        head = None
        for i in range(len(L) - 1, -1, -1):
            head = Node(L[i], head)
        return head

    @staticmethod
    def pretty_string(head):
        data_list = []
        while head:
            data_list.append(str(head.data))
            head = head.next_node
        return "[" + ", ".join(data_list) + "]"


def is_palindrome(head):
    #---------------------------------------------------------------------------
    # Method 1: Iterative approach with stack. n/2 space, 2n time.
    #---------------------------------------------------------------------------
    # slow, fast = head, head
    # stack = []
    # while fast and fast.next_node:
    #     stack.append(slow.data)
    #     slow, fast = slow.next_node, fast.next_node.next_node
    # # All data before slow is now stored in the stack.
    # # If LL is [1, 2, 3, 4, 5], then slow -> 3 and fast -> 5.
    # # If LL is [1, 2, 3, 4],    then slow -> 3 and fast -> None.
    # if fast:
    #     slow = slow.next_node   # Skip the middle node for odd linked lists.
    # while slow:
    #     if slow.data != stack.pop():
    #         return False
    #     slow = slow.next_node
    # return True

    #---------------------------------------------------------------------------
    # Method 2: Modify the LL, then fix afterwards. O(1) space, O(n) time.
    #---------------------------------------------------------------------------
    # Find the second half.
    slow, fast = head, head
    while fast and fast.next_node:
        slow, fast = slow.next_node, fast.next_node.next_node
    if fast:
        slow = slow.next_node
    # Reverse the second half and compare with the first half.
    slow = reverse(slow)
    curr = slow
    is_pal = True
    while curr and is_pal:
        if curr.data != head.data:
            is_pal = False
        curr, head = curr.next_node, head.next_node
    # Undo the reversal and return the result.
    reverse(slow)
    return is_pal


def reverse(head):
    prev = None
    while head:
        head.next_node, prev, head = prev, head, head.next_node
    return prev


def main():
    test_lists = [
        [],
        [1],
        [2, 2],
        [1, 2],
        [1, 2, 3, 4, 5, 4, 3, 2, 1],
        [1, 2, 3, 4, 4, 3, 2, 1],
        [1, 2, 3, 4, 4, 3, 7, 1],
        [1, 2, 3, 6, 5, 4, 3, 2, 1]
    ]
    for i, test_list in enumerate(test_lists):
        linked_list = Node.list_to_LL(test_list)
        before = str(linked_list)
        is_pal = is_palindrome(linked_list)
        after = str(linked_list)
        result = "Palindrome!" if is_pal else "Not a palindrome."
        print("Test Case #{}: {}".format(i + 1, result))
        print("   BEFORE: {}".format(before))
        print("    AFTER: {}".format(after))

if __name__ == "__main__":
    main()