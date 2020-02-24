
class BubbleSort:

    def __init__(self):
        print("BubbleSort constructor ! ")

    def sort(self , l):
        print("BubbleSort is sorting ... ")

class MergeSort:

    def __init__(self):
        print("Merge sort constructor !")

    def sort(self , l):
        print("MergeSort is sorting ... ")

class SortingFactory:

    def __init__(self):
        print("SortingFactory constructor ! ")

    def getSorter(self , t):
        if(t == "BubbleSort"):
            return BubbleSort()
        elif(t == "MergeSort"):
            return MergeSort()
        else:
            print("Nothing !")




class Sorter:

    def __init__(self):
        pass

    def sort(self , l , t):
        s = SortingFactory()
        ss = s.getSorter(t);
        ss.sort(l)


s = Sorter()
toBeSorted = [2,4,1,56,7];
s.sort(toBeSorted , "BubbleSort")


