
from Iterator import VectorIterator
from collections.abc import Iterable, Iterator

class Vector(Iterable):

    def __init__(self , size):
        self.size = size;
        self.ds = [i for i in range(size)] 
        pass
    
    def __iter__(self) -> VectorIterator:
        vctIt = VectorIterator(self.ds);
        return vctIt

    
if (__name__ == "__main__"):
    v = Vector(10)
    for i in v:
        print(i)
