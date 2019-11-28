from linked_list import LList


class HM_list():
    """
    Hashmap implementation using standard python-list like a storage
    """
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def __len__(self):
        return self.size

    def __repr__(self):
        result = ''
        for item in self.map:
            if item is not None:
                for pair in item:
                    result = pair.__repr__() + ', ' + result
        return '{ ' + result[:-2] + ' }'

    def __hash__func(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.__hash__func(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value
            self.map[key_hash].append(key_value)

    def get(self, key):
        key_hash = self.__hash__func(key)

        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        else:
            raise KeyError("Key [{}] doesn't exist".format(key))

    def delete(self, key):
        key_hash = self.__hash__func(key)

        if self.map[key_hash] is None:
            raise KeyError("Key [{}] doesn't exist".format(key))
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                return self.map[key_hash].pop(i)


class HM_LList():
    """
    Hashmap which using my implementation of linked-list like a storage
    """

    def __init__(self):
        self.map = LList()
        self.size = 0

    def __len__(self):
        return self.size

    def __repr__(self):
        pass

    def __hash__func(self):
        pass

    def add(self, key, value):
        pass

    def get(self, key):
        pass
