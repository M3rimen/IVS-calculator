## @file stddev.py
# @brief Calculates the standard deviation of a series of numbers provided via standard input (stdin).
# It processes the input, calculates the mean, sum of squares, and the standard deviation.
# The result is printed to stdout.
# The script expects input in the form of whitespace-separated numbers (multiple lines allowed).
# @version 1.0
# @date 2025-04-28

import sys
import math_lib as math


## @brief Function to load data from standard input.
# @details This function reads lines from standard input, splits them into individual numbers,
# converts them to floats, and stores them in a list. It handles invalid input.
# Stops reading when EOF is reached.
# @return list of floats
def load_data():
    ## @var data 
    # list for storing input
    data = []
    for line in sys.stdin: # sys.stdin checks for EOF (input() does not)
        line = line.strip() # remove leading and trailing whitespace

        line = line.split() # split by whitespaces

        try:
            line = [float(x) for x in line] # convert string to float
        except ValueError:
            print("Invalid input.", file=sys.stderr) 
            sys.exit(1)

        data.extend(line)

    return data


## @brief Function to calculate the standard deviation of a list of numbers.
# @param data list of numbers
# @return standard deviation of data
def calculate_stddev(data):
    ## @var N 
    # number of elements in data
    N = len(data)

    if N == 0:
        print("No data provided.", file=sys.stderr) 
        sys.exit(1)

    mean = math.sum(data) / N

    sum_of_squares = math.sum(math.square(x) for x in data) # calculate sum of squares

    s = math.sqrt((sum_of_squares - N * math.square(mean)) / (N - 1)) # calculate standard deviation

    return s


# --main--
data = load_data() # load data from stdin
stddev = calculate_stddev(data) # calculate standard deviation
print(stddev) # print result
    
# end of stddev.py