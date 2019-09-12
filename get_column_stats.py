import sys
import math
import argparse

parser = argparse.ArgumentParser(
            description='input file and column number; returns the mean & std',
            prog='input arg')

parser.add_argument('file_name', type=str, help='Name of the file')

parser.add_argument('col_num', type=int, help='The column number')

args = parser.parse_args()

print(args.file_name, args.col_num)

# file_name = sys.argv[1]
# col_num = int(sys.argv[2])

f = open(args.file_name, 'r')

V = []

for l in f:
    A = [int(x) for x in l.split()]
    V.append(A[args.col_num])

mean = sum(V)/len(V)

stdev = math.sqrt(sum([(mean-x)**2 for x in V]) / len(V))

print('mean:', mean)
print('stdev:', stdev)
