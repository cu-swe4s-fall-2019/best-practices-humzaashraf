import sys
import math
import argparse


def col_from_file(file_name, col_num): 
    """Take a file name and a column number and create an array

    Parameters
    ----------
    
    file_name : string
    col_num : integer

    Returns
    -------
    V : fill empty array w/ integers from specified column 

    """
    V = []

    f = open(file_name, 'r')

    for l in f:
        A = [int(x) for x in l.split()]
        V.append(A[col_num])

    return(V)


def mean_calc(data_list): 
    """ Take the mean and standard deviation of an array

    Arguments
    ---------
    data_list : array of integers

    Returns
    -------
    mean : mean
    stdev : standard deviation

    """
    mean = sum(data_list)/len(data_list)
    stdev = math.sqrt(sum([(mean-x)**2 for x in data_list]) / len(data_list))

    return(mean)
    return(stdev)


def main():
    parser = argparse.ArgumentParser(
             description='input file and column number; returns the mean & std',
             prog='input arg')

    parser.add_argument('file_name', type=str, help='Name of the file')
    parser.add_argument('col_num', type=int, help='The column number')

    args = parser.parse_args()

	print(args.file_name, args.col_num)

    # Functional validation of output with various argument errors

    try:
        int(args.col_num) == None 
    except ValueError:
        print('Column index must be an integer')
        sys.exit(1)

    try:
        open(file_name, 'r') == None
    except FileNotFoundError:
        print('No file found')
        sys.exit(1)

    try:
        col_from_file(args.file_name,args.col_num) == None 
    except IndexError:
        print('File or list index out of range')
        sys.exit(1)

    try:
        str(args.file_name) == None
    except PermissionError:
        print('File cannot be accessed')
        sys.exit(1)


if __name__ == '__main__':
    main()
