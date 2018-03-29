#!/usr/bin/env bash

# Read array elements
idx=0
for line in `cat`
do
    countries[$idx]=$line
    idx=$[$idx + 1]
done

# Print the 4th element
echo ${countries[3]}
