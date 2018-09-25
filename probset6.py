import sys
import argparse
import next_prime
import random
import hashFunction


def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument("--mode",type=str,default="count",help="Mode of generating data or exam elements")
    parser.add_argument('--algoType',type=str,default='1',help='Algorithm Type')
    parser.add_argument('--numElements',type=int,default=10000,help="number of elements to be generated")
    parser.add_argument("--num_A",type=int,default=100,help="number of A")
    parser.add_argument("--num_B",type=int,default=100,help="number of B")





def algo1():


def hashFunctions(args):
    '''
    Generate hash function use a prime field
    :return: an Array contains A number of hash functions
    '''
    p=next_prime.find_next_prime(args.num_B)
    #generate  A hash functions
    result=[]
    for i in range(0,args.num_A):
        a=random.randint(1,p-1)
        b=random.randint(0,p-1)
        hash_function=hashFunction(a,b,p,args.num_B)
        result.append(hash_function)
    return result

def count(args,inputstream,hashfunctions):
    assert len(inputstream)>0
    assert len(hashfunctions)>0
    #initialize one empty matrix with A rows B cols
    #counter[row][col]
    counter=[[0 for x in range(args.num_B)] for y in range(args.num_A)]
    for element in inputstream:
        for i in range(0,args.num_A):
            counter[i][hashfunctions[i].hash(element)]+=1




if __name__ == "__main__":

