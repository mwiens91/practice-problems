#!/usr/bin/env Rscript

A.mean <- 0.88
B.mean <- 1.55

A.cost <- 160 + 40 * (A.mean + A.mean^2)
B.cost <- 128 + 40 * (B.mean + B.mean^2)

# Print the results
cat(format(round(A.cost, 3), nsmall=3), sep="\n")
cat(format(round(B.cost, 3), nsmall=3), sep="\n")
