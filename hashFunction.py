import math

class hashFunction:
    def __init__(self,a,b,p,M):
        self.a=a
        self.b=b
        self.p=p
        self.M=M

    def hash(self,x)
        #using same logic of java.lang.string hashCode function to convert string to int
        #https://en.wikipedia.org/wiki/Java_hashCode()
        if isinstance(x,int):
            result = ((self.a*x+self.b)%self.p)%self.M
        else:
            #Convert to String
            x=str(x)
            #Convert x to integer
            str_to_int=0
            for i in range(0,len(x)):
                str_to_int+=x[i]*math.pow(31,len(x)-1-i)
            #Use hash function to hash integer
            result = ((self.a * str_to_int + self.b) % self.p) % self.M
        return result
