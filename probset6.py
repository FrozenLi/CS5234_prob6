import sys
import argparse
import next_prime
import random
from hashFunction import hashFunction
import statistics
import math
import draw_bar
from numpy import savetxt


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--algoType', type=str, default='1', help='Algorithm Type')
    parser.add_argument("--num_A", type=int, default=100, help="number of A")
    parser.add_argument("--num_B", type=int, default=200, help="number of B")
    parser.add_argument("--data_generator", type=str, default="uniform_generator",
                        help="enter the data generater, have 3 types"
                             " -- uniform_generator|exponential_generator|real_world_data_generator ")
    parser.add_argument("--real_world_data_input", type=str, default="", help="real world data location")
    parser.add_argument("--result_path", type=str, default="./result.csv", help="path of result csv file")

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
    progress = 0
    # initialize one empty matrix with A rows B cols
    # counter[row][col]
    counter = [[0 for x in range(args.num_B)] for y in range(args.num_A)]
    for element in inputstream:
        for i in range(0, args.num_A):
            counter[i][hashfunctions[i].hash(element)] += 1
        progress += 1
        if progress % 10000 == 0:
            print("Counter has counted {} number of values".format(progress))
    return counter


def uniform_generator(n, m):
    assert m < n
    inputstream = []
    for i in range(0, n):
        inputstream.append(random.randint(0, m - 1))
    return inputstream


def exponential_generator(n, m):
    assert m < n
    inputstream = []
    stream_range = range(0, m)
    stream_probability = []
    for i in range(0, m):
        stream_probability.append(math.pow(1 / 2, i + 1))
    for i in range(0, n):
        inputstream.append(random.choices(stream_range, stream_probability))
    return inputstream


def real_world_data_generator(input_path):
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
    if args.data_generator == "uniform_generator":
        inputstream = uniform_generator(100000, 100)
    elif args.data_generator == "exponential_generator":
        inputstream = exponential_generator(100000, 100)
    elif args.data_generator == "real_world_data_generator":
        inputstream = real_world_data_generator(args.real_world_data_input)
    else:
        print("Data generator type error")
        exit(1)
    hashfunctions = hashFunctions(args)
    counter = count(args, inputstream, hashfunctions)
    unique_element_input_stream = set(inputstream)

    algo1_query_result = []
    algo2_query_result = []
    algo1_diff = []
    algo2_diff = []
    actual_results = []
    labels = []
    writer = open(args.result_path, 'w')
    for element in unique_element_input_stream:
        algo1_query = algo1(args, counter, hashfunctions, element)
        algo2_query = algo2(args, counter, hashfunctions, element)
        actual_result = inputstream.count(element)
        # print("Element {}".format(element))
        # print("algo 1 query result is {}".format(algo1_query))
        # print("algo 2 query result is {}".format(algo2_query))
        # print("Actual result is {}".format(actual_result))
        algo1_query_diff = math.fabs(algo1_query - actual_result)
        algo2_query_diff = math.fabs(algo2_query - actual_result)
        to_write = ",".join(
            [str(element), str(algo1_query), str(algo2_query), str(actual_result), str(algo1_query_diff),
             str(algo2_query_diff)])
        writer.write(to_write)
        algo1_query_result.append(algo1_query)
        algo2_query_result.append(algo2_query)
        algo1_diff.append(algo1_query_diff)
        algo2_diff.append(algo2_query_diff)
        actual_results.append(actual_result)
        labels.append(element)
    writer.close()
    # draw_bar.draw_stats(algo1_query_result,algo2_query_result,actual_results,labels)
    # draw_bar.draw_diff(algo1_diff,algo2_diff,labels)
    print("Counting complete")
