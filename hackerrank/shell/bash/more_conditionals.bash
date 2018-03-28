#!/usr/bin/env bash
read x
read y
read z

num_equal=0

# Count the number of variables equal
if [ $x -eq $y ]
then
    num_equal=$[$num_equal + 1]
fi

if [ $y -eq $z ]
then
    num_equal=$[$num_equal + 1]
fi

if [ $x -eq $z ]
then
    num_equal=$[$num_equal + 1]
fi

# Print the result
if [ $num_equal -gt 1 ]
then
    echo "EQUILATERAL"
elif [ $num_equal -eq 1 ]
then
    echo "ISOSCELES"
else
    echo "SCALENE"
fi
