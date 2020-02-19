class BstNode():
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

    def add(self, new_leaf_data):
        if new_leaf_data > self._data:
            if self._right_leaf is None:
                self._right_leaf = BstNode(new_leaf_data)
            else:
                self._right_leaf.add(new_leaf_data)
        elif new_leaf_data < self._data:
            if self._left_leaf is None:
                self._left_leaf = BstNode(new_leaf_data)
            else:
                self._left_leaf.add(new_leaf_data)

    def get_leafs(self):
        return (self._left_leaf, self._right_leaf)


class BsTree():
    """
        Binary Search Tree implementation
    """
    def __init__(self, root=None):
        self.root = BstNode(root)

    def __len__(self):
        pass

    def __repr__(self):
        pass

    def add(self, new_leaf_data):
        self.root.add(new_leaf_data)

    def traverse(self):
        pass

    def get_data(self):
        """
            Traverse tree, and return list with data from all leafs
        """
        pass

    def set_data(self, list_of_data):
        for item in list_of_data:
            if self.root.get_data() is None:
                self.root.set_data(item)
                continue
            self.root.add(item)
