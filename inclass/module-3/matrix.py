#!/usr/bin/env python3
## Class example for matrix operations

import json

class Matrix:

    def __init__(self,h,w,load=None):
        self._h=h ## Height (rows)
        self._w=w ## Width (cols)
        self._matrix=[[]]*h
        for i in range(0,self._h):
            self._matrix[i]=[0]*w
        if load is not None:
            for i in range(0,self._h):
                for j in range(0,self._w):
                    self._matrix[i][j]=load[i][j]

    def rows(self):
        return self._h

    def cols(self):
        return self._w

    def get(self,i,j):
        assert i<self.rows()
        assert j<self.cols()
        return self._matrix[i][j]

    def set(self,i,j,v):
        assert i<self.rows()
        assert j<self.cols()
        self._matrix[i][j]=v

    def __str__(self):
        output=[]
        for row in self._matrix:
            str=[]
            for x in row:
                str.append("%4d" % x)
            output.append(" ".join(str))
        return "\n".join(output)
        
    def __repr__(self):
        return str(self._matrix)

    def add(self,m1):
        ## dimensional check
        assert self.rows()==m1.rows()
        assert self.cols()==m1.cols()
        
        for i in range(0,self._h):
            for j in range(0,self._w):
                self._matrix[i][j]+=m1.get(i,j)

    def equal(self,m1):
        ## dimensional check
        assert self.rows()==m1.rows()
        assert self.cols()==m1.cols()
        
        for i in range(0,self._h):
            for j in range(0,self._w):
                if self._matrix[i][j] != m1.get(i,j):
                    return False
        return True

## Tests
def test():
    ## Simple zero matrix
    print("+++ Matrix m")
    m=Matrix(3,2)
    print(m)
    print(repr(m))
    assert repr(m)=="[[0, 0], [0, 0], [0, 0]]"
    assert m.rows()==3
    assert m.cols()==2

    ## Matrix addition
    a=Matrix(3,2,[[1,2],[3,4],[5,6]])
    b=Matrix(3,2,[[10,10],[20,20],[30,30]])
    print("+++ Matrix a")
    print(a)
    print("+++ Matrix b")
    print(b)

    print("+++ Matrix a.add(b)")
    a.add(b)
    print(a)
    print(repr(a))
    assert repr(a)=="[[11, 12], [23, 24], [35, 36]]"

    print("+++ Matrix JSON test")
    f=open("matrix.json")
    d=json.load(f)
    f.close()

    h,w,matrix=d['a']
    a1=Matrix(h,w,matrix)
    h,w,matrix=d['b']
    b1=Matrix(h,w,matrix)

    print("+++ Matrix b = b1")
    assert b.equal(b1)

    print("+++ Matrix a1 != b1")
    assert not a1.equal(b1)

    print("+++ Matrix a1+b1 == r1")
    b1.add(a1)
    h,w,matrix=d['a+b']
    r1=Matrix(h,w,matrix)
    assert b1.equal(r1)

    
## module entry point
if __name__=="__main__":
    print("matrix.py test")
    test()
    print("matrix.py done")
