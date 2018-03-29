#!/usr/bin/env bash

# Read array elements that do not contain 'a' or 'A'
idx=0
while read line
do
    if grep -qv 'a\|A' <<< "$line"
    then
        countries[$idx]=$line
        idx=$[$idx + 1]
    fi
done

# Print the elements
echo ${countries[*]}
