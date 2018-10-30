#!/usr/bin/env Rscript

GeometricDistribution <- function(n, p) {
  return(p * (1 - p)^(n - 1))
}

# Parse "input" variables (actually hardcoded)
probability.defective <- 1/3
last.inspection.number.to.find.first.defective <- 5

# Compute the result
result <- 0

for (inspection.number in 1:last.inspection.number.to.find.first.defective) {
  result <- result + GeometricDistribution(inspection.number,
                                           probability.defective)
}

# Print the result
cat(format(round(result, 3), nsmall=3), sep="\n")
