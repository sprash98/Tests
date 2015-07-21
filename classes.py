

class temp() :

    """ Temporary class to mess around with
    """

    def __init__(self,x=0,y=0):

        self.x = x
        self.y = y


    def __str__(self):

        print("Object is %s+i%s" %(self.x,self.y))


    def __add__(self,other):

        self.x +=other.x
        self.y +=other.y
        return self

    def __sub__(self, other):

        self.x = self.x - other.x
        self.y = self.y - other.y
        return self

    def __eq__(self, other):

        if self.x == other.x and self.y == other.y :
            return 1
        else :
            return 0

    def __ge__(self, other):

        myval = self.x**2 + self.y**2
        otherval = other.x**2 + other.y**2

        if myval >= otherval :
            return 1
        else :
            return 0



class Kangaroo(object):
    """a Kangaroo is a marsupial"""

    def __init__(self, contents=None):
        """initialize the pouch contents; the default value is
        an empty list"""

        if contents == None:
            self.pouch_contents = []
        else :
            self.pouch_contents = contents

    def __str__(self):
        """return a string representaion of this Kangaroo and
        the contents of the pouch, with one item per line"""
        t = [ object.__str__(self) + ' with pouch contents:' ]
        for obj in self.pouch_contents:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def put_in_pouch(self, item):
        """add a new item to the pouch contents"""
        self.pouch_contents.append(item)

kanga = Kangaroo()
roo = Kangaroo()
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car keys')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)






