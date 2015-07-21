

import re
class  iter():
    """ Class for iterators and generators
    """

    max = 5
    def __init__(self,n):
        self.n = n


    def __iter__(self):

        while self.n <= self.max:
            yield self.n
            self.n += 1





x = 5


for i in iter(2):
    print(i)

s = 'All\nin all this was all in fun'
print(s)
b= set(s.lower())
print(b)
f = re.search(r"All(.*)",s)
print(f.groups(1))

