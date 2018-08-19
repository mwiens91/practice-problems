#!/usr/bin/env Rscript


Mode <- function(x) {
  # Function to find statistical mode. Thanks to Ken Williams on
  # StackOverflow for his post at
  # https://stackoverflow.com/questions/2547402/is-there-a-built-in-function-for-finding-the-mode
  x <- sort(x)
  ux <- unique(x)
  ux[which.max(tabulate(match(x, ux)))]
}


# Read from stdin
lines <- readLines(file("stdin"))

# Parse input
numbers <- as.numeric(unlist(strsplit(lines[2], split=" ")))

# Compute results
result.mean <- mean(numbers)
result.median <- median(numbers)
result.mode <- Mode(numbers)

# Print results
cat(format(round(result.mean, 1), nsmall=1), sep="\n")
cat(format(round(result.median, 1), nsmall=1), sep="\n")
cat(result.mode, sep="\n")
