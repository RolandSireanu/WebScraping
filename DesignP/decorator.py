
def myDecorator(f):
    def wrapper(*args):
        print("Inside wrapper")
        f(*args)
        print("Finish !")        
        return "Hello world !"

    return wrapper

@myDecorator
def myFunction(a , b , c):
    print("Inside myfunction !" + str(a) + " " + str(b) + " " + str(c))

print(myFunction(2,4,65))
