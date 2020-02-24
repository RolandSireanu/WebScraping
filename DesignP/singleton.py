

class SingletonClass:

    instance = None

    def __init__(self , arg_nr):
        self.myNumber = arg_nr
        if(SingletonClass.instance != None):
            raise Exception("This is a singleton class")
        else:
           SingletonClass.instance = self

    @staticmethod
    def getInstance():
        if(SingletonClass.instance == None):
            SingletonClass(22)
        return SingletonClass.instance


s = SingletonClass(20)
s = SingletonClass.getInstance()           
#print(s.myNumber)
#print(dir(s))
print("========================")
print(s.__dict__)
print(SingletonClass.__dict__)
