class Array(object):

    def __init__(self, *args):
        self._data = args

    def __str__(self):
        return f'Array{self._data}'

    def __repr__(self):
        return str(self)

    def append(self, new_element):
        self._data += (new_element,)

    def __add__(self, other):
        return Array(*(self._data + other._data))

    def __len__(self):
        return len(self._data)

    def index(self, value):
        for i in range(len(self._data)):
            if self._data[i] == value:
                return i
        return -1

    def __getitem__(self, index):
        return self._data[index]

    def __iter__(self):
        return iter(self._data)