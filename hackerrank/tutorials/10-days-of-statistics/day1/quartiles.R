#!/usr/bin/env Rscript

# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers <- as.numeric(unlist(strsplit(lines[2], split=" ")))

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
quartiles.2 <- median(numbers)
quartiles.3 <- median(upper.half)

# Print the results
cat(quartiles.1, sep="\n")
cat(quartiles.2, sep="\n")
cat(quartiles.3, sep="\n")
