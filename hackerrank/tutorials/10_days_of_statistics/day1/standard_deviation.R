#!/usr/bin/env Rscript

# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers.length <- as.numeric(lines[1])
numbers <- as.numeric(unlist(strsplit(lines[2], split=" ")))

# Calculate the population standard deviation
population.sd <- sd(numbers) * sqrt(numbers.length - 1) / sqrt(numbers.length)

# Print the result
cat(format(round(population.sd, 1), nsmall=1), sep="\n")
