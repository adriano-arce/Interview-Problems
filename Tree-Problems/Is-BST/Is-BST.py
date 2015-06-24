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
        m = (i + j) // 2
        left = Node.recurse_list_to_tree(L, i, m - 1)
        right = Node.recurse_list_to_tree(L, m + 1, j)
        return Node(L[m], left, right)

    @staticmethod
    def list_to_tree(L):
        return Node.recurse_list_to_tree(L, 0, len(L) - 1)


def is_BST_recurse(root, low, high):
    """Returns True iff the tree is a BST and fits between low and high."""
    if not root:
        return True

    return low < root.data < high and \
           is_BST_recurse(root.left, low, root.data) and \
           is_BST_recurse(root.right, root.data, high)


def is_BST(root):
    return is_BST_recurse(root, float("-inf"), float("inf"))
    # if not root:
    # return True
    # if is_BST(root.left) and is_BST(root.right):
    #     predecessor = root.left
    #     if predecessor:
    #         while predecessor.right:
    #             predecessor = predecessor.right
    #         if predecessor.data > root.data:
    #             return False
    #     successor = root.right
    #     if successor:
    #         while successor.left:
    #             successor = successor.left
    #         if successor.data < root.data:
    #             return False
    #     return True
    # return False


if __name__ == "__main__":
    test_trees = [
        Node.list_to_tree([2, 3, 4, 5, 6]),
        Node.list_to_tree([2, 4, 3, 5, 6]),
        Node.list_to_tree([3, 4, 5, 6, 7, 8, 9]),
        Node.list_to_tree([5, 3, 4, 6, 1, 2, 3]),
        Node.list_to_tree([]),
        Node.list_to_tree([3, 4, 5, 6, 7, 9, 8])
    ]
    for index, tree in enumerate(test_trees):
        isBST = is_BST(tree)
        print("Test Case #{}: {}".format(index + 1, isBST))
        print(tree)