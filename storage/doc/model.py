class Node(object):
    def __init__(self, name, parent=None):
        self.name = name
        self._parent = parent
        if parent:
            parent.add_child(self)
        self._blocks = []
        self._children = []

    def add_block(self, b):
        self._blocks.append(b)

    def add_child(self, ch):
        ch._parent = self
        self._children.append(ch)

    @property
    def blocks(self):
        return self._blocks

    @property
    def children(self):
        return self._children

    @property
    def parent(self):
        return self._parent
