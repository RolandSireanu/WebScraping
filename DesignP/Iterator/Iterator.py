
from collections.abc import Iterable, Iterator

class VectorIterator(Iterator):

    def __init__(self , ds):
        self.pos = 0
        self.data = ds
        self.stop = len(self.data)

    def __next__(self):
        self.pos = self.pos + 1;

        try:
            value = self.data[self.pos]
        except IndexError:
            raise StopIteration()

        return value
        


       