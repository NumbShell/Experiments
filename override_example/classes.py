from override_example import base as b


class inheriting(b.Base):

    def __init__(self):
        self.x = 17


class inheritingTwo(b.Base):

    def printMe(self):
        print ("You just override Welcome from the Base class!")


obj = inheritingTwo()
obj1 = inheriting()
obj2 = b.Base()


obj.printMe()
print(obj1.x)

print(obj2.x)
obj2.printMe()

