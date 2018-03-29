#!/usr/bin/env bash

# Read array elements
idx=0
while read line
do
    countries[$idx]=$line
    idx=$[$idx + 1]
done

# Print the elements
echo ${countries[*]}
