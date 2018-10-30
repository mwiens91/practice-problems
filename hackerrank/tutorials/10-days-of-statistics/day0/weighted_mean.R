#!/usr/bin/env Rscript

# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers.numbers <- as.numeric(unlist(strsplit(lines[2], split=" ")))
numbers.weights <- as.numeric(unlist(strsplit(lines[3], split=" ")))

# Calculate the weighted mean
result <- (numbers.numbers %*% numbers.weights) / sum(numbers.weights)

# Print the result
cat(format(round(result, 1), nsmall=1), sep="\n")
