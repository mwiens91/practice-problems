#!/usr/bin/env bash

# Read array elements
idx=0
for line in `cat`
do
    idx=$[$idx + 1]

    # Replace first capital letter with a '.'
    if [[ ${line:0:1} == [A-Z] ]]
    then
        line="."${line:1}
    fi

    # Add the element
    countries[$idx]=$line
done

# Print the elements
echo ${countries[*]}
