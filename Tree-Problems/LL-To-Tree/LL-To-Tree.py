class ListNode:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    @staticmethod
    def list_to_linked_list(L):
        """
        Converts the given Python list into a linked list.
        """
        head = None
        for i in range(len(L) - 1, -1, -1):
            head = ListNode(L[i], head)
        return head


class TreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "\n".join(TreeNode.pretty_string(self, 0))

    @staticmethod
    def pretty_string(root, depth):
        if not root:
            return []
        right = TreeNode.pretty_string(root.right, depth + 1)
        curr = [depth * "   " + str(root.data)]
        left = TreeNode.pretty_string(root.left, depth + 1)
        return right + curr + left

    @staticmethod
    def LL_to_tree(head):
        n = 0
        p = head
        while p:
            n += 1
            p = p.next_node
        __, root = TreeNode.recurse_LL_to_tree(head, 0, n - 1)
        return root

    @staticmethod
    def recurse_LL_to_tree(unvisited, i, j):
        """
        Traverses the ith to jth nodes (inclusive) of the original linked list.
        Returns the next ListNode to be visited and the root of the tree
        corresponding to the traversed section of the linked list.
        """
        if i > j:
            return unvisited, None
        mid = i + (j - i)//2
        unvisited, left = TreeNode.recurse_LL_to_tree(unvisited, i, mid - 1)

        root = TreeNode(unvisited.data, left)
        unvisited = unvisited.next_node

        unvisited, right = TreeNode.recurse_LL_to_tree(unvisited, mid + 1, j)
        root.right = right
        return unvisited, root

if __name__ == "__main__":
    test_lists = [
        ListNode.list_to_linked_list([2, 3, 4, 5, 6, 7, 8]),
        ListNode.list_to_linked_list(list(range(5, 50))),
        ListNode.list_to_linked_list([7, 1, 3, 4, 5, 6]),
        ListNode.list_to_linked_list([]),
        ListNode.list_to_linked_list([1, 2, 3, 4, 5]),
        ListNode.list_to_linked_list([6])
    ]
    for i, LL in enumerate(test_lists):
        print("Test Case #{}:".format(i + 1))
        print(TreeNode.LL_to_tree(LL))