import math

class NumException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

def simple(a,b):
    nums=[]
    if b<a or a<0:
        raise NumException("Bad interval of numbers")
    else:

        if a<=2 and b>2:
            nums.append(2)
            i=3
        elif a<=2 and b==2:
            nums.append(2)
            return nums
        else:
            i=math.ceil(a)                     #rounding the number up
        while i<=b:
            j=i-1
            kol=0
            while j>=2:
                if i/j==i/float(j):        
                    break
                else:
                    kol=kol+1
                j=j-1
            if kol==i-2:
                nums.append(i)
            i=i+1
        return nums

import unittest


class Tests(unittest.TestCase):

    def true_input(self):
        self.a=-2
        self.b=10
        self.assertRaises (NumException, simple, self.a, self.b)

    def test_small(self):
        self.a=1
        self.b=2
        self.assertEqual([2],simple(self.a,self.b))

    def test_empty(self):
        self.a=8
        self.b=10
        self.assertEqual([],simple(self.a,self.b))

    def test_full(self):
        self.a=1
        self.b=15
        self.assertEqual([2, 3, 5, 7, 11, 13],simple(self.a,self.b))


if __name__=='__main__':
    unittest.main()    
