#!/bin/bash

input_file="profile_test.txt" # temporary file for input
profiling_output="../profiling/vystup.txt" # profiling output

# reset the profiling output file
> "$profiling_output"

# generate 10 random numbers and save to input_file
for i in {1..10}; do
    echo $((RANDOM % 2001 - 1000)) >> "$input_file" # random number between -1000 and 1000
done

# run the profiling command and capture its output 
# (except the first line, which is stddev.py output)
echo "Profiling stddev.py with cProfile on a file with 10 random numbers..." >> "$profiling_output"
python3 -m cProfile -s cumulative stddev.py < "$input_file" | tail -n +2 >> "$profiling_output"

# generate 990 random numbers and append to input_file
for i in {1..990}; do
    echo $((RANDOM % 2001 - 1000)) >> "$input_file" 
done

echo "________________________________________________________________________" >> "$profiling_output"
echo "Profiling stddev.py with cProfile on a file with 1 000 random numbers..." >> "$profiling_output"
python3 -m cProfile -s cumulative stddev.py < "$input_file" | tail -n +2 >> "$profiling_output"

# generate 999 000 random numbers and append to input_file
for i in {1..999000}; do
    echo $((RANDOM % 2001 - 1000)) >> "$input_file" 
done

echo "____________________________________________________________________________" >> "$profiling_output"
echo "Profiling stddev.py with cProfile on a file with 1 000 000 random numbers..." >> "$profiling_output"
python3 -m cProfile -s cumulative stddev.py < "$input_file" | tail -n +2 >> "$profiling_output"

echo "Profiling complete. Results saved to $profiling_output."
rm -f "$input_file"