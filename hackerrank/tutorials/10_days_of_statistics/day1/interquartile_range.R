#!/usr/bin/env Rscript

# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers.units <- as.numeric(unlist(strsplit(lines[2], split=" ")))
numbers.frequencies <- as.numeric(unlist(strsplit(lines[3], split=" ")))

# Build the list of numbers
numbers <- rep(numbers.units, numbers.frequencies)

# Split the numbers into two halves
numbers <- sort(numbers)
numbers.length <- length(numbers)

if (numbers.length %% 2 == 0) {
  lower.half <- numbers[1:(numbers.length / 2)]
  upper.half <- numbers[(numbers.length / 2 + 1):numbers.length]
} else {
  lower.half <- numbers[1:(numbers.length %/% 2)]
  upper.half <- numbers[(numbers.length %/% 2 + 2):numbers.length]
}

# Find the quartiles
quartiles.1 <- median(lower.half)
quartiles.3 <- median(upper.half)

# Find the interquartile range
interquartile.range <- quartiles.3 - quartiles.1

# Print the result
cat(format(round(interquartile.range, 1), nsmall=1), sep="\n")
