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
    """
    Returns True iff for each node, the depth of its two subtrees never differ
    by more than one.

    Definitions:
         depth(n): The number of edges from n to the root.
        height(n): The number of edges on the longest path from n to a leaf.

    Hence, it follows that:
        height(T) = height(root) = max(depth(n) for n in T) = depth(T)

    Assume that the empty tree is balanced and has depth -1.
    """
    return depth(root) != -2


def depth(root):
    """
    Returns -2 if the tree is not balanced; else, returns its depth.
    """
    if root:
        left_depth = depth(root.left)
        if left_depth == -2:
            return -2
        right_depth = depth(root.right)
        if right_depth == -2:
            return -2
        if abs(left_depth - right_depth) > 1:
            return -2
        return 1 + max(left_depth, right_depth)
    return -1  # The tree is empty.


def main():
    node4, node5, node7 = Node(4), Node(5), Node(7)
    node2, node6 = Node(2, node4, node5), Node(6, node7)
    node3 = Node(3, right=node6)
    node1 = Node(1, node2, node3)
    test_trees = [
        None, node7, node6, node3, node1, node2
    ]
    for index, tree in enumerate(test_trees):
        print("Test Case #{}: {}".format(index + 1, is_balanced(tree)))
        print(tree)

if __name__ == "__main__":
    main()