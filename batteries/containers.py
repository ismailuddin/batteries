"""Containers"""


from typing import Callable, Iterable


class Array:
    """Class for array functionality"""

    def __init__(self, iterable: Iterable) -> None:
        self.iterable = iterable

    def filter(self, func: Callable):
        return Array(list(filter(func, self.iterable)))

    def map(self, func: Callable):
        return Array([func(x) for x in self.iterable])

    def flatten(self):
        return Array([item for sublist in self.iterable for item in sublist])

    def all(self):
        return self.iterable

    def length(self):
        return len(self.iterable)

    def first(self):
        try:
            return self.iterable[0]
        except IndexError:
            return None
