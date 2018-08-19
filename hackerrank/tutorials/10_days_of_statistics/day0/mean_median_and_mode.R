#!/usr/bin/env Rscript


# Function to find statistical mode. Thanks to Ken Williams on
# StackOverflow for his post at
# https://stackoverflow.com/questions/2547402/is-there-a-built-in-function-for-finding-the-mode
Mode <- function(x) {
  x <- sort(x)
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}


# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers <- as.numeric(unlist(strsplit(lines[2], split=" ")))

# Compute results
result_mean <- mean(numbers)
result_median <- median(numbers)
result_mode <- Mode(numbers)

# Print results
cat(round(result_mean, 1), sep="\n")
cat(round(result_median, 1), sep="\n")
cat(result_mode, sep="\n")
