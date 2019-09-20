import sys
import os
import math
import argparse


def mean_calc(data_list):
    """ Take the mean of an array

    Arguments
    ---------
    data_list : array of integers

    Returns
    -------
    mean : mean

    """
    mean = sum(data_list)/len(data_list)

    print('mean', mean)

    return(mean)

def stdev_calc(data_list):
    """ Take the stdev of an array

    Arguments
    ---------
    data_list : array of integers

    Returns
    -------
    stdev : stdev

    """
    stdev = math.sqrt(sum([(mean-x)**2 for x in data_list]) / len(data_list))
    
    print('stdev', stdev)

    return(stdev)

def main():
    parser = argparse.ArgumentParser(
             description='input file and column number; returns the mean & std',
             prog='input arg')

    parser.add_argument('--file_name', type=str, help='Name of the file')
    parser.add_argument('--col_num', type=int, help='The column number')

    args = parser.parse_args()


    V = []


    try:
        f = open(args.file_name, 'r')
    except FileNotFoundError:
        print('No file found')
        sys.exit(1)
    except PermissionError:
        print('Cannot read')
        sys.exit(1)


    for l in f:
        A = [int(x) for x in l.split()]
        try: 
            V.append(A[args.col_num])
        except ValueError:
            print('Column index must be an integer')
            sys.exit(1)
        except IndexError:
               print('Out of bounds')
               sys.exit(1)


    x = mean_calc(V)
    print(x)

    y = stdev_calc(V)
    print(y)

if __name__ == '__main__':
    main()
