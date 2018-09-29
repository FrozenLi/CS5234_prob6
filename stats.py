import sys
import math

if __name__ == "__main__":
    input_file=sys.argv[1]
    algo1_error_sum=0
    algo2_error_sum=0
    with open(input_file,'r') as f:
        for row in f:
            temp=row.split(",")
            algo1_error=math.fabs(float(temp[-2].strip()))
            algo2_error=math.fabs(float(temp[-3].strip()))
            algo1_error_sum+=algo1_error
            algo2_error_sum+=algo2_error
    print("Algo 1 error is {}".format(algo1_error_sum))
    print("Algo 2 error is {}".format(algo2_error_sum))

