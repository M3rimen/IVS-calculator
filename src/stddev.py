"""
@file stddev.py
-----------
@brief Calculates the standard deviation of a series of numbers provided via standard input (stdin).

It processes the input, calculates the mean, sum of squares, and the standard deviation.
The result is printed to stdout.

The script expects input in the form of whitespace-separated numbers (multiple lines allowed).

@version 1.0
@date 2025-04-28
"""
import sys
import math_lib as math

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

N = len(data)

if N == 0:
    print("No data provided.", file=sys.stderr) 
    sys.exit(1)

mean = math.sum(data) / N

sum_of_squares = math.sum(x**2 for x in data)

s = math.sqrt((sum_of_squares - N * mean**2) / (N - 1)) # calculate standard deviation

print(s)