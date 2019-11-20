class BST_Node(object):
    """
        Node class for binary search tree (can be used for
        double linked list)
    """
    def __init__(self, data=None, left_leaf=None, right_leaf=None):
        self._data = data
        self._left_leaf = left_leaf
        self._right_leaf = right_leaf

    def __repr__(self):
        return "<" + repr(self._data) + ">"

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def add_leaf(self, new_leaf_data):
        if new_leaf_data > self._data:
            if self._right_leaf is None:
                self._right_leaf = Node(new_leaf_data)
            else:
                self._right_leaf.add_leaf(new_leaf_data)
        elif new_leaf_data < self._data:
            if self._left_leaf is None:
                self._left_leaf = Node(new_leaf_data)
            else:
                self._left_leaf.add_leaf(new_leaf_data)
        else:
            return

    def get_leafs(self):
        return (self._left_leaf, self._right_leaf)


class BS_Tree():
    """
        Binary Search Tree implementation
    """
    def __init__(self, root=BST_Node()):
        self.root = root

    def __len__(self):
        pass

    def traverse(self):
        pass