#!/usr/bin/env bash

# Read input
read N

# Get the sum of the numbers
sum=0

for i in `seq 1 $N`
do
    read num
    sum=$[$sum + $num]
done

# Print the average
printf "%.3f\n" $(echo "$sum / $N" | bc -l)
