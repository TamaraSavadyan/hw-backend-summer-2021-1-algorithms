from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        initial_root = self._root
        stack = [self._root]
        result = []
        
        while stack:
            current = stack.pop()
            self._root = current

            if current in result:
                continue
            result.append(current)

            for node in self._root.outbound[::-1]:
                stack.append(node)

        self._root = initial_root
        return result
        

    def bfs(self) -> list[Node]:
        initial_root = self._root
        stack = [self._root]
        result = []

        while stack:
            current = stack.pop()
            self._root = current

            if current in result:
                continue
            result.append(current) 

            for node in self._root.outbound:
                stack.insert(0, node)

        self._root = initial_root
        return result
        
