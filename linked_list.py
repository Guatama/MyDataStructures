class Node(object):
    """
        Node class for linked list
    """
    def __init__(self, data=None, next_node=None):
        self._data = data
        self._next_node = next_node

    def __repr__(self):
        return "*" + repr(self._data)

    def __add__(self, other):
        return LList(self, other)

    def __getitem__(self, key):
        return self.get_data()[key]

    def get_data(self):
        return self._data

    def set_data(self, new_data):
        self._data = new_data

    def get_next(self):
        return self._next_node

    def set_next(self, new_next):
        self._next_node = new_next


class LList(object):
    """
        Linked list
    """
    def __init__(self, head=None, *args):
        if head is not None:
            self.head = Node(head)

            if args is not None:
                for item in args:
                    self.insert(item)
        else:
            self.head = head

    def __repr__(self):
        current = self.head
        result = ""

        while current:
            result = result + repr(current) + " -> "
            current = current.get_next()

        if len(result) > 0:
            result = result[:-4]

        result = "[ " + result + " ]"
        return str(result)

    def __len__(self):
        return self._size()

    def __add__(self, other):
        # BUG Possibility of creating infinite loop
        previous = None
        current = self.head

        while current:
            previous = current
            current = current.get_next()

        if previous is None and current is None:
            self.head = other.head
        elif previous is not None and current is None:
            previous.set_next(other.head)
        else:
            current.set_next(other.head)

    def __getitem__(self, key):
        return self._find_pos(key)

    def __iter__(self):
        size = len(self)
        for i in range(size):
            yield self.__getitem__(i)

    def _size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.get_next()
        return count

    def _find_data(self, data):
        current = self.head
        counter = 0
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
                counter += 1

        if current is None:
            raise ValueError("Data not in list")
        return current, counter

    def _find_pos(self, position):
        current = self.head
        found = False
        count = 0

        while current and found is False:
            if count == position:
                found = True
                break
            count += 1
            current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")

        return current

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node

    def find(self, data):
        return self._find_data(data)[0]

    def index(self, data):
        return self._find_data(data)[1]

    def delete(self, data):
        current = self.head
        previous = None
        found = False

        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                previous = current
                current = current.get_next()

        if current is None:
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def clear(self):
        self.head = None


if __name__ == "__main__":
    p1 = LList('Test1', 'Test2', 'Test3', True, 2342)
    print('p1 is ', p1)
    p2 = LList()
    print('p2 is ', p2)
    p2.insert(234)
    p2.insert('New string')
    print('p2 is ', p2)
    p1 + p2
    print('p1 is ', p1)
    for item in p1:
        print(item)
