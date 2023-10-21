"""
2023/10/21 shining in shanghai
unionfind
"""


class UnionFind:
    """
    initialize a unionfind
    """

    def __init__(self, n):
        self.pa = list(range(n))
        self.size = [1] * n  # size of the current

    """
    Returns the parent of the element x (root element).
    >>> uf = UnionFind(3)
    >>> uf.find(2)
    2
    >>> uf.find(1)
    1
    """

    def find(self, x):
        if self.pa[x] != x:
            self.pa[x] = self.find(self.pa[x])
        return self.pa[x]

    """
    Returns the union of tree x and tree y.
    we connect a tree with fewer nodes to another tree.
    >>> uf = UnionFind(9)
    >>> uf.union(2,3)
    >>> uf.find(3)
    2
    >>> uf.union(3,4)
    >>> uf.union(4)
    2
    """

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size[x] < self.size[y]:
            x, y = y, x
        self.pa[y] = x
        self.size[x] += self.size[y]

    """
    Returns the size of tree x that contains its children
    >>> uf.UnionFind(4)
    >>> uf.getSize(1)
    1
    >>> uf.union(1,2)
    >>> uf.getSize(1)
    2
    """

    def getSize(self, x):
        return self.size[x]


if __name__ == "__main__":
    # test
    uf = UnionFind(6)
    uf.union(1, 2)
    uf.union(2, 4)
    assert uf.getSize(1) == 3
