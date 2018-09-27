import sys
import argparse
import next_prime
import random
from hashFunction import hashFunction
import statistics
import math
import os


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algoType', type=str, default='1', help='Algorithm Type')
    parser.add_argument("--num_A", type=int, default=100, help="number of A")
    parser.add_argument("--num_B", type=int, default=200, help="number of B")
    args = parser.parse_args()
    return args


def algo1(args, counter, hashfunctions, x):
    '''

    :param args: command line argument
    :param counter: counter matrix
    :param hashfunctions: hash functions array
    :param x: element to be quried
    :return: median value according to algo 1
    '''
    to_be_quried = []
    for i in range(0, args.num_A):
        to_be_quried.append(counter[i][hashfunctions[i].hash(x)])
    return statistics.median(to_be_quried)


def algo2(args, counter, hashfunctions, x):
    estimate = []
    for i in range(0, args.num_A):
        position = hashfunctions[i].hash(x)
        # query is odd position and it is not at the end of the array
        if position % 2 == 0 and position < args.num_B - 1:
            neighbor_pos = position + 1
            neighbor = counter[i][neighbor_pos]
        elif position % 2 == 1:
            neighbor_pos = position - 1
            neighbor = counter[i][neighbor_pos]
        else:
            neighbor = 0
        estimate_single = counter[i][position] - neighbor
        estimate.append(estimate_single)
    return statistics.median(estimate)


def hashFunctions(args):
    '''
    Generate hash function use a prime field
    :return: an Array contains A number of hash functions
    '''
    p = next_prime.find_next_prime(args.num_B)
    # generate  A hash functions
    result = []
    for i in range(0, args.num_A):
        a = random.randint(1, p - 1)
        b = random.randint(0, p - 1)
        hash_function = hashFunction(a, b, p, args.num_B)
        result.append(hash_function)
    return result


def count(args, inputstream, hashfunctions):
    assert len(inputstream) > 0
    assert len(hashfunctions) > 0
    # initialize one empty matrix with A rows B cols
    # counter[row][col]
    counter = [[0 for x in range(args.num_B)] for y in range(args.num_A)]
    for element in inputstream:
        for i in range(0, args.num_A):
            counter[i][hashfunctions[i].hash(element)] += 1
    return counter


def uniform_generater(n, m):
    assert m < n
    inputstream = []
    for i in range(0, n):
        inputstream.append(random.randint(0, m - 1))
    return inputstream


def exponential_generater(n, m):
    assert m < n
    inputstream = []
    stream_range = range(0, m)
    stream_probability = []
    for i in range(0, m):
        stream_probability.append(math.pow(1 / 2, i + 1))
    for i in range(0, n):
        inputstream.append(random.choices(stream_range, stream_probability))
    return inputstream


def real_world_data_generater(input_path):
    try:
        with open(input_path, 'r') as myfile:
            data = myfile.read().replace('\n', '')
    except:
        raise ValueError('could not open {}'.format(input_path))
        exit(1)
    inputstream = data.split(" ")
    return inputstream


if __name__ == "__main__":
    args = get_args()
    inputstream = uniform_generater(100000, 100)
    hashfunctions = hashFunctions(args)
    counter = count(args, inputstream, hashfunctions)
    unique_element_input_stream = set(inputstream)
    for element in unique_element_input_stream:
        algo1_query = algo1(args, counter, hashfunctions, element)
        algo2_query = algo2(args, counter, hashfunctions, element)
        print("Element {}".format(element))
        print("algo 1 query result is {}".format(algo1_query))
        print("algo 2 query result is {}".format(algo2_query))
