class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None

    def __str__(self):
        str_data_list = []
        p = self.head
        while p:
            str_data_list.append(str(p.data))
            p = p.next_node
        return "[" + ", ".join(str_data_list) + "]"

    def insert(self, data):
        """
        Inserts a new node (with the given data) at the head of the list.
        """
        self.head = Node(data, self.head)


def python_2_linked(python_list):
    linked_list = LinkedList()
    for i in range(len(python_list) - 1, -1, -1):
        linked_list.insert(python_list[i])
    return linked_list

if __name__ == "__main__":
    testLinkedLists = [
        python_2_linked([1, 2, 3, 4])
    ]

    for (index, linkedList) in enumerate(testLinkedLists):
        print("Test String #{}:".format(index + 1))
        print(linkedList)