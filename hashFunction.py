import math


class hashFunction():
    def __int__(self,a,b,p,M):
        self.a=a
        self.b=b
        self.p=p
        self.M=M

    def hash(self,x):
        result = ((self.a*x+self.b)%self.p)%self.M
        return result
