import copy


class BiNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        data_list = []
        prev, curr = None, self
        while curr:
            if prev != curr.left:
                p = prev.data if prev else None
                c = curr.left.data if curr.left else None
                return "ERROR: {} != {}".format(p, c)
            data_list.append(curr.data)
            prev, curr = curr, curr.right
        return " <-> ".join(map(str, data_list))


def tree_to_DLL(root):
    head, tail = helper(root)
    return head


def helper(root):
    """
    Converts the given tree to a doubly linked list, but also returns both the
    head and the tail.
    """
    if root:
        if root.left:
            left_head, left_tail = helper(root.left)
            left_tail.right, root.left = root, left_tail
        else:
            left_head = root
        if root.right:
            right_head, right_tail = helper(root.right)
            root.right, right_head.left = right_head, root
        else:
            right_tail = root
        return left_head, right_tail
    return None, None


def main():
    node4, node5, node7 = BiNode(4), BiNode(5), BiNode(7)
    node2, node6 = BiNode(2, node4, node5), BiNode(6, node7)
    node3 = BiNode(3, right=node6)
    node1 = BiNode(1, node2, node3)
    test_trees = [
        copy.deepcopy(None),
        copy.deepcopy(node7),
        copy.deepcopy(node6),
        copy.deepcopy(node3),
        copy.deepcopy(node1),
        copy.deepcopy(node2)
    ]
    for i, tree in enumerate(test_trees):
        print("Test Case #{}:".format(i + 1))
        print("    {}".format(tree_to_DLL(tree)))


if __name__ == "__main__":
    main()