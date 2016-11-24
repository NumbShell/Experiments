from override_example import base as b

#Create a Class that inherent from Base
class inheriting(b.Base):

    #Run init to define variables
    def __init__(self):
        #Init the Base Class
        super().__init__()
        self.x = 17


class inheritingTwo(b.Base):

    #Override the printMe method from Base class
    def printMe(self):
        print ("You just override the printMe method in Base class!")


#Create some objects
obj = inheritingTwo()
obj1 = inheriting()
obj2 = b.Base()

#Prints out the subclasses of class Base
print(b.Base.__subclasses__())

#Prints out some stuff
obj.printMe()
print(obj1.x)

print(obj2.x)
obj2.printMe()

