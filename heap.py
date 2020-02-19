class HeapNode():
    """
        Node class for heap tree
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

    def add(self, new_leaf_data):
        # if new_leaf_data > self._data:
        #     if self._right_leaf is None:
        #         self._right_leaf = BST_Node(new_leaf_data)
        #     else:
        #         self._right_leaf.add(new_leaf_data)
        # elif new_leaf_data < self._data:
        #     if self._left_leaf is None:
        #         self._left_leaf = BST_Node(new_leaf_data)
        #     else:
        #         self._left_leaf.add(new_leaf_data)
        pass

    def get_leafs(self):
        return (self._left_leaf, self._right_leaf)


class Heap():

    def __init__(self, root=None):
        self.root = HeapNode(root)

    def __repr__(self):
        pass

    def __len__(self):
        pass

    def add(self, data):
        self.root.add(data)

    def get_min(self):
        return self.head
