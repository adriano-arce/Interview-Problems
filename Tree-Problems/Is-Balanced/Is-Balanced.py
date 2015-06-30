class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "\n".join(Node.pretty_string(self, 0))

    @staticmethod
    def pretty_string(root, depth):
        if not root:
            return []
        right = Node.pretty_string(root.right, depth + 1)
        curr = [depth * "   " + str(root.data)]
        left = Node.pretty_string(root.left, depth + 1)
        return right + curr + left

    @staticmethod
    def recurse_list_to_tree(L, i, j):
        if i > j:
            return None
        m = i + (j - i) // 2  # Same as (i + j) // 2, but avoids overflow.
        left = Node.recurse_list_to_tree(L, i, m - 1)
        right = Node.recurse_list_to_tree(L, m + 1, j)
        return Node(L[m], left, right)

    @staticmethod
    def list_to_tree(L):
        return Node.recurse_list_to_tree(L, 0, len(L) - 1)



def is_balanced(root):
    return True


if __name__ == "__main__":
    test_trees = [
        Node.list_to_tree([2, 3, 4, 5, 6]),
        Node.list_to_tree([2, 4, 3, 5]),
        Node.list_to_tree([3, 4, 5, 6, 7, 8, 9]),
        Node.list_to_tree([]),
    ]
    for index, tree in enumerate(test_trees):
        isBST = is_balanced(tree)
        print("Test Case #{}: {}".format(index + 1, isBST))
        print(tree)